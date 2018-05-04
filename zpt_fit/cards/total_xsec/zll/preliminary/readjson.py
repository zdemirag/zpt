#!/usr/bin/env python

import json
import os
import pprint
import sys
import argparse
import math

parser = argparse.ArgumentParser()
parser.add_argument('--input1' , '-i1', help='input json file 1, binned analysis')
parser.add_argument('--input2' , '-i2', help='input json file 2, total analysis')
parser.add_argument('--poi'    , type=int , default=0 , help='the poi you are looking at for the binned analysis')
parser.add_argument('--verbose', type=int , default=0 , help='set verbose level, 0 or 1')
args = parser.parse_args()

if (args.verbose > 0): print "\nInput 1 corresponding to the binned analysis is", args.input1 
settings_poi   = json.load(open(str(args.input1)+'.json'))
POIs     = [ele['name'] for ele in settings_poi['POIs']] ## full list of pois
poi_up = {}; poi_central ={}; poi_down={}

if len(POIs) <= args.poi:
    print "WARNING: There are not that many pois in the binned analysis! Exiting ..."
    quit()

if (args.verbose > 0): print "Full list of nuisances for poi ", POIs[args.poi],
for nuis in settings_poi['params']:
    if (args.verbose > 0): print nuis['name'], POIs[args.poi], nuis[POIs[args.poi]]
    poi_up     [nuis['name']]=nuis[POIs[args.poi]][0]
    poi_central[nuis['name']]=nuis[POIs[args.poi]][1]
    poi_down   [nuis['name']]=nuis[POIs[args.poi]][2]

############################################################################################

if (args.verbose > 0): print "\nInput 2 corresponding to the total analysis is", args.input2
settings_total = json.load(open(str(args.input2)+'.json'))
POIs_total     = [ele['name'] for ele in settings_total['POIs']] ## full list of pois
total_up = {}; total_central ={}; total_down={}

if len(POIs_total) != 1:
    print "WARNING: Total xsec json has more than 1 poi! Something might be wrong! Exiting ..."
    quit()

if (args.verbose > 0): print "Full list of nuisances for total", POIs_total[0],"\n"
for nuis in settings_total['params']:
    if (args.verbose > 0): print nuis['name'], POIs_total[0], nuis[POIs_total[0]]
    total_up     [nuis['name']]=nuis[POIs_total[0]][0]
    total_central[nuis['name']]=nuis[POIs_total[0]][1]
    total_down   [nuis['name']]=nuis[POIs_total[0]][2]

############################################################################################

sum_ratio = 0 ; sum_total = 0; sum_poi =0;

if (args.verbose > 0): print "\nNow doing the comparison between the two json files"
for key in poi_up.keys(): # Iterates through the binned analysis uncertainties
    if (args.verbose > 0): print "The nuisance considered is ", key
    
    if not key in total_down:
        total_down[key]=1.0
        total_up[key]=1.0
        total_central[key]=1.0

    sum_ratio += (1 - (poi_down[key]/poi_central[key])/(total_down[key]/total_central[key]))**2

    sum_total += (1 - (total_down[key]/total_central[key]) ) **2
    sum_poi   += (1 - (poi_down[key]/poi_central[key])) **2

print "\n\n"
print "1-bin     "    , POIs_total[0] , "unc:", str(round(math.sqrt(sum_total),3)*100)+"%"
print "multi-bin "    , POIs[args.poi], "unc:", str(round(math.sqrt(sum_poi),3)*100)+"%"
print "RATIO     "    , POIs[args.poi], "unc:", str(round(math.sqrt(sum_ratio),3)*100)+"%"
print "\n"
