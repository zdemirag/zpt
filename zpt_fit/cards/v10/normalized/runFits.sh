#!/bin/sh

combine -M MultiDimFit inputs/workspace_zmm.root        -n zmm_obs        --algo=singles --robustFit=1 
combine -M MultiDimFit inputs/workspace_zee.root        -n zee_obs        --algo=singles --robustFit=1 
combine -M MultiDimFit inputs/workspace_zll.root        -n zll_obs        --algo=singles --robustFit=1 
combine -M MultiDimFit inputs/workspace_znn.root        -n znn_obs        --algo=singles --robustFit=1 
combine -M MultiDimFit inputs/workspace_zxx.root        -n zxx_obs        --algo=singles --robustFit=1 
combine -M MultiDimFit inputs/workspace_zmm_total.root  -n zmm_total_obs  --algo=singles --robustFit=1
combine -M MultiDimFit inputs/workspace_zee_total.root  -n zee_total_obs  --algo=singles --robustFit=1
combine -M MultiDimFit inputs/workspace_zll_total.root  -n zll_total_obs  --algo=singles --robustFit=1
combine -M MultiDimFit inputs/workspace_zll_total0.root -n zll_total0_obs --algo=singles --robustFit=1 
combine -M MultiDimFit inputs/workspace_zll_total1.root -n zll_total1_obs --algo=singles --robustFit=1 
combine -M MultiDimFit inputs/workspace_znn_total.root  -n znn_total_obs  --algo=singles --robustFit=1
combine -M MultiDimFit inputs/workspace_znn_total0.root -n znn_total0_obs --algo=singles --robustFit=1 
combine -M MultiDimFit inputs/workspace_znn_total1.root -n znn_total1_obs --algo=singles --robustFit=1 
combine -M MultiDimFit inputs/workspace_zxx_total.root  -n zxx_total_obs  --algo=singles --robustFit=1
combine -M MultiDimFit inputs/workspace_zxx_total0.root -n zxx_total0_obs --algo=singles --robustFit=1 
combine -M MultiDimFit inputs/workspace_zxx_total1.root -n zxx_total1_obs --algo=singles --robustFit=1 

#combine -M MultiDimFit workspace_zll.root -n zll_exp --algo=singles --robustFit=1 -t -1 --setParameters r_s1=1,r_s2=1,r_s3=1,r_s4=1,r_s5=1
#combine -M MultiDimFit workspace_zll.root -n zll_obs --algo=singles --robustFit=1 
#combine -M MultiDimFit workspace_zll.root -n zll_r_s1 --algo=grid --robustFit=1 --points=600 -P r_s1 --floatOtherPOIs=1 --setParameterRanges r_s1=0.7,1.3:r_s2=0.7,1.3:r_s3=0.7,1.3:r_s4=0.7,1.3:r_s5=0.7,1.3
#combine -M MultiDimFit workspace_zll.root -n zll_r_s2 --algo=grid --robustFit=1 --points=600 -P r_s2 --floatOtherPOIs=1 --setParameterRanges r_s1=0.7,1.3:r_s2=0.7,1.3:r_s3=0.7,1.3:r_s4=0.7,1.3:r_s5=0.7,1.3
#combine -M MultiDimFit workspace_zll.root -n zll_r_s3 --algo=grid --robustFit=1 --points=600 -P r_s3 --floatOtherPOIs=1 --setParameterRanges r_s1=0.7,1.3:r_s2=0.7,1.3:r_s3=0.7,1.3:r_s4=0.7,1.3:r_s5=0.7,1.3
#combine -M MultiDimFit workspace_zll.root -n zll_r_s4 --algo=grid --robustFit=1 --points=600 -P r_s4 --floatOtherPOIs=1 --setParameterRanges r_s1=0.7,1.3:r_s2=0.7,1.3:r_s3=0.7,1.3:r_s4=0.7,1.3:r_s5=0.7,1.3
#combine -M MultiDimFit workspace_zll.root -n zll_r_s5 --algo=grid --robustFit=1 --points=600 -P r_s5 --floatOtherPOIs=1 --setParameterRanges r_s1=0.7,1.3:r_s2=0.7,1.3:r_s3=0.7,1.3:r_s4=0.7,1.3:r_s5=0.7,1.3
#combine -M MultiDimFit workspace_zll.root -n zll_r_s1_statonly --algo=grid --robustFit=1 --points=600 -P r_s1 --floatOtherPOIs=1 --setParameterRanges r_s1=0.7,1.3:r_s2=0.7,1.3:r_s3=0.7,1.3:r_s4=0.7,1.3:r_s5=0.7,1.3 --fastScan
#combine -M MultiDimFit workspace_zll.root -n zll_r_s2_statonly --algo=grid --robustFit=1 --points=600 -P r_s2 --floatOtherPOIs=1 --setParameterRanges r_s1=0.7,1.3:r_s2=0.7,1.3:r_s3=0.7,1.3:r_s4=0.7,1.3:r_s5=0.7,1.3 --fastScan
#combine -M MultiDimFit workspace_zll.root -n zll_r_s3_statonly --algo=grid --robustFit=1 --points=600 -P r_s3 --floatOtherPOIs=1 --setParameterRanges r_s1=0.7,1.3:r_s2=0.7,1.3:r_s3=0.7,1.3:r_s4=0.7,1.3:r_s5=0.7,1.3 --fastScan
#combine -M MultiDimFit workspace_zll.root -n zll_r_s4_statonly --algo=grid --robustFit=1 --points=600 -P r_s4 --floatOtherPOIs=1 --setParameterRanges r_s1=0.7,1.3:r_s2=0.7,1.3:r_s3=0.7,1.3:r_s4=0.7,1.3:r_s5=0.7,1.3 --fastScan
#combine -M MultiDimFit workspace_zll.root -n zll_r_s5_statonly --algo=grid --robustFit=1 --points=600 -P r_s5 --floatOtherPOIs=1 --setParameterRanges r_s1=0.7,1.3:r_s2=0.7,1.3:r_s3=0.7,1.3:r_s4=0.7,1.3:r_s5=0.7,1.3 --fastScan

