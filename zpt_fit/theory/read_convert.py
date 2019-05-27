# Standard imports
import os,sys,socket,argparse
import ROOT
import math
from array import array
import numpy as np

ROOT.gROOT.SetBatch(True)
ROOT.gStyle.SetOptStat(0)

hname = "initial"
xlo = []
xhi = []
val = []
errminus = []
errplus  = []

output = ROOT.TFile("vvj.root","RECREATE");

file = open("vvj.dat","r") 
for line in file: 
    if line in ['\n', '\r\n']:
        continue
    if "#" in line:
        if "BEGIN HISTO1D" in line: 
            #print line
            hname = line.split()[3]            
            #renew them
            xlo = []
            xhi = []
            val = []
            errminus = []
            errplus  = []
            continue;
        elif "END HISTO1D" in line:
            #print line
            xbinsTab = np.array(xlo)
            xerrsTab = np.array(errplus)
            valTab = np.array(val)
            h = ROOT.TH1F(hname, hname, valTab.size - 1, xbinsTab)

            for i in range(0,len(xbinsTab)):
                #print xerrsTab[i], valTab[i]
                h.SetBinContent(i+1,float(valTab[i]))
                h.SetBinError  (i+1,float(xerrsTab[i]))    
                
                h.GetYaxis().SetTitle(hname)
                h.GetYaxis().SetTitleOffset(1.6)
                h.GetXaxis().SetTitle("Gen boson p_{T}")
                h.GetXaxis().SetTitleOffset(1.2)
                h.SetTitle("")

            c = ROOT.TCanvas("c2","c2",600,600)
            c.SetRightMargin(0.06)    
            h.Draw("hist")
            h.Write()
            c.SaveAs("/afs/cern.ch/user/z/zdemirag/www/zpt/panda/v10/theory/"+hname+".pdf")
            c.SaveAs("/afs/cern.ch/user/z/zdemirag/www/zpt/panda/v10/theory/"+hname+".png")            
            continue;
        else:        
            #print line
            continue;

    #print line
    
    xlo.append(float(line.split()[0]))      
    xhi.append(float(line.split()[1]))      
    val.append(float(line.split()[2]))      
    errminus.append(float(line.split()[3]))
    errplus.append(float(line.split()[4]))

output.Write()
output.Close()
