combine -M MultiDimFit -n _initialFit_Test --algo singles --redefineSignalPOIs r_zcat0 --robustFit 1 -m 125 -d zpt_multidim_inclusive.root  --expectSignal=1
combineTool.py -M Impacts -d zpt_multidim_inclusive.root -m 125 --robustFit 1 --doFits --redefineSignalPOIs r_zcat0  --expectSignal=1
combineTool.py -M Impacts -d zpt_multidim_inclusive.root -m 125 -o impacts.json --redefineSignalPOIs r_zcat0  --expectSignal=1
plotImpacts.py -i impacts.json -o impacts_rz0 --per-page 35
