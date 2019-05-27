#! /usr/bin/env python                                                                                                                                                              
from ROOT import *
from array import array
from tdrStyle import *
import math
from pretty import plot_ratio
setTDRStyle()

c = {}

infile = TFile("qcd_abcd.root","read")
dirList = gDirectory.GetListOfKeys()

i=0
for hist in dirList: 


    h = hist.ReadObj()

    c[i] = TCanvas("c_"+hist.GetName(),"c_"+hist.GetName(),700,700)
    c[i].cd()

    if "h2d" in h.GetName():
        #now make pretty the 2D histograms
        #h2dMET
        h.GetYaxis().SetTitle("#Delta#phi(jet,p_{T}^{miss})")
        h.GetXaxis().SetTitle("p_{T}^{miss} [GeV]")
        h.GetXaxis().SetTitleOffset(1.15)
        h.GetXaxis().SetTitleSize(0.05)
        h.GetXaxis().SetLabelSize(0.04)
        #h.SetMinimum(0)
        #h.SetMinimum(10e5)
        h.Draw("COLZ")


    else:
        h.GetYaxis().SetTitle("Events")
        h.GetXaxis().SetTitle("p_{T}^{miss} [GeV]")
        h.GetXaxis().SetTitleOffset(1.15)
        h.GetXaxis().SetTitleSize(0.05)
        h.GetXaxis().SetLabelSize(0.04)
        c[i].SetLogy()
        h.Draw("HIST")

    c[i].SaveAs("/afs/cern.ch/user/z/zdemirag/www/zpt/panda/qcd2/"+hist.GetName()+".png")
    c[i].SaveAs("/afs/cern.ch/user/z/zdemirag/www/zpt/panda/qcd2/"+hist.GetName()+".pdf")
    c[i].SaveAs("/afs/cern.ch/user/z/zdemirag/www/zpt/panda/qcd2/"+hist.GetName()+".C")

    i=i+1     

