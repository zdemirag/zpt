import sys  
import os
import math
import glob

rnames = {"r_s0":"Non-fiducial","r_s1":"200-300","r_s2":"300-400", "r_s3":"400-500", "r_s4":"500-800", "r_s5":"800-1500"}
channame = {'zee':"Z$\\rightarrow$ee",'zmm':"Z$\\rightarrow$\\mu\\mu",'zll':"Z$\\rightarrow$\\ell\\ell",'znn':"Z$\\rightarrow$\\nu\\nu",'zxx':"Z$\\rightarrow$\\ell\\ell+\\nu\\nu"}

def main():  

  chans = ['zee','zmm','zll','znn','zxx']

  res = {}
  for chan in chans:
    files = glob.glob(chan+"*.txt")
    for chanfile in files:
      ext = chanfile.split(".txt")[0].split(chan+"_")[1]
      with open(chanfile,'r') as f:
        for line in f:
          if ("RooArgSet" in line): continue
          if (("r_s" in line) or ("RDY" in line)): 
            if (not res.has_key(chan+"_"+ext)): res[chan+"_"+ext] = {}
            res[chan+"_"+ext][line.split()[0]]= {"r":line.split()[0],"val":line.split()[2].replace("+",""),
                                                 "lo":line.split()[3].split("/")[0].replace("-",""),"hi":line.split()[3].split("/")[1].replace("+","")}


  print "% table 1, charged leptons"
  chans = ['zee','zmm','zll']
  line = "p_{\\rm T}^{\\rm Z} (GeV)"
  for chan in chans:
    line += " & "+channame[chan]
  print line + "\\\\ \\hline"
  line = "Inclusive "
  for chan in chans:
    line += " & "+res[chan+"_total_obs"]["r_s0"]["val"]+"^{+"+res[chan+"_total_obs"]["r_s0"]["hi"]+"}_{-"+res[chan+"_total_obs"]["r_s0"]["lo"]+"}"
  print line + "\\\\ \\hline"
  for r in ["r_s0","r_s1","r_s2","r_s3","r_s4","r_s5"]:
    line = rnames[r]
    for chan in chans:
      line += " & "+res[chan+"_obs"][r]["val"]+"^{+"+res[chan+"_obs"][r]["hi"]+"}_{-"+res[chan+"_obs"][r]["lo"]+"}"
    print line + " \\\\ "
  print "\\hline "


  print "% table 2, znn and comb"
  chans = ['zll','znn','zxx']
  line = "p_{\\rm T}^{\\rm Z} (GeV)"
  for chan in chans:
    line += " & "+channame[chan]
  print line + "\\\\ \\hline"
  line = "Inclusive "
  for chan in chans:
    line += " & "+res[chan+"_total_obs"]["r_s0"]["val"]+"^{+"+res[chan+"_total_obs"]["r_s0"]["hi"]+"}_{-"+res[chan+"_total_obs"]["r_s0"]["lo"]+"}"
  print line + "\\\\ \\hline"
  for r in ["r_s0","r_s1","r_s2","r_s3","r_s4","r_s5"]:
    line = rnames[r]
    for chan in chans:
      line += " & "+res[chan+"_obs"][r]["val"]+"^{+"+res[chan+"_obs"][r]["hi"]+"}_{-"+res[chan+"_obs"][r]["lo"]+"}"
    print line + " \\\\ "
  print "\\hline "



  print "% table 3, znn and comb"
  chans = ['zee', 'zmm', 'zll','znn','zxx']
  line = "p_{\\rm T}^{\\rm Z} (GeV)"
  for chan in chans:
    line += " & "+channame[chan]
  print line + "\\\\ \\hline"
  line = "Inclusive "
  for chan in chans:
    line += " & "+res[chan+"_total_obs"]["r_s0"]["val"]+"^{+"+res[chan+"_total_obs"]["r_s0"]["hi"]+"}_{-"+res[chan+"_total_obs"]["r_s0"]["lo"]+"}"
  print line + "\\\\ \\hline"
  for r in ["r_s0","r_s1","r_s2","r_s3","r_s4","r_s5"]:
    line = rnames[r]
    for chan in chans:
      line += " & "+res[chan+"_obs"][r]["val"]+"^{+"+res[chan+"_obs"][r]["hi"]+"}_{-"+res[chan+"_obs"][r]["lo"]+"}"
    print line + " \\\\ "
  print "\\hline "


  zllall = ""
  zllup = ""
  zlllo = ""
  znnall = ""
  znnup = ""
  znnlo = ""
  zxxall = ""
  zxxup = ""
  zxxlo = ""


  for r in ["r_s0","r_s1","r_s2","r_s3","r_s4","r_s5"]:
    zllall += res["zll_obs"][r]["val"] + ","
    zllup  += res["zll_obs"][r]["hi"] + ","
    zlllo  += res["zll_obs"][r]["lo"] + ","

    znnall += res["znn_obs"][r]["val"] + ","
    znnup  += res["znn_obs"][r]["hi"] + ","
    znnlo  += res["znn_obs"][r]["lo"] + ","

    zxxall += res["zxx_obs"][r]["val"] + ","
    zxxup  += res["zxx_obs"][r]["hi"] + ","
    zxxlo  += res["zxx_obs"][r]["lo"] + ","

  print "double rsZLL[nValues]  = {"+zllall+"};"
  print "double rsZLLUp[nValues] = {"+zllup+"};"
  #print zlllo
  print "double rsZNN[nValues]  = {"+znnall+"};"
  print "double rsZNNUp[nValues] = {"+znnup+"};"
  #print znnlo
  print "double rsZXX[nValues]  = {"+zxxall+"};"
  print "double rsZXXUp[nValues] = {"+zxxup+"};"
  #print zxxlo

if __name__ == '__main__':  
    main()

