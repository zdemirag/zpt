The creation of this folder dates October 8 2018. The goal is to study the latest cobmination of Zvv and Zll analysis. 

Guillelmo created the workspaces:

text2workspace.py -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel --PO verbose  \
--PO 'map=.*/NonFid:r_s0[1,0,10]'  \
--PO 'map=.*/DY_0:r_s1[1,0,10]'  \
--PO 'map=.*/DY_1:r_s2[1,0,10]'  \
--PO 'map=.*/DY_2:r_s3[1,0,10]'  \
--PO 'map=.*/DY_3:r_s4[1,0,10]'  \
--PO 'map=.*/DY_4:r_s5[1,0,10]'  \
--PO 'map=.*/zcat0:r_s6[1,0,10]'  \
--PO 'map=.*/zcat1:r_s1[1,0,10]'  \
--PO 'map=.*/zcat2:r_s2[1,0,10]'  \
--PO 'map=.*/zcat3:r_s3[1,0,10]'  \
--PO 'map=.*/zcat4:r_s4[1,0,10]'  \
--PO 'map=.*/zcat5:r_s5[1,0,10]'  \
datacard_zxx.text -o workspace_zxx.root;

text2workspace.py -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel --PO verbose  \
--PO 'map=.*/NonFid:r_s1[1,0,10]'  \
--PO 'map=.*/DY_0:r_s0[1,0,10]'  \
--PO 'map=.*/DY_1:r_s0[1,0,10]'  \
--PO 'map=.*/DY_2:r_s0[1,0,10]'  \
--PO 'map=.*/DY_3:r_s0[1,0,10]'  \
--PO 'map=.*/DY_4:r_s0[1,0,10]'  \
--PO 'map=.*/zcat0:r_s2[1,0,10]'  \
--PO 'map=.*/zcat1:r_s0[1,0,10]'  \
--PO 'map=.*/zcat2:r_s0[1,0,10]'  \
--PO 'map=.*/zcat3:r_s0[1,0,10]'  \
--PO 'map=.*/zcat4:r_s0[1,0,10]'  \
--PO 'map=.*/zcat5:r_s0[1,0,10]'  \
datacard_zxx.text -o workspace_zxx_total.root;

