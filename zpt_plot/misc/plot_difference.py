#! /usr/bin/env python

from ROOT import *
from array import array
from tdrStyle import *
import math
from pretty import plot_ratio
setTDRStyle()

folder = "/desktop/05a/zdemirag/fitting_difference/"



ptbins = [250,275,300,350,400,450,500,650,800,1150,1500]

def scale(model):

    #"Zvv_signal"
    infile_central = TFile(folder+"fittingForest_all.root","read")
    tree_central = infile_central.Get(model+"_nlo_signal")
    h   = TH1D("h"  ,"h"  ,len(ptbins)-1,array('d',ptbins))    
    tree_central.Draw("met>>h","weight")
    #h.SetDirectory(0)
    h.Scale(1,"width")
    print h.Integral()

    infile_npv      = TFile(folder+"fittingForest_signal_pv.root","read")
    tree_npv     = infile_npv.Get(model+"_nlo_signal")
    hnpv = TH1D("hnpv","hnpv",len(ptbins)-1,array('d',ptbins))    
    #hnpv.SetDirectory(0)
    tree_npv.Draw("met>>hnpv","weight","goff")
    hnpv.Scale(1,"width")

    infile_npv_lo    = TFile(folder+"fittingForest_signal_pv_lo.root","read")
    tree_npv_lo   = infile_npv_lo.Get(model+"_signal")
    hnpv_lo = TH1D("hnpv_lo","hnpv_lo",len(ptbins)-1,array('d',ptbins))    
    #hdw.SetDirectory(0)
    tree_npv_lo.Draw("met>>hnpv_lo","weight","goff")
    hnpv_lo.Scale(1,"width")

    c = TCanvas("c","c",700,800)
    c.SetLogy()
    c.SetBottomMargin(0.3)
    c.SetRightMargin(0.06)
    h_clone = h.Clone()
    h_clone2 = hnpv.Clone()
    h.GetYaxis().SetTitle("Events/GeV")
    h.GetXaxis().SetTitle(" ")
    h.GetXaxis().SetTitleOffset(1.15)
    h.GetXaxis().SetTitleSize(0)
    h.GetXaxis().SetLabelSize(0)
    #h.SetLineWidth(2)
    h.Draw("hist")
    #hnpv.SetLineWidth(2)
    hnpv.SetLineColor(2)
    hnpv.Draw("histsame")
    #hdw.SetLineWidth(2)
    hnpv_lo.SetLineColor(4)
    hnpv_lo.Draw("histsame")

    leg = TLegend(.35,.8,.9,.9)                                                                                                                                                     
    leg.SetFillStyle(0)                                                                                                                                                             
    leg.SetBorderSize(0)                                                                                                                                                            
    leg.AddEntry(h ,"NLO samples, pu reweighting","l")                                                                                                                 
    leg.AddEntry(hnpv ,"NLO samples, pv reweighting","l")
    leg.AddEntry(hnpv_lo ,"LO samples, pv reweighting","l")
    leg.Draw("same")

    Pad = TPad("pad", "pad", 0.0, 0.0, 1.0, 0.9)
    Pad.SetTopMargin(0.7)
    Pad.SetRightMargin(0.06)
    Pad.SetFillColor(0)
    Pad.SetGridy(0)
    Pad.SetFillStyle(0)
    Pad.Draw()
    Pad.cd(0)
    
    ratio = plot_ratio(False,h_clone,hnpv_lo,"p_{T}^{miss} [GeV]","#frac{NLO with pu}{LO with pv}",0.90,1.10,5)
    ratio.GetXaxis().SetTitle("p_{T}^{miss} [GeV]")
    ratio.GetYaxis().SetTitleSize(0.03)
    ratio.GetYaxis().SetTitleOffset(1.6)

    ratio.SetLineColor(1)
    ratio.Draw("hist")
    #ratio2 = plot_ratio(False,h_clone,hnpv_lo,"p_{T}^{miss} [GeV]","Difference",0.93,1.07,5)
    #ratio2 = plot_ratio(False,h_clone2,hnpv_lo,"p_{T}^{miss} [GeV]","Difference",0.90,1.10,5)
    #ratio.SetLineColor(4)
    #ratio2.Draw("histsame")

    f1 = TF1("f1","pol0",250,1500)
    f1.SetParameter(0,1)
    f1.SetLineColor(kGray)
    f1.SetLineStyle(2)
    f1.Draw("same")

    c.SaveAs("/afs/cern.ch/user/z/zdemirag/www/zpt/panda/"+model+"_difference.png")
    c.SaveAs("/afs/cern.ch/user/z/zdemirag/www/zpt/panda/"+model+"_difference.pdf")
    c.SaveAs("/afs/cern.ch/user/z/zdemirag/www/zpt/panda/"+model+"_difference.C")


scale("Zvv")
scale("Wlv")
