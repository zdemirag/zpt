#! /usr/bin/env python                                                                                                                                                              
from ROOT import *
from array import array
from tdrStyle import *
import math
from pretty import plot_ratio
setTDRStyle()

def makevariations(model):

  #bins = [ 250,350,500,700,1000,1500 ]
  #bins = [ 250.0, 275.0, 300.0, 325.0, 350.0, 375.0, 400.0, 450.0, 500.0, 750.0, 1000.0, 1500.0, 2000.0]

  bins = [ 250.0, 300.0, 350.0, 400.0, 500.0, 750.0, 1000.0, 1500.0]

  if model == "pdf":
    infile = TFile("/afs/cern.ch/user/z/zdemirag/public/forRaffaele/new_sys/out_pdf.root","READ")
    f_out = TFile("wtow_pdf_sys_plot.root","recreate")

  h_orig = {}
  h = {}
  hmj_orig = {}
  hmj = {}
  hv_orig = {}
  hv = {}
  i = 0

  samplehistos = infile.GetListOfKeys()
  for s in samplehistos: 
    obj = s.ReadObj()
    if type(obj)!=type(TH1F()): continue
    samplehist = obj
    #print obj.GetTitle(), obj.GetName()

    h_orig[i] = obj.Clone();
    h[i] = obj.Clone(); h[i].SetName(obj.GetName()+"_Down")    

    hmj[i] = TH1F(h[i].GetName(),h[i].GetName(),len(bins)-1,array('d',bins))
    hmj_orig[i] = TH1F(h_orig[i].GetName(),h_orig[i].GetName(),len(bins)-1,array('d',bins))

    print i, h_orig[i].GetName()

    for b in range(0,len(bins)):
      hmj_orig[i].SetBinContent(b,h[i].GetBinContent(h[i].FindBin(hmj[i].GetBinCenter(b))))
      hmj[i].SetBinContent(b,2-h[i].GetBinContent(h[i].FindBin(hmj[i].GetBinCenter(b))))
      #print b, bins[b], hmj_orig[i].GetBinContent(b), hmj[i].GetBinContent(b)

    #hmj[i].SetMaximum(1.1)
    #hmj[i].SetMinimum(0.9)
    #hmj_orig[i].SetMaximum(1.1)
    #hmj_orig[i].SetMinimum(0.9)
    f_out.cd()
    hmj_orig[i].Write()
    hmj[i].Write()

    i+1

  f_out.Close()
  
  fnew = TFile("wtow_pdf_sys_plot.root","read")
  
  h1 = fnew.Get("pdfvariationsignal")
  h2 = fnew.Get("pdfvariationsinglemuon")

  c_sr = TCanvas("c_sr","c_sr", 600, 700)
  c_sr.SetBottomMargin(0.3)
  c_sr.SetRightMargin(0.06)
  c_sr.cd()

  gStyle.SetOptStat(False)

  htemp  = h1.Clone("htemp")

  h1.SetLineColor(4)
  h1.SetLineWidth(2)
  h1.Draw("hist")
  h2.SetLineColor(2)
  h2.SetLineWidth(2)
  h2.Draw("histsame")

  h1.GetYaxis().SetTitle("Variation")
  h1.GetYaxis().CenterTitle()
  h1.GetXaxis().SetTitle("")
  h2.SetTitle("")
  h1.SetTitle("")
  h1.GetXaxis().SetLabelSize(0)
  
  h1.SetMaximum(h1.GetMaximum()*1.2)

  #legend_sr = TLegend(.60,.65,.82,.92)
  legend_sr = TLegend(.20,.75,.62,.92)
  legend_sr.AddEntry(h1, "W(l#nu) signal region","l")
  legend_sr.AddEntry(h2, "W(#mu#nu) control region","l")
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
  
  pull = plot_ratio(False,htemp,h2,len(bins),"E_{T}^{miss} [GeV]","Uncert. %",0.95,1.05,5)
  pull.SetLineColor(2)
  pull.Draw("HIST0")


  c_sr.SaveAs("/afs/cern.ch/user/z/zdemirag/www/zpt/panda/v2/wpdf.pdf")
  c_sr.SaveAs("/afs/cern.ch/user/z/zdemirag/www/zpt/panda/v2/wpdf.png")
  c_sr.SaveAs("/afs/cern.ch/user/z/zdemirag/www/zpt/panda/v2/wpdf.C")



################################

makevariations("pdf")
