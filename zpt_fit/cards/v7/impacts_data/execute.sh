combine -M MultiDimFit -n _initialFit_Test --algo singles --redefineSignalPOIs r_zcat2,r_zcat3,r_zcat0,r_zcat1,r_zcat4,r_zcat5 --robustFit 1 -m 125 -d zpt_multidim.root  --expectSignal=1
combineTool.py -M Impacts -d zpt_multidim.root -m 125 --robustFit 1 --doFits --redefineSignalPOIs r_zcat2,r_zcat3,r_zcat0,r_zcat1,r_zcat4,r_zcat5  --expectSignal=1
combineTool.py -M Impacts -d zpt_multidim.root -m 125 -o impacts.json --redefineSignalPOIs r_zcat2,r_zcat3,r_zcat0,r_zcat1,r_zcat4,r_zcat5  --expectSignal=1
plotImpacts.py -i impacts.json -o impacts_rz2 --per-page 35
