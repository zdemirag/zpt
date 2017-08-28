#! /usr/bin/env python                                                                                                                                                              
from ROOT import *
from array import array
import math

def makevariations(cat):

  #bins = [ 250,350,500,700,1000,1500 ]
  #bins = [ 250.0, 275.0, 300.0, 325.0, 350.0, 375.0, 400.0, 450.0, 500.0, 750.0, 1000.0, 1500.0, 2000.0]
  bins = [ 250.0, 300.0, 350.0, 400.0, 500.0, 750.0, 1000.0, 1500.0]

  f_in = TFile("trigger_sys.root","read")
  f_out = TFile("trigger_ratio"+cat+".root","recreate")
  zmm = f_in.Get("zmm_sys"+cat)
  zvv = f_in.Get("zvv_sys"+cat)

  #zmm.Divide(zvv)
  zvv.Divide(zmm)
  zvv_up = zmm.Clone("down")
  for b in range(0,len(bins)):
      if (b == zvv.FindBin(520) or b>zvv.FindBin(520)):
          zvv.SetBinContent(b,1)
      zvv_up.SetBinContent(b,2-zvv.GetBinContent(b))

  zvv.SetName("trig_sys_down"+cat)
  zvv_up.SetName("trig_sys_up"+cat)
  zvv.Write()
  zvv_up.Write()
  f_out.Close()

################################

makevariations("")
