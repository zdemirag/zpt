#! /usr/bin/env python                                                                                                                                                              
from ROOT import *
from array import array
#from tdrStyle import *
import math
#from pretty import plot_cms
#setTDRStyle()

def makevariations(model):

  #bins = [ 250,350,500,700,1000,1500 ]
  #bins = [ 250.0, 275.0, 300.0, 325.0, 350.0, 375.0, 400.0, 450.0, 500.0, 750.0, 1000.0, 1500.0, 2000.0]

  #bins = [ 250.0, 300.0, 350.0, 400.0, 500.0, 750.0, 1000.0, 1500.0]
  #bins =[250,275,300,350,400,450,500,650,800,1150,1500]                                                                                                                                                                                    
  #bins =[250,275,300,350,400,450,500,650,800,1150,1500,2000]   
  bins =[250,275,300,350,400,450,500,650,800,1150,1500]   

  if model == "pdf":
    infile = TFile("/afs/cern.ch/user/z/zdemirag/public/forRaffaele/new_sys/out_pdf.root","READ")
    f_out = TFile("wtow_pdf_sys_newbin.root","recreate")

  if model == "veto":
    infile = TFile("/afs/cern.ch/user/z/zdemirag/public/forRaffaele/new_sys/out_veto.root","READ")
    f_out = TFile("veto_sys_newbin.root","recreate")

  if model == "trigger":
    infile = TFile("/afs/cern.ch/user/z/zdemirag/public/forRaffaele/new_sys/out_triggersys.root","READ")
    f_out = TFile("trigger_sys_newbin.root","recreate")

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
    print obj.GetTitle(), obj.GetName()

    h_orig[i] = obj.Clone();
    h[i] = obj.Clone(); h[i].SetName(obj.GetName()+"_Down")    

    hmj[i] = TH1F(h[i].GetName(),h[i].GetName(),len(bins)-1,array('d',bins))
    hmj_orig[i] = TH1F(h_orig[i].GetName(),h_orig[i].GetName(),len(bins)-1,array('d',bins))

    if model is "veto":
      for b in range(0,len(bins)):
        half_up = (h[i].GetBinContent(h[i].FindBin(hmj[i].GetBinCenter(b))) - 1)/2.0
        hmj_orig[i].SetBinContent(b,1+half_up)
        hmj[i].SetBinContent(b,1-half_up)
        print b, bins[b], hmj_orig[i].GetBinContent(b), hmj[i].GetBinContent(b)
    else:
      for b in range(0,len(bins)):
        hmj_orig[i].SetBinContent(b,h[i].GetBinContent(h[i].FindBin(hmj[i].GetBinCenter(b))))
        hmj[i].SetBinContent(b,2-h[i].GetBinContent(h[i].FindBin(hmj[i].GetBinCenter(b))))
        print b, bins[b], hmj_orig[i].GetBinContent(b), hmj[i].GetBinContent(b)

    hmj[i].SetMaximum(1.1)
    hmj[i].SetMinimum(0.9)
    hmj_orig[i].SetMaximum(1.1)
    hmj_orig[i].SetMinimum(0.9)
    f_out.cd()
    hmj_orig[i].Write()
    hmj[i].Write()

    i+1

  f_out.Close()

################################

makevariations("pdf")
makevariations("trigger")
makevariations("veto")