#combine -M MultiDimFit workspace_znn.root -n znn_exp --algo=singles --robustFit=1 -t -1 --setParameters r_s0=1,r_s1=1,r_s2=1,r_s3=1,r_s4=1,r_s5=1
#combine -M MultiDimFit workspace_znn.root -n znn_obs --algo=singles --robustFit=1 
#combine -M MultiDimFit workspace_znn.root -n znn_r_s0 --algo=grid --robustFit=1 --points=600 -P r_s0 --floatOtherPOIs=1 --setParameterRanges r_s0=0.7,1.3:r_s1=0.7,1.3:r_s2=0.7,1.3:r_s3=0.7,1.3:r_s4=0.7,1.3:r_s5=0.7,1.3
#combine -M MultiDimFit workspace_znn.root -n znn_r_s1 --algo=grid --robustFit=1 --points=600 -P r_s1 --floatOtherPOIs=1 --setParameterRanges r_s0=0.7,1.3:r_s1=0.7,1.3:r_s2=0.7,1.3:r_s3=0.7,1.3:r_s4=0.7,1.3:r_s5=0.7,1.3
#combine -M MultiDimFit workspace_znn.root -n znn_r_s2 --algo=grid --robustFit=1 --points=600 -P r_s2 --floatOtherPOIs=1 --setParameterRanges r_s0=0.7,1.3:r_s1=0.7,1.3:r_s2=0.7,1.3:r_s3=0.7,1.3:r_s4=0.7,1.3:r_s5=0.7,1.3
#combine -M MultiDimFit workspace_znn.root -n znn_r_s3 --algo=grid --robustFit=1 --points=600 -P r_s3 --floatOtherPOIs=1 --setParameterRanges r_s0=0.7,1.3:r_s1=0.7,1.3:r_s2=0.7,1.3:r_s3=0.7,1.3:r_s4=0.7,1.3:r_s5=0.7,1.3
#combine -M MultiDimFit workspace_znn.root -n znn_r_s4 --algo=grid --robustFit=1 --points=600 -P r_s4 --floatOtherPOIs=1 --setParameterRanges r_s0=0.7,1.3:r_s1=0.7,1.3:r_s2=0.7,1.3:r_s3=0.7,1.3:r_s4=0.7,1.3:r_s5=0.7,1.3
#combine -M MultiDimFit workspace_znn.root -n znn_r_s5 --algo=grid --robustFit=1 --points=600 -P r_s5 --floatOtherPOIs=1 --setParameterRanges r_s0=0.7,1.3:r_s1=0.7,1.3:r_s2=0.7,1.3:r_s3=0.7,1.3:r_s4=0.7,1.3:r_s5=0.7,1.3
#combine -M MultiDimFit workspace_znn.root -n znn_r_s0_statonly --algo=grid --robustFit=1 --points=600 -P r_s0 --floatOtherPOIs=1 --setParameterRanges r_s0=0.7,1.3:r_s1=0.7,1.3:r_s2=0.7,1.3:r_s3=0.7,1.3:r_s4=0.7,1.3:r_s5=0.7,1.3 --fastScan
#combine -M MultiDimFit workspace_znn.root -n znn_r_s1_statonly --algo=grid --robustFit=1 --points=600 -P r_s1 --floatOtherPOIs=1 --setParameterRanges r_s0=0.7,1.3:r_s1=0.7,1.3:r_s2=0.7,1.3:r_s3=0.7,1.3:r_s4=0.7,1.3:r_s5=0.7,1.3 --fastScan
#combine -M MultiDimFit workspace_znn.root -n znn_r_s2_statonly --algo=grid --robustFit=1 --points=600 -P r_s2 --floatOtherPOIs=1 --setParameterRanges r_s0=0.7,1.3:r_s1=0.7,1.3:r_s2=0.7,1.3:r_s3=0.7,1.3:r_s4=0.7,1.3:r_s5=0.7,1.3 --fastScan
#combine -M MultiDimFit workspace_znn.root -n znn_r_s3_statonly --algo=grid --robustFit=1 --points=600 -P r_s3 --floatOtherPOIs=1 --setParameterRanges r_s0=0.7,1.3:r_s1=0.7,1.3:r_s2=0.7,1.3:r_s3=0.7,1.3:r_s4=0.7,1.3:r_s5=0.7,1.3 --fastScan
#combine -M MultiDimFit workspace_znn.root -n znn_r_s4_statonly --algo=grid --robustFit=1 --points=600 -P r_s4 --floatOtherPOIs=1 --setParameterRanges r_s0=0.7,1.3:r_s1=0.7,1.3:r_s2=0.7,1.3:r_s3=0.7,1.3:r_s4=0.7,1.3:r_s5=0.7,1.3 --fastScan
#combine -M MultiDimFit workspace_znn.root -n znn_r_s5_statonly --algo=grid --robustFit=1 --points=600 -P r_s5 --floatOtherPOIs=1 --setParameterRanges r_s0=0.7,1.3:r_s1=0.7,1.3:r_s2=0.7,1.3:r_s3=0.7,1.3:r_s4=0.7,1.3:r_s5=0.7,1.3 --fastScan

