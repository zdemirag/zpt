#! /usr/bin/env python                                                                                                                                                              
from ROOT import *
from array import array
from tdrStyle import *
import math
from pretty import plot_ratio
setTDRStyle()

def kfactor(model):
    infile = TFile("/afs/cern.ch/user/z/zdemirag/lnwork/studies/monojet_kfactors/mcweights/kfactor_vjet_qcd/kfactor_24bins.root","read")

    if model == "z":
        lo_name = "ZJets_LO/inv_pt"
        nlo_qcd = "ZJets_012j_NLO/nominal"
        nlo_ewk = "EWKcorr/Z"

    if model == "w":
        lo_name = "WJets_LO/inv_pt"
        nlo_qcd = "WJets_012j_NLO/nominal"
        nlo_ewk = "EWKcorr/W"

    hlo      = infile.Get(lo_name)
    hnlo_qcd = infile.Get(nlo_qcd)
    hnlo_ewk = infile.Get(nlo_ewk)


    c_sr = TCanvas("c_sr","c_sr", 600, 700)
    c_sr.SetBottomMargin(0.3)
    c_sr.SetRightMargin(0.06)
    c_sr.cd()
    c_sr.SetLogy()

    gStyle.SetOptStat(False)

    htemp  = hnlo_qcd.Clone("htemp")
    htemp2  = hnlo_ewk.Clone("htemp2")

    hlo.SetLineColor(4)
    hlo.SetLineWidth(2)
    hlo.Draw("hist")
    hnlo_qcd.SetLineColor(2)
    hnlo_qcd.SetLineWidth(2)
    hnlo_qcd.Draw("histsame")
    hnlo_ewk.SetLineColor(8)
    hnlo_ewk.SetLineWidth(2)
    hnlo_ewk.Draw("histsame")

    hlo.GetYaxis().SetTitle("Events")
    hlo.GetYaxis().CenterTitle()
    hlo.GetXaxis().SetTitle("")
    hnlo_qcd.SetTitle("")
    hlo.SetTitle("")
    hlo.GetXaxis().SetLabelSize(0)
  
    hlo.SetMaximum(hlo.GetMaximum()*10.0)
    
    legend_sr = TLegend(.60,.65,.82,.92)
    legend_sr.AddEntry(hlo, "LO","l")
    legend_sr.AddEntry(hnlo_qcd, "NLO QCD","l")
    legend_sr.AddEntry(hnlo_ewk, "NLO QCD + EWK","l")
    legend_sr.SetShadowColor(0);
    legend_sr.SetFillColor(0);
    legend_sr.SetLineColor(0);
    legend_sr.Draw("same")
    
    Pad = TPad("pad", "pad", 0.0, 0.0, 1.0, 0.9)
    Pad.SetTopMargin(0.7)
    Pad.SetRightMargin(0.06)
    Pad.SetFillColor(0)
    Pad.SetFillStyle(0)
    Pad.Draw()
    Pad.cd(0)

    pull = plot_ratio(False,htemp,hlo,htemp.GetNbinsX(),"Gen boson p_{T} [GeV]",,"k-factor",0.0,2.0,5)
    pull.SetLineColor(2)
    pull.Draw("HIST0")    
    #pull2 = plot_ratio(False,htemp2,hlo,htemp.GetNbinsX(),"Gen boson p_{T} [GeV]",0.0,2.0,5)

    
    

    c_sr.SaveAs("/afs/cern.ch/user/z/zdemirag/www/zpt/panda/v2/"+model+"_kfactor.pdf")
    c_sr.SaveAs("/afs/cern.ch/user/z/zdemirag/www/zpt/panda/v2/"+model+"_kfactor.png")
    c_sr.SaveAs("/afs/cern.ch/user/z/zdemirag/www/zpt/panda/v2/"+model+"_kfactor.C")




kfactor("z")
