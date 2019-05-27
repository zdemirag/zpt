#!/bin/sh

export PARAM="";

if [ $# != 2 ]; then
   echo "TOO FEW PARAMETERS"
   exit
fi

expDirName=""
if [ $2 = "exp" ]; then
  PARAM="--expectSignal=1 -t -1";
  expDirName="_exp"
fi

rm -rf impacts_$1${expDirName}
mkdir impacts_$1${expDirName}
cp inputs/$1.root impacts_$1${expDirName}/
cd impacts_$1${expDirName}/

combine -M MaxLikelihoodFit $1.root -n $1 --saveNorm --saveWithUncertainties --robustFit=1 --X-rtd FITTER_DYN_STEP $PARAM

combine -M MultiDimFit $1.root -n $1 --algo=singles --robustFit=1 --saveFitResult $PARAM

combineTool.py -M Impacts -d $1.root -m 125 -n $1 --robustFit 1 --doInitialFit --allPars $PARAM;
combineTool.py -M Impacts -d $1.root -m 125 -n $1 --robustFit 1 --doFits --allPars $PARAM;
combineTool.py -M Impacts -d $1.root -m 125 -n $1 -o impacts_$1.json --allPars $PARAM;
plotImpacts.py -i impacts_$1.json -o impacts_$1;

rm -f combine_logger.out;

#root -l multidimfittest_ww_dphill.root
#fit_mdf->correlationHist()->Draw("colz")