#combine -M MultiDimFit workspace_zxx.root -n zxx_exp --algo=singles --robustFit=1 -t -1 --setParameters r_s0=1,r_s1=1,r_s2=1,r_s3=1,r_s4=1,r_s5=1
#combine -M MultiDimFit workspace_zxx.root -n zxx_obs --algo=singles --robustFit=1
#combine -M MultiDimFit workspace_zxx.root -n zxx_r_s0 --algo=grid --robustFit=1 --points=600 -P r_s0 --floatOtherPOIs=1 --setParameterRanges r_s0=0.7,1.3:r_s1=0.7,1.3:r_s2=0.7,1.3:r_s3=0.7,1.3:r_s4=0.7,1.3:r_s5=0.7,1.3
#combine -M MultiDimFit workspace_zxx.root -n zxx_r_s1 --algo=grid --robustFit=1 --points=600 -P r_s1 --floatOtherPOIs=1 --setParameterRanges r_s0=0.7,1.3:r_s1=0.7,1.3:r_s2=0.7,1.3:r_s3=0.7,1.3:r_s4=0.7,1.3:r_s5=0.7,1.3
#combine -M MultiDimFit workspace_zxx.root -n zxx_r_s2 --algo=grid --robustFit=1 --points=600 -P r_s2 --floatOtherPOIs=1 --setParameterRanges r_s0=0.7,1.3:r_s1=0.7,1.3:r_s2=0.7,1.3:r_s3=0.7,1.3:r_s4=0.7,1.3:r_s5=0.7,1.3
#combine -M MultiDimFit workspace_zxx.root -n zxx_r_s3 --algo=grid --robustFit=1 --points=600 -P r_s3 --floatOtherPOIs=1 --setParameterRanges r_s0=0.7,1.3:r_s1=0.7,1.3:r_s2=0.7,1.3:r_s3=0.7,1.3:r_s4=0.7,1.3:r_s5=0.7,1.3
#combine -M MultiDimFit workspace_zxx.root -n zxx_r_s4 --algo=grid --robustFit=1 --points=600 -P r_s4 --floatOtherPOIs=1 --setParameterRanges r_s0=0.7,1.3:r_s1=0.7,1.3:r_s2=0.7,1.3:r_s3=0.7,1.3:r_s4=0.7,1.3:r_s5=0.7,1.3
#combine -M MultiDimFit workspace_zxx.root -n zxx_r_s5 --algo=grid --robustFit=1 --points=600 -P r_s5 --floatOtherPOIs=1 --setParameterRanges r_s0=0.7,1.3:r_s1=0.7,1.3:r_s2=0.7,1.3:r_s3=0.7,1.3:r_s4=0.7,1.3:r_s5=0.7,1.3
#combine -M MultiDimFit workspace_zxx.root -n zxx_r_s0_statonly --algo=grid --robustFit=1 --points=600 -P r_s0 --floatOtherPOIs=1 --setParameterRanges r_s0=0.7,1.3:r_s1=0.7,1.3:r_s2=0.7,1.3:r_s3=0.7,1.3:r_s4=0.7,1.3:r_s5=0.7,1.3 --fastScan
#combine -M MultiDimFit workspace_zxx.root -n zxx_r_s1_statonly --algo=grid --robustFit=1 --points=600 -P r_s1 --floatOtherPOIs=1 --setParameterRanges r_s0=0.7,1.3:r_s1=0.7,1.3:r_s2=0.7,1.3:r_s3=0.7,1.3:r_s4=0.7,1.3:r_s5=0.7,1.3 --fastScan
#combine -M MultiDimFit workspace_zxx.root -n zxx_r_s2_statonly --algo=grid --robustFit=1 --points=600 -P r_s2 --floatOtherPOIs=1 --setParameterRanges r_s0=0.7,1.3:r_s1=0.7,1.3:r_s2=0.7,1.3:r_s3=0.7,1.3:r_s4=0.7,1.3:r_s5=0.7,1.3 --fastScan
#combine -M MultiDimFit workspace_zxx.root -n zxx_r_s3_statonly --algo=grid --robustFit=1 --points=600 -P r_s3 --floatOtherPOIs=1 --setParameterRanges r_s0=0.7,1.3:r_s1=0.7,1.3:r_s2=0.7,1.3:r_s3=0.7,1.3:r_s4=0.7,1.3:r_s5=0.7,1.3 --fastScan
#combine -M MultiDimFit workspace_zxx.root -n zxx_r_s4_statonly --algo=grid --robustFit=1 --points=600 -P r_s4 --floatOtherPOIs=1 --setParameterRanges r_s0=0.7,1.3:r_s1=0.7,1.3:r_s2=0.7,1.3:r_s3=0.7,1.3:r_s4=0.7,1.3:r_s5=0.7,1.3 --fastScan
#combine -M MultiDimFit workspace_zxx.root -n zxx_r_s5_statonly --algo=grid --robustFit=1 --points=600 -P r_s5 --floatOtherPOIs=1 --setParameterRanges r_s0=0.7,1.3:r_s1=0.7,1.3:r_s2=0.7,1.3:r_s3=0.7,1.3:r_s4=0.7,1.3:r_s5=0.7,1.3 --fastScan

rm -f higgsCombine*.root;
rm -f combine_logger.out;
