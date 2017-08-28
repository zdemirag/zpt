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


genptbins = [100,250,350,500,700,1000,1500]
ptbins = [250,350,500,700,1000,1500]

#nb = len(ptbins)-1
nb = len(genptbins)-1

h = {}
hshaded = {}

var="pfmet"
varcut = "trueGenBosonPt"

for i in range(nb):
    
    print i, ptbins[i], ptbins[i+1]
    h[i] = TH1D("h"+str(i),varcut+" >= " + str(ptbins[i]) + " && "+varcut+" <" + str(ptbins[i+1]),nb,array('d',ptbins))    
    #h[i] = TH1D("h"+str(i),varcut+" >= " + str(ptbins[i]) + " && "+varcut+" <" + str(ptbins[i+1]),40,0,2000)
    h[i].Sumw2()
    binned_cuts = cuts +" && "+varcut+" >= " + str(ptbins[i]) + " && "+varcut+" <" + str(ptbins[i+1]) + ")"
    print binned_cuts+"*"+weights
    tree0.Draw(var+">>h"+str(i),binned_cuts+"*"+weights,"")
    h[i].Scale(35800,"width")




c1 = TCanvas("c1","c1",900,600)
c1.Divide(3,2)

gStyle.SetOptStat(0);


'''


for i in range(nb):
   
    c1.cd(i+1)
    p1 = c1.cd(i+1);
    p1.SetLogy();
    h[i].GetXaxis().SetTitle("E_{T}^{miss} [GeV]");
    #h[i].GetXaxis().SetTitle("Generator Z p_{T}");
    h[i].GetYaxis().SetTitle("Events/GeV");
    h[i].GetYaxis().SetTitleOffset(1.2)
    h[i].GetXaxis().SetTitleOffset(1.2)
    h[i].GetYaxis().CenterTitle()
    h[i].SetLineColor(4)
    #h[i].SetFillColor(4)
    #h[i].SetFillStyle(3004)

    hshaded[i] = h[i].Clone('hshaded')
    
    hshaded[i].SetLineColor(4)
    hshaded[i].SetFillColor(4)
    hshaded[i].SetFillStyle(3004)
    startBin = h[i].FindBin(ptbins[i])
    endBin   = h[i].FindBin(ptbins[i+1])

    for iB in xrange(0,startBin):
        hshaded[i].SetBinContent(iB,0)

    for iB in xrange(endBin,hshaded[i].GetNbinsX()+1):
        hshaded[i].SetBinContent(iB,0)


    #integral_total = h[i].Integral(0,nb+1)
    #integral_in    = h[i].Integral(startBin,endBin)

    integral_total = h[i].Integral()
    integral_in = hshaded[i].Integral()

    print "*****",i, ptbins[i], ptbins[i+1], startBin, endBin
    print integral_total, integral_in
    ratio = integral_in/integral_total*100


    h[i].SetMaximum(h[i].GetMaximum()*100)
    h[i].Draw("hist")
    hshaded[i].Draw("hist same")

    #leg = TLegend(.55,.7,.9,.9)
    #leg.SetFillStyle(0)
    #leg.SetBorderSize(0)
    #leg.AddEntry(h[i]   ,"Total gen event","l")
    #leg.AddEntry(hshaded,"Area below real data","F")

    latex2 = TLatex()
    latex2.SetNDC()
    latex2.SetTextSize(0.5*c1.GetTopMargin())
    latex2.SetTextFont(42)
    latex2.SetTextAlign(31) # align right
    #atex2.DrawLatex(0.9, 0.94,"35.9 fb^{-1} (13 TeV)")
    latex2.DrawLatex(0.94, 0.94,"(13 TeV)")
    latex2.SetTextSize(0.6*c1.GetTopMargin())
    latex2.SetTextFont(62)
    latex2.SetTextAlign(11) # align right
    latex2.DrawLatex(0.19, 0.85, "CMS")
    latex2.SetTextSize(0.5*c1.GetTopMargin())
    latex2.SetTextFont(52)
    latex2.SetTextAlign(11)
    #atex2.DrawLatex(0.28, 0.85, "Preliminary")          
    latex2.DrawLatex(0.28, 0.85, "Simulation")          
    latex2.SetTextFont(42)
    latex2.DrawLatex(0.19,0.8,"%.2f %% of the signal is in the reco bin"%ratio    )

    print i, nb, ptbins[i],ptbins[i+1]

    latex2.DrawLatex(0.19,0.75," %i GeV < Generator Z p_{T} < %i GeV"%(ptbins[i],ptbins[i+1]))
''' 

c1.cd(6)
h2d = TH2D("h2d","h2d", nb,array('d',ptbins),nb,array('d',ptbins))
tree0.Draw(var+":"+varcut+">>h2d", cuts+" && pfmet>250)*"+weights)

#Create a 1D histogram
#Compute the ratio of (all cuts + gen cut) / gen cut
#Fill each bin of 1D histogram 

#tree0.Draw(var+">>ratio", cuts+"&&")

ratio = TH2D("ratio","ratio",nb,array('d',ptbins),nb,array('d',ptbins))
for iB in xrange(0,ratio.GetNbinsX()):

    numerator = tree0.GetEntries(cuts+" && "+varcut+" >= " + str(ptbins[iB]) + " && "+varcut+" <" + str(ptbins[iB+1])+ ")")
    denominator = tree0.GetEntries(varcut+" >= " + str(ptbins[iB]) + " && "+varcut+" <" + str(ptbins[iB+1]))

    print numerator, denominator, float(numerator)/float(denominator)

    numratio = float(numerator)/float(denominator)

    for iY in xrange(0,ratio.GetNbinsY()):
        ratio.SetBinContent(iB,iY,numratio)


h2d.GetYaxis().SetTitle("E_{T}^{miss} [GeV]")
h2d.GetXaxis().SetTitle("Generator Z p_{T} [GeV]")
h2d.Divide(ratio)
h2d.Scale(1,"width")
h2d.Draw("colz")

#ratio.Draw("colz")

c1.SaveAs(folder+"/signal_template_pt_analysis_gen.pdf")
c1.SaveAs(folder+"/signal_template_pt_analysis_gen.png")
c1.SaveAs(folder+"/signal_template_pt_analysis_gen.C")
