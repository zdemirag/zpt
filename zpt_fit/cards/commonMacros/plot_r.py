#! /usr/bin/env python

import sys, os, string, re, time, datetime
from multiprocessing import Process
from array import *
from ROOT import *

from tdrStyle import *
setTDRStyle()

folder = '/afs/cern.ch/user/z/zdemirag/www/zpt/panda/v10/'
infolder = "../v10/"
for i in range(0,6):

    if i==0:
        rangelow = 0.5
        rangehigh = 1.5
    else:
        rangelow = 0.8
        rangehigh = 1.2
    
    f1 = TFile(infolder+"higgsCombineTest.MultiDimFit.mH"+str(i)+".000000.root","READ")
    h1 = TH2D("h1","h1",100000,rangelow,rangehigh,100,0,5)
    limit1 = f1.Get("limit")
    limit1.Draw("2*deltaNLL:r_zcat"+str(i)+">>h1","2*deltaNLL<5","goff")

    f2 = TFile(infolder+"higgsCombineTest.MultiDimFit.mH10"+str(i)+".000000.root","READ")
    h2 = TH2D("h2","h2",100000,rangelow,rangehigh,100,0,5)
    limit2 = f2.Get("limit")
    limit2.Draw("2*deltaNLL:r_zcat"+str(i)+">>h2","2*deltaNLL<5","goff")

    c1 = TCanvas("c1","c1",700,700)
    c1.cd()

    h1.GetXaxis().SetTitle("POI "+str(i))
    h1.GetYaxis().SetTitle("2 * Delta NLL")
    h1.GetYaxis().CenterTitle()
    h1.GetYaxis().SetTitleOffset(1.2)
    h1.GetXaxis().SetTitleOffset(1.2)

    h1.SetMarkerColor(2)
    h1.SetMarkerStyle(20)
    h1.SetMarkerSize(0.5)
    h1.Draw()
    h2.SetMarkerColor(4)
    h2.SetMarkerStyle(20)
    h2.SetMarkerSize(0.5)
    h2.Draw("same")

    leg = TLegend(.55,.7,.9,.9)
    leg.SetFillStyle(0)     
    leg.SetBorderSize(0) 
    leg.AddEntry(h1   ,"Full uncertainty","p")
    leg.AddEntry(h2   ,"Stat. only uncertainty","p") 
    leg.Draw("same")

    func = TF1("func","1",0,2);
    func.SetLineColor(kGreen+2);
    func.SetLineStyle(2);
    func.SetLineWidth(2);
    func.Draw("same");

    c1.SaveAs(folder+"/poi_"+str(i)+".pdf")
    c1.SaveAs(folder+"/poi_"+str(i)+".png")
    c1.SaveAs(folder+"/poi_"+str(i)+".C")

    del c1,f1,limit1,f2,limit2,h2,h1, func
