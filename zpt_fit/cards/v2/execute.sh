text2workspace.py -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel --PO verbose --PO 'map=.*/zcat0:r_zcat0[1,0,10]'  --PO 'map=.*/zcat1:r_zcat1[1,0,10]' --PO 'map=.*/zcat2:r_zcat2[1,0,10]' --PO 'map=.*/zcat3:r_zcat3[1,0,10]' --PO 'map=.*/zcat4:r_zcat4[1,0,10]' --PO 'map=.*/zcat5:r_zcat5[1,0,10]' --PO 'map=.*/zcat6:r_zcat6[1,0,10]' zpt_card.txt -o zpt_multidim.root

combine -M MultiDimFit zpt_multidim.root --algo=singles --robustFit=1

combine zpt_multidim.root -M MaxLikelihoodFit --saveShapes --saveWithUncertainties > & log_maxlikelihood &


   62315:28emacs -nw execute.sh
   62415:28combine -M MultiDimFit zpt_multidim.root
   62515:29combine -M MultiDimFit zpt_multidim.root --algo=singles --robustFit=1
   62615:31combine -M MultiDimFit zpt_multidim.root -v 3
   62715:32combine -M MultiDimFit zpt_multidim.root --saveFitResult
   62915:33emacs -nw multidimfit.root
   63015:33root -l multidimfit.root
   63115:33combine -M MultiDimFit zpt_multidim.root --saveFitResult --saveShapes --saveWithUncertainties
   63215:33combine -M MultiDimFit zpt_multidim.root --saveFitResult --saveWithUncertainties
   63315:34combine -M MultiDimFit zpt_multidim.root --saveFitResult --saveWorkspace



   67218:59combineTool.py -M Impacts -d zpt_impacts.root -m 125 --doInitialFit --robustFit 1
   67318:59combineTool.py -M Impacts -d zpt_impacts.root -m 125 --robustFit 1 --doFits
   67419:02combineTool.py -M Impacts -d zpt_impacts.root -m 125 -o impacts.json
   67519:02plotImpacts.py -i impacts.json -o impacts
   67619:02evince impacts.pdf
