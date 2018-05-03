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

hb_up   = hb.Clone()
hb_down = hb.Clone()

hd = infile.Get("hdQCD")
hd.Scale(35900.)

func = TF1("func","exp([0]+([1]*exp([2]+[3]*x)))+[4]",250,1500)
#func.SetParameter(0,-6.55)
#func.SetParameter(1,0.5634)
#func.SetParameter(2,3.125)
#func.SetParameter(3,-0.006941)
func.SetParameter(0,-34.69)
func.SetParameter(1,2.02)
func.SetParameter(2,2.937)
func.SetParameter(3,-0.0010)
func.SetParameter(4,0.00319)

hb.Multiply(func)

funcup = TF1("funcup","exp([0]+([1]*exp([2]+[3]*x)))+[4]",250,1500)
#funcup.SetParameter(0,-7.504)
#funcup.SetParameter(1,2.217)
#funcup.SetParameter(2,1.71)
#funcup.SetParameter(3,-0.0051)
funcup.SetParameter(0,-27.11)
funcup.SetParameter(1,1.075)
funcup.SetParameter(2,3.336)
funcup.SetParameter(3,-0.00118)
funcup.SetParameter(4,0.0026)
hb_up.Multiply(funcup)

funcdown = TF1("funcdown","exp([0]+([1]*exp([2]+[3]*x)))+[4]",250,1500)
#funcdown.SetParameter(0,-6.41)
#funcdown.SetParameter(1,4.35)
#funcdown.SetParameter(2,1.181)
#funcdown.SetParameter(3,-0.0082)
funcdown.SetParameter(0,-12.52)
funcdown.SetParameter(1,2.33)
funcdown.SetParameter(2,2.004)
funcdown.SetParameter(3,-0.003449)
funcdown.SetParameter(4,0.00301)
hb_down.Multiply(funcdown)

c = TCanvas("c","c",700,800)
c.SetLogy()
c.SetBottomMargin(0.3)
c.SetRightMargin(0.06)
hb_clone = hb.Clone()
hb_clone.Sumw2()
hb.GetYaxis().SetTitle("Events")
hb.GetXaxis().SetTitle(" ")
hb.GetXaxis().SetTitleOffset(1.15)
hb.GetXaxis().SetTitleSize(0)
hb.GetXaxis().SetLabelSize(0)

hb.SetMarkerStyle(20)
hb.Draw("histEP")
hb_up.SetMarkerStyle(20)
hb_up.SetMarkerColor(2)
hb_up.SetLineColor(2)
hb_up.Draw("samehistEP")
hb_down.SetMarkerStyle(20)
hb_down.SetMarkerColor(2)
hb_down.SetLineColor(2)
hb_down.Draw("samehistEP")


leg = TLegend(.45,.7,.9,.9)                                                                                                                                                     
leg.SetFillStyle(0)                                                                                                                                                             
leg.SetBorderSize(0)                                                                                                                                                            
leg.AddEntry(hb ,"Data driven QCD estimate","l")                                                                                                                                     
leg.AddEntry(hb_down ,"+/- Scale and resolution variations","l")                                                                                                                                     
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
ratio = plot_ratio(False,hb_clone,hb_up,"p_{T}^{miss} [GeV]","ratio",0,3,5)
ratio.GetXaxis().SetTitle("p_{T}^{miss} [GeV]")
ratio.SetMarkerStyle(20)
ratio.Draw("ep")
ratio2 = plot_ratio(False,hb_clone,hb_down,"p_{T}^{miss} [GeV]","ratio",0,3,5)
ratio2.Draw("sameep")

#ratio.Fit("pol0","","",250,600)
#gStyle.SetOptStat(0)
#gStyle.SetOptFit(0)

c.SaveAs("/afs/cern.ch/user/z/zdemirag/www/zpt/panda/qcd/Up/estimation.png")
c.SaveAs("/afs/cern.ch/user/z/zdemirag/www/zpt/panda/qcd/Up/estimation.pdf")
c.SaveAs("/afs/cern.ch/user/z/zdemirag/www/zpt/panda/qcd/Up/estimation.C")


c2 = TCanvas("c2","c2",700,700)
c2.SetLogy()
c2.cd()

func.SetLineColor(1)
func.Draw("")
funcup.SetLineColor(2)
funcup.Draw("same")
funcdown.SetLineColor(4)
funcdown.Draw("same")

c2.SaveAs("/afs/cern.ch/user/z/zdemirag/www/zpt/panda/qcd/Up/fitfunction.pdf")
c2.SaveAs("/afs/cern.ch/user/z/zdemirag/www/zpt/panda/qcd/Up/fitfunction.png")
c2.SaveAs("/afs/cern.ch/user/z/zdemirag/www/zpt/panda/qcd/Up/fitfunction.C")
