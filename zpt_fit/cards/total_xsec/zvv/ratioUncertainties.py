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
parser.add_argument('--relative', type=int , default=1 , help='Show relative uncertainties, 0 or 1')
args = parser.parse_args()

if (args.verbose > 0): print "\nInput 1 corresponding to the binned analysis is", args.input1 
settings_poi   = json.load(open(str(args.input1)+'.json'))
POIs     = [ele['name'] for ele in settings_poi['POIs']] ## full list of pois
poi_up = {}; poi_central ={}; poi_down={}

if len(POIs) <= args.poi:
    print "WARNING: There are not that many pois in the binned analysis! Exiting ..."
    quit()

POI_fit = settings_poi['POIs'][args.poi]['fit']

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
POI_total_fit = settings_total['POIs'][0]['fit']

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

sum_ratio_up   = 0 ; sum_total_up   = 0; sum_poi_up   = 0;
sum_ratio_down = 0 ; sum_total_down = 0; sum_poi_down = 0;

if (args.verbose > 0): print "\nNow doing the comparison between the two json files"
for key in poi_up.keys(): # Iterates through the binned analysis uncertainties
    if (args.verbose > 0): print "The nuisance considered is ", key
    
    if not key in total_down:
        total_up[key]=1.0
        total_central[key]=1.0
        total_down[key]=1.0

    sum_total_up += (1 - (total_up[key]/total_central[key]) ) **2
    sum_poi_up   += (1 - (poi_up[key]/poi_central[key])) **2
    sum_ratio_up += (1 - (poi_up[key]/poi_central[key])/(total_up[key]/total_central[key]))**2

    sum_total_down += (1 - (total_down[key]/total_central[key]) ) **2
    sum_poi_down   += (1 - (poi_down[key]/poi_central[key])) **2
    sum_ratio_down += (1 - (poi_down[key]/poi_central[key])/(total_down[key]/total_central[key]))**2

# Total uncertainty
all_unc_total_up   = abs(POI_total_fit[2] - POI_total_fit[1])/POI_total_fit[1]
all_unc_total_down = abs(POI_total_fit[0] - POI_total_fit[1])/POI_total_fit[1]

all_unc_poi_up     = abs(POI_fit[2] - POI_fit[1])/POI_fit[1]
all_unc_poi_down   = abs(POI_fit[0] - POI_fit[1])/POI_fit[1]

all_unc_total = (POI_total_fit[2] - POI_total_fit[0])/2./POI_total_fit[1]
all_unc_poi   = (POI_fit[2]       - POI_fit[0]      )/2./POI_fit[1]

# Statistical uncertainty
stat_total_up   = math.sqrt(max(all_unc_total_up  *all_unc_total_up  -sum_total_up  ,0.0))
stat_total_down = math.sqrt(max(all_unc_total_down*all_unc_total_down-sum_total_down,0.0))

stat_poi_up     = math.sqrt(max(all_unc_poi_up  *all_unc_poi_up  -sum_poi_up  ,0.0))
stat_poi_down   = math.sqrt(max(all_unc_poi_down*all_unc_poi_down-sum_poi_down,0.0))

stat_total = (stat_total_up+stat_total_down)/2
stat_poi   = (stat_poi_up  +stat_poi_down  )/2

# Systematic uncertainty
sum_total = (math.sqrt(sum_total_up) + math.sqrt(sum_total_down))/2
sum_poi   = (math.sqrt(sum_poi_up)   + math.sqrt(sum_poi_down)  )/2
sum_ratio = (math.sqrt(sum_ratio_up) + math.sqrt(sum_ratio_down))/2

# poi statistical uncertainty plus ratio systematic uncertainty
all_unc_ratio = math.sqrt(stat_poi*stat_poi+sum_ratio*sum_ratio)

scale_total = 1
scale_poi = 1
if (args.relative == 0):
    print "===> Absolute uncertainties, absolute central values"
    scale_total = POI_total_fit[1]
    scale_poi = POI_fit[1]

else:
   print "===> Relative uncertainties, absolute central values"

print "1-bin     ", POIs_total[0] ," res: ",round(POI_total_fit[1],3)           ," +/- ",round(all_unc_total*scale_total,3),"(stat = ",round(stat_total*scale_total,3),", syst = ",round(sum_total*scale_total,3),")"
print "multi-bin ", POIs[args.poi]," res: ",round(POI_fit[1],3)                 ," +/- ",round(all_unc_poi*scale_poi  ,3),"(stat = ",round(stat_poi*scale_poi  ,3),", syst = ",round(sum_poi*scale_poi  ,3),")"
print "Ratio     ", POIs[args.poi]," res: ",round(POI_fit[1]/POI_total_fit[1],3)," +/- ",round(all_unc_ratio*scale_poi,3),"(stat = ",round(stat_poi*scale_poi  ,3),", syst = ",round(sum_ratio*scale_poi,3),")"
