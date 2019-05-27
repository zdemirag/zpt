#! /usr/bin/env python

from ROOT import *
from array import array
from tdrStyle import *
import math
from pretty import plot_ratio
setTDRStyle()

folder = "/desktop/05a/zdemirag/zpt_greenlight/v2/"

ptbins = [250,275,300,350,400,450,500,650,800,1150,1500]

def scale(model):

    #"Zvv_signal"
    infile_central = TFile(folder+"ZtoNuNu_pt.root","read")
    tree_central = infile_central.Get("events")
    h   = TH1D("h"  ,"h"  ,len(ptbins)-1,array('d',ptbins))    
    cuts = "metFilter==1&&pfmet>250   && dphipfmet>0.5 && nLooseLep==0  && fabs(calomet-pfmet)/pfmet<0.5&&jet1Pt>100 && fabs(jet1Eta)<2.4 && jet1IsTight==1 && nTau==0 && jetNMBtags==0"
    weights = "(sf_pu*sf_tt*normalizedWeight*sf_lepID*sf_lepIso*sf_lepTrack*sf_ewkV*sf_metTrig*35900.0)"
    tree_central.Draw("pfmet>>h","("+cuts+" && nLoosePhoton==0)*"+weights)
    h.Scale(1,"width")
    print h.Integral()

    hph = TH1D("hph","hph",len(ptbins)-1,array('d',ptbins))    
    tree_central.Draw("pfmet>>hph","("+cuts+")*"+weights)
    hph.Scale(1,"width")

    c = TCanvas("c","c",700,800)
    c.SetLogy()
    c.SetBottomMargin(0.3)
    c.SetRightMargin(0.06)
    h_clone = h.Clone()
    h.GetYaxis().SetTitle("Events/GeV")
    h.GetXaxis().SetTitle(" ")
    h.GetXaxis().SetTitleOffset(1.15)
    h.GetXaxis().SetTitleSize(0)
    h.GetXaxis().SetLabelSize(0)
    h.Draw("hist")
    hph.SetLineColor(2)
    hph.Draw("histsame")

    leg = TLegend(.35,.8,.9,.9)                                                                                                                                                     
    leg.SetFillStyle(0)                                                                                                                                                             
    leg.SetBorderSize(0)                                                                                                                                                            
    leg.AddEntry(h ,"Zvv estimates with photon veto","l")                                                                                                                                    
    leg.AddEntry(hph ,"Zvv estimates without photon veto","l")                                                                                                                 
    leg.Draw("same")

    Pad = TPad("pad", "pad", 0.0, 0.0, 1.0, 0.9)
    Pad.SetTopMargin(0.7)
    Pad.SetRightMargin(0.06)
    Pad.SetFillColor(0)
    Pad.SetGridy(0)
    Pad.SetFillStyle(0)
    Pad.Draw()
    Pad.cd(0)
    
    ratio = plot_ratio(False,h_clone,hph,"p_{T}^{miss} [GeV]","Uncertainty",0.93,1.07,5)
    ratio.GetXaxis().SetTitle("p_{T}^{miss} [GeV]")
    ratio.Draw("hist")

    f1 = TF1("f1","pol0",250,1500)
    f1.SetParameter(0,1)
    f1.SetLineColor(kGray)
    f1.SetLineStyle(2)
    f1.Draw("same")

    c.SaveAs("/afs/cern.ch/user/z/zdemirag/www/zpt/panda/zvv_phoveto.png")
    c.SaveAs("/afs/cern.ch/user/z/zdemirag/www/zpt/panda/zvv_phoveto.pdf")
    c.SaveAs("/afs/cern.ch/user/z/zdemirag/www/zpt/panda/zvv_phoveto.C")


scale("Zvv")
