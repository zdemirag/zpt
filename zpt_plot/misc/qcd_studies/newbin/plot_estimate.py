#! /usr/bin/env python                                                                                                                                                           
from ROOT import *
from array import array
from tdrStyle import *
import math
from pretty import plot_ratio
setTDRStyle()

infile = TFile("qcd_abcd.root","read")

hb = infile.Get("hbMET")

hb_z = infile.Get("hbZtoNuNu")
hb_w = infile.Get("hbWJets")

hb_z.Sumw2()
hb_w.Sumw2()

hb_z.Scale(35900.)
hb_w.Scale(35900.)

hb.Add(hb_z,-1)
hb.Add(hb_w,-1)

hd = infile.Get("hdQCD")
hd.Scale(35900.)

hb.Scale(1,"width")
hd.Scale(1,"width")

func = TF1("func","exp([0]+([1]*exp([2]+[3]*x)))+[4]",250,2000)
func.SetParameter(0,-46.36)
func.SetParameter(1,2.47)
func.SetParameter(2,3.002)
func.SetParameter(3,-0.00075)
func.SetParameter(4,0.002872)

#func.SetParameter(0,3.278)
#func.SetParameter(1,-0.03533)
#func.SetParameter(2,-4.341)
#func.SetParameter(3,-0.00317)
hb.Multiply(func)

c = TCanvas("c","c",700,800)
c.SetLogy()
c.SetBottomMargin(0.3)
c.SetRightMargin(0.06)
hb_clone = hb.Clone()
hb_clone.Sumw2()
hb.GetYaxis().SetTitle("Events/GeV")
hb.GetXaxis().SetTitle(" ")
hb.GetXaxis().SetTitleOffset(1.15)
hb.GetXaxis().SetTitleSize(0)
hb.GetXaxis().SetLabelSize(0)

hb.SetMarkerStyle(20)
hb.Draw("histEP")
hd.SetMarkerStyle(20)
hd.SetMarkerColor(2)
hd.SetLineColor(2)
hd.Draw("samehistEP")

leg = TLegend(.45,.7,.9,.9)                                                                                                                                                     
leg.SetFillStyle(0)                                                                                                                                                             
leg.SetBorderSize(0)                                                                                                                                                            
leg.AddEntry(hb ,"Data driven QCD estimate","l")                                                                                                                                     
leg.AddEntry(hd ,"QCD estimate from MC","l")                                                                                                                                     
leg.Draw("same")

Pad = TPad("pad", "pad", 0.0, 0.0, 1.0, 0.9)
Pad.SetTopMargin(0.7)
Pad.SetRightMargin(0.06)
Pad.SetFillColor(0)
Pad.SetGridy(0)
Pad.SetFillStyle(0)
Pad.Draw()
Pad.cd(0)

hd.Sumw2()
ratio = plot_ratio(False,hb_clone,hd,"p_{T}^{miss} [GeV]","ratio",0,5,5)
ratio.GetXaxis().SetTitle("p_{T}^{miss} [GeV]")
ratio.SetMarkerStyle(20)
ratio.Draw("ep")

#ratio.Fit("pol0","","",250,600)
gStyle.SetOptStat(0)
gStyle.SetOptFit(0)

c.SaveAs("/afs/cern.ch/user/z/zdemirag/www/zpt/panda/qcd2/estimation.png")
c.SaveAs("/afs/cern.ch/user/z/zdemirag/www/zpt/panda/qcd2/estimation.pdf")
c.SaveAs("/afs/cern.ch/user/z/zdemirag/www/zpt/panda/qcd2/estimation.C")
