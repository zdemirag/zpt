#! /usr/bin/env python

from ROOT import *
from array import array
from tdrStyle import *
import math
from pretty import plot_ratio
setTDRStyle()

folder = "/desktop/05a/zdemirag/fitting/"


#ptbins = [250,350,500,700,1000,1500]
ptbins = [250,275,300,350,400,450,500,650,800,1150,1500]

def scale(model):

    #"Zvv_signal"
    infile_central = TFile(folder+"fittingForest_signal.root","read")
    tree_central = infile_central.Get("Zvv_signal")
    h   = TH1D("h"  ,"h"  ,len(ptbins)-1,array('d',ptbins))    
    tree_central.Draw("met>>h","weight")
    #h.SetDirectory(0)
    h.Scale(1,"width")
    print h.Integral()

    infile_up      = TFile(folder+"fittingForest_Up_signal.root","read")
    tree_up     = infile_up.Get(model+"_signal")
    hup = TH1D("hup","hup",len(ptbins)-1,array('d',ptbins))    
    #hup.SetDirectory(0)
    tree_up.Draw("met>>hup","weight","goff")
    hup.Scale(1,"width")

    infile_down    = TFile(folder+"fittingForest_Down_signal.root","read")
    tree_down   = infile_down.Get(model+"_signal")
    hdw = TH1D("hdw","hdw",len(ptbins)-1,array('d',ptbins))    
    #hdw.SetDirectory(0)
    tree_down.Draw("met>>hdw","weight","goff")
    hdw.Scale(1,"width")

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
    #h.SetLineWidth(2)
    h.Draw("hist")
    #hup.SetLineWidth(2)
    hup.SetLineColor(2)
    hup.Draw("histsame")
    #hdw.SetLineWidth(2)
    hdw.SetLineColor(2)
    hdw.Draw("histsame")

    leg = TLegend(.35,.8,.9,.9)                                                                                                                                                     
    leg.SetFillStyle(0)                                                                                                                                                             
    leg.SetBorderSize(0)                                                                                                                                                            
    leg.AddEntry(h ,"Zvv central estimates","l")                                                                                                                                    
    leg.AddEntry(hdw ,"+/- Scale and resolution variations","l")                                                                                                                 
    leg.Draw("same")

    Pad = TPad("pad", "pad", 0.0, 0.0, 1.0, 0.9)
    Pad.SetTopMargin(0.7)
    Pad.SetRightMargin(0.06)
    Pad.SetFillColor(0)
    Pad.SetGridy(0)
    Pad.SetFillStyle(0)
    Pad.Draw()
    Pad.cd(0)
    
    ratio = plot_ratio(False,h_clone,hup,"p_{T}^{miss} [GeV]","Uncertainty",0.93,1.07,5)
    ratio.GetXaxis().SetTitle("p_{T}^{miss} [GeV]")
    ratio.Draw("hist")
    ratio2 = plot_ratio(False,h_clone,hdw,"p_{T}^{miss} [GeV]","Uncertainty",0.93,1.07,5)
    ratio2.Draw("histsame")
    ratio2.Draw("histsame")

    f1 = TF1("f1","pol0",250,1500)
    f1.SetParameter(0,1)
    f1.SetLineColor(kGray)
    f1.SetLineStyle(2)
    f1.Draw("same")

    f2 = TF1("f2","pol0",250,1500)
    f2.SetParameter(0,1.04)
    f2.SetLineColor(kGray)
    f2.SetLineStyle(2)
    f2.Draw("same")

    f3 = TF1("f3","pol0",250,1500)
    f3.SetParameter(0,0.96)
    f3.SetLineColor(kGray)
    f3.SetLineStyle(2)
    f3.Draw("same")

    c.SaveAs("/afs/cern.ch/user/z/zdemirag/www/zpt/panda/zvv_variation2.png")
    c.SaveAs("/afs/cern.ch/user/z/zdemirag/www/zpt/panda/zvv_variation2.pdf")
    c.SaveAs("/afs/cern.ch/user/z/zdemirag/www/zpt/panda/zvv_variation2.C")


scale("Zvv")
