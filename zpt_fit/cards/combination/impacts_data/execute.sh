combine -M MultiDimFit -n _initialFit_Test --algo singles --redefineSignalPOIs r_zcat2,r_zcat3,r_zcat0,r_zcat1,r_zcat4,r_zcat5 --robustFit 1 -m 125 -d zpt_combined_multidim.root  --expectSignal=1
mv higgsCombine_initialFit_Test.MultiDimFit.mH125.000000.root higgsCombine_initialFit_Test.MultiDimFit.mH125.root
combineTool.py -M Impacts -d zpt_combined_multidim.root -m 125 --robustFit 1 --doFits --redefineSignalPOIs r_zcat2,r_zcat3,r_zcat0,r_zcat1,r_zcat4,r_zcat5  --expectSignal=1
combineTool.py -M Impacts -d zpt_combined_multidim.root -m 125 -o impacts.json --redefineSignalPOIs r_zcat2,r_zcat3,r_zcat0,r_zcat1,r_zcat4,r_zcat5  --expectSignal=1

