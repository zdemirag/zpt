#! /usr/bin/env python                                                                                                                                                               
import sys, os, string, re, time, datetime
from multiprocessing import Process
from array import *
from ROOT import *

from tdrStyle import *
setTDRStyle()

folder = '/afs/cern.ch/user/z/zdemirag/www/zpt/panda/'

dataDir = "/afs/cern.ch/work/z/zdemirag/public/moriond17/setup80x/vbf_panda/vbf_004_5/"
file0 = TFile(dataDir+"ZtoNuNu.root","READ")
tree0 = file0.Get("events")

#pfmet > 250

cuts = "(metFilter==1 && egmFilter==1 && dphipfmet>0.5 && nLooseLep==0 && nLoosePhoton==0 && fabs(calomet-pfmet)/pfmet<0.5&&jet1Pt>100 && fabs(jet1Eta)<2.4 && jet1IsTight==1 && nTau==0 && jetNMBtags==0"

weights = "(sf_pu*sf_tt*normalizedWeight*sf_lepID*sf_lepIso*sf_lepTrack*sf_ewkV*sf_qcdV*sf_metTrig)"



#genptbins = [100,250,350,500,700,1000,1500]
genptbins = [250,350,500,700,1000,1500]
ptbins = [250,350,500,700,1000,1500]

#nb = len(ptbins)-1
nb = len(genptbins)-1

h = {}
hshaded = {}

var="pfmet"
varcut = "trueGenBosonPt"


c1 = TCanvas("c1","c1",700,600)
gStyle.SetOptStat(0);

#h2d = TH2D("h2d","h2d", nb,array('d',ptbins),nb,array('d',ptbins))
#tree0.Draw(var+":"+varcut+">>h2d", cuts+" && pfmet>250)*"+weights)

#Create a 1D histogram
#Compute the ratio of (all cuts + gen cut) / gen cut
#Fill each bin of 1D histogram 

#tree0.Draw(var+">>ratio", cuts+"&&")

ratio = TH2D("ratio","ratio",nb,array('d',ptbins),nb,array('d',ptbins))
for iB in xrange(0,ratio.GetNbinsX()):

    numcuts = cuts+" && "+varcut+" >= " + str(ptbins[iB]) + " && "+varcut+" <" + str(ptbins[iB+1])+ " && "+var+" >= " + str(ptbins[iB]) + " && "+var+" <" + str(ptbins[iB+1])+ ")"
    dencuts = cuts+" && "+varcut+" >= " + str(ptbins[iB]) + " && "+varcut+" <" + str(ptbins[iB+1])+ ")"
    
    print "num", numcuts
    print "den", dencuts

    numerator   = tree0.GetEntries(numcuts)
    denominator = tree0.GetEntries(dencuts)

    print numerator, denominator, float(numerator)/float(denominator)

    numratio = float(numerator)/float(denominator)

    for iY in xrange(0,ratio.GetNbinsY()):
        if iB==iY:
            print iB, iY, numratio
            ratio.SetBinContent(iB,iY,numratio)
        else:
            ratio.SetBinContent(iB,iY,0)


ratio.GetYaxis().SetTitle("E_{T}^{miss} [GeV]")
ratio.GetXaxis().SetTitle("Generator Z p_{T} [GeV]")
#ratio.Divide(ratio)
#ratio.Scale(1,"width")
ratio.Draw("colz")

#ratio.Draw("colz")

c1.SaveAs(folder+"/signal_template_pt_analysis_gen_purity.pdf")
c1.SaveAs(folder+"/signal_template_pt_analysis_gen_purity.png")
c1.SaveAs(folder+"/signal_template_pt_analysis_gen_purity.C")
