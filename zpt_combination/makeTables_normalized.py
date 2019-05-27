import sys  
import os
import math
import glob

rnames = {"r_s1":"Non-fiducial","r_s0":"200-300","RDY_1":"300-400", "RDY_2":"400-500", "RDY_3":"500-800", "RDY_4":"800-1500"}
channame = {'zll':"Z$\\rightarrow$\\ell\\ell",'znn':"Z$\\rightarrow$\\nu\\nu",'zxx':"Z$\\rightarrow$\\ell\\ell+\\nu\\nu"}


#    r_s0 :    +1.107   -0.059/+0.065 (68%)
#    r_s1 :    +1.069   -0.302/+0.509 (68%)
#   RDY_1 :    +0.979   -0.013/+0.014 (68%)
#   RDY_2 :    +0.964   -0.017/+0.017 (68%)
#   RDY_3 :    +0.942   -0.021/+0.021 (68%)
#   RDY_4 :    +0.871   -0.054/+0.055 (68%)
#Done in 0.28 min (cpu), 0.28 min (real)


def main():  

  chans = ['zll','znn','zxx']

  res = {}
  for chan in chans:
    files = glob.glob(chan+"*.txt")
    print files
    for chanfile in files:
      ext = chanfile.split(".txt")[0].split(chan+"_")[1]
      if "normalized0": 
        with open(chanfile,'r') as f:
          for line in f:
            if ("RooArgSet" in line): continue
            if (("r_s" in line) or ("RDY" in line)): 
              if (not res.has_key(chan+"_"+ext)): res[chan+"_"+ext] = {}
              res[chan+"_"+ext][line.split()[0]]= {"r":line.split()[0],"val":line.split()[2].replace("+",""),
                                                   "lo":line.split()[3].split("/")[0].replace("-",""),"hi":line.split()[3].split("/")[1].replace("+","")}


  print "% table 2, znn and comb"
  chans = ['zll','znn','zxx']
  line = "p_{\\rm T}^{\\rm Z} (GeV)"
  for chan in chans:
    line += " & "+channame[chan]
  print line + "\\\\ \\hline"
  line = "Inclusive "
  for chan in chans:
    print chan
    line += " & "+res[chan+"_normalized0"]["r_s0"]["val"]+"^{+"+res[chan+"_normalized0"]["r_s0"]["hi"]+"}_{-"+res[chan+"_normalized0"]["r_s0"]["lo"]+"}"
  print line + "\\\\ \\hline"
  #for r in ["r_s0","r_s1","r_s2","r_s3","r_s4","r_s5"]:
  for r in ["r_s1","RDY_1","RDY_2","RDY_3","RDY_4"]:
    line = rnames[r]
    for chan in chans:
      line += " & "+res[chan+"_normalized0"][r]["val"]+"^{+"+res[chan+"_normalized0"][r]["hi"]+"}_{-"+res[chan+"_normalized0"][r]["lo"]+"}"
    print line + " \\\\ "
  print "\\hline "


  

if __name__ == '__main__':  
    main()

