#!/bin/sh

combine -M MultiDimFit inputs/workspace_zll_normalized0.root -n zll_normalized0_obs --algo=singles --robustFit=1  --redefineSignalPOIs r_s0,r_s1,RDY_1,RDY_2,RDY_3,RDY_4 
combine -M MultiDimFit inputs/workspace_zll_normalized1.root -n zll_normalized1_obs --algo=singles --robustFit=1  --redefineSignalPOIs r_s0,r_s1,RDY_0,RDY_2,RDY_3,RDY_4

combine -M MultiDimFit inputs/workspace_znn_normalized0.root -n znn_normalized0_obs --algo=singles --robustFit=1  --redefineSignalPOIs r_s0,r_s1,RDY_1,RDY_2,RDY_3,RDY_4 
combine -M MultiDimFit inputs/workspace_znn_normalized1.root -n znn_normalized1_obs --algo=singles --robustFit=1  --redefineSignalPOIs r_s0,r_s1,RDY_0,RDY_2,RDY_3,RDY_4 

combine -M MultiDimFit inputs/workspace_zxx_normalized0.root -n zxx_normalized0_obs --algo=singles --robustFit=1  --redefineSignalPOIs r_s0,r_s1,r_s2,RDY_1,RDY_2,RDY_3,RDY_4 
combine -M MultiDimFit inputs/workspace_zxx_normalized1.root -n zxx_normalized1_obs --algo=singles --robustFit=1  --redefineSignalPOIs r_s0,r_s1,r_s2,RDY_0,RDY_2,RDY_3,RDY_4 

rm -f higgsCombine*.root;
rm -f combine_logger.out;
