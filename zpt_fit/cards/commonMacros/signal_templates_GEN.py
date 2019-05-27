#! /usr/bin/env python                                                                                                                                                               
import sys, os, string, re, time, datetime
from multiprocessing import Process
from array import *
from ROOT import *

from tdrStyle import *
setTDRStyle()

folder = '/afs/cern.ch/user/z/zdemirag/www/zpt/panda/v10/'
dataDir = '/desktop/05a/zdemirag/fittingnlo_test5/'

file0 = TFile(dataDir+"fittingForest_signal.root","READ")
tree0 = file0.Get("Zvv_nlo_signal")

cuts = " (met>250)"
weights = "weight"

ptbins    = [250,275,300,350,400,450,500,650,800,1150,1500]
jetptbins = [0, 50, 100, 150, 200, 250, 300, 350, 400, 500, 800, 1500]

nb = len(jetptbins)-1

h = {}
hshaded = {}

var=["met","jetPt","genJetPt","genBosonPt"]
varname = ["p_{T}^{miss} [GeV]", "Jet p_{T} [GeV]", "Generated Jet p_{T} [GeV]", "Generated Boson p_{T} [GeV]"]
for i in range(len(var)):
    if "met" in var[i]:
        h[i] = TH1D("h"+str(i),"test",len(ptbins)-1,array('d',ptbins))    
    else:
        h[i] = TH1D("h"+str(i),"test",len(jetptbins)-1,array('d',jetptbins))

    h[i].Sumw2()
    tree0.Draw(var[i]+">>h"+str(i),cuts+"*"+weights,"")
    h[i].Scale(35800,"width")

#c1 = TCanvas("c1","c1",900,600)
#c1.Divide(3,2)

c1 = {}

gStyle.SetOptStat(0);

for i in range(len(var)):
    c1[i] = TCanvas("c1","c1",600,600)
    #c1.cd(i+1)
    #p1 = c1.cd(i+1);
    #p1.SetLogy();
    c1[i].SetLogy()
    h[i].GetXaxis().SetTitle(varname[i]);
    h[i].GetYaxis().SetTitle("Events/GeV");
    h[i].GetYaxis().SetTitleOffset(1.2)
    h[i].GetXaxis().SetTitleOffset(1.2)
    h[i].GetYaxis().CenterTitle()
    h[i].SetLineColor(4)
    #h[i].SetFillColor(4)
    #h[i].SetFillStyle(3004)


    h[i].SetMaximum(h[i].GetMaximum()*100)
    h[i].Draw("hist")

    #leg = TLegend(.55,.7,.9,.9)
    #leg.SetFillStyle(0)
    #leg.SetBorderSize(0)
    #leg.AddEntry(h[i]   ,"Total gen event","l")
    #leg.AddEntry(hshaded,"Area below real data","F")

    latex2 = TLatex()
    latex2.SetNDC()
    latex2.SetTextSize(0.5*c1[i].GetTopMargin())
    latex2.SetTextFont(42)
    latex2.SetTextAlign(31) # align right
    #atex2.DrawLatex(0.9, 0.94,"35.9 fb^{-1} (13 TeV)")
    latex2.DrawLatex(0.94, 0.94,"(13 TeV)")
    latex2.SetTextSize(0.6*c1[i].GetTopMargin())
    latex2.SetTextFont(62)
    latex2.SetTextAlign(11) # align right
    latex2.DrawLatex(0.19, 0.85, "CMS")
    latex2.SetTextSize(0.5*c1[i].GetTopMargin())
    latex2.SetTextFont(52)
    latex2.SetTextAlign(11)
    #atex2.DrawLatex(0.28, 0.85, "Preliminary")          
    latex2.DrawLatex(0.28, 0.85, "Simulation")          
    latex2.SetTextFont(42)
    #latex2.DrawLatex(0.19,0.8,"%.2f %% of the signal is in the reco bin"%ratio    )

    print i, nb, ptbins[i],ptbins[i+1]

    #latex2.DrawLatex(0.19,0.75," %i GeV < Generator Z p_{T} < %i GeV"%(genptbins[i],genptbins[i+1]))

    c1[i].SaveAs(folder+"/signal_template_"+str(var[i])+".C")
    c1[i].SaveAs(folder+"/signal_template_"+str(var[i])+".pdf")
    c1[i].SaveAs(folder+"/signal_template_"+str(var[i])+".png")
    c1[i].SaveAs(folder+"/signal_template_"+str(var[i])+".root")

