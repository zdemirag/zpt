text2workspace.py -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel --PO verbose --PO 'map=.*/zcat0:r_zcat0[1,0,10]' --PO 'map=.*/zcat1:r_zcat1[1,0,10]' --PO 'map=.*/zcat2:r_zcat2[1,0,10]' --PO 'map=.*/zcat3:r_zcat3[1,0,10]' --PO 'map=.*/zcat4:r_zcat4[1,0,10]' zpt_card.txt -o zpt_multidim.root

combine -M MultiDimFit zpt_multidim.root --algo=singles --robustFit=1

combine -M FitDiagnostics zpt_multidim.root  --saveShapes --saveWithUncertainties
