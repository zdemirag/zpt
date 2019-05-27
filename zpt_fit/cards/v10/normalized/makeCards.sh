#!/bin/sh

combineCards.py -S ../zll/datacard_Pt_mm.txt > datacard_zmm.text;
combineCards.py -S ../zll/datacard_Pt_ee.txt > datacard_zee.text;
combineCards.py -S ../zll/datacard_Pt_mm.txt ../zll/datacard_Pt_ee.txt > datacard_zll.text;

combineCards.py -S ../znn/zpt_card.txt        > datacard_znn.text;

combineCards.py -S datacard_zll.text datacard_znn.text > datacard_zxx.text;

text2workspace.py -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel --PO verbose  \
--PO 'map=.*/NonFid:r_s0[1,0,10]'  \
--PO 'map=.*/DY_0:r_s1[1,0,10]'  \
--PO 'map=.*/DY_1:r_s2[1,0,10]'  \
--PO 'map=.*/DY_2:r_s3[1,0,10]'  \
--PO 'map=.*/DY_3:r_s4[1,0,10]'  \
--PO 'map=.*/DY_4:r_s5[1,0,10]'  \
datacard_zmm.text -o workspace_zmm.root;

text2workspace.py -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel --PO verbose  \
--PO 'map=.*/NonFid:r_s0[1,0,10]'  \
--PO 'map=.*/DY_0:r_s1[1,0,10]'  \
--PO 'map=.*/DY_1:r_s2[1,0,10]'  \
--PO 'map=.*/DY_2:r_s3[1,0,10]'  \
--PO 'map=.*/DY_3:r_s4[1,0,10]'  \
--PO 'map=.*/DY_4:r_s5[1,0,10]'  \
datacard_zee.text -o workspace_zee.root;

text2workspace.py -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel --PO verbose  \
--PO 'map=.*/NonFid:r_s0[1,0,10]'  \
--PO 'map=.*/DY_0:r_s1[1,0,10]'  \
--PO 'map=.*/DY_1:r_s2[1,0,10]'  \
--PO 'map=.*/DY_2:r_s3[1,0,10]'  \
--PO 'map=.*/DY_3:r_s4[1,0,10]'  \
--PO 'map=.*/DY_4:r_s5[1,0,10]'  \
datacard_zll.text -o workspace_zll.root;

text2workspace.py -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel --PO verbose  \
--PO 'map=.*/NonFid:r_s1[1,0,10]'  \
--PO 'map=.*/DY_0:r_s0[1,0,10]'  \
--PO 'map=.*/DY_1:r_s0[1,0,10]'  \
--PO 'map=.*/DY_2:r_s0[1,0,10]'  \
--PO 'map=.*/DY_3:r_s0[1,0,10]'  \
--PO 'map=.*/DY_4:r_s0[1,0,10]'  \
datacard_zll.text -o workspace_zll_total.root;

text2workspace.py -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel --PO verbose  \
--PO 'map=.*/NonFid:r_s1[1,0,10]'  \
--PO 'map=.*/DY_0:r_s0[1,0,10]'  \
--PO 'map=.*/DY_1:r_s0[1,0,10]'  \
--PO 'map=.*/DY_2:r_s0[1,0,10]'  \
--PO 'map=.*/DY_3:r_s0[1,0,10]'  \
--PO 'map=.*/DY_4:r_s0[1,0,10]'  \
datacard_zmm.text -o workspace_zmm_total.root;

text2workspace.py -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel --PO verbose  \
--PO 'map=.*/NonFid:r_s1[1,0,10]'  \
--PO 'map=.*/DY_0:r_s0[1,0,10]'  \
--PO 'map=.*/DY_1:r_s0[1,0,10]'  \
--PO 'map=.*/DY_2:r_s0[1,0,10]'  \
--PO 'map=.*/DY_3:r_s0[1,0,10]'  \
--PO 'map=.*/DY_4:r_s0[1,0,10]'  \
datacard_zee.text -o workspace_zee_total.root;

text2workspace.py -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel --PO verbose  \
--PO 'map=.*/NonFid:r_s0[1,0,10]'  \
--PO 'map=.*/DY_0:r_s0[1,0,10]'  \
--PO 'map=.*/DY_1:r_s0[1,0,10]'  \
--PO 'map=.*/DY_2:r_s0[1,0,10]'  \
--PO 'map=.*/DY_3:r_s0[1,0,10]'  \
--PO 'map=.*/DY_4:r_s0[1,0,10]'  \
datacard_zll.text -o workspace_zll_total0.root;

text2workspace.py -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel --PO verbose  \
--PO 'map=.*/DY_0:r_s0[1,0,10]'  \
--PO 'map=.*/DY_1:r_s0[1,0,10]'  \
--PO 'map=.*/DY_2:r_s0[1,0,10]'  \
--PO 'map=.*/DY_3:r_s0[1,0,10]'  \
--PO 'map=.*/DY_4:r_s0[1,0,10]'  \
datacard_zll.text -o workspace_zll_total1.root;

text2workspace.py -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel --PO verbose \
--PO 'map=.*/zcat0:r_s0[1,0,10]' \
--PO 'map=.*/zcat1:r_s1[1,0,10]' \
--PO 'map=.*/zcat2:r_s2[1,0,10]' \
--PO 'map=.*/zcat3:r_s3[1,0,10]' \
--PO 'map=.*/zcat4:r_s4[1,0,10]' \
--PO 'map=.*/zcat5:r_s5[1,0,10]' \
datacard_znn.text -o workspace_znn.root;

text2workspace.py -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel --PO verbose \
--PO 'map=.*/zcat0:r_s1[1,0,10]' \
--PO 'map=.*/zcat1:r_s0[1,0,10]' \
--PO 'map=.*/zcat2:r_s0[1,0,10]' \
--PO 'map=.*/zcat3:r_s0[1,0,10]' \
--PO 'map=.*/zcat4:r_s0[1,0,10]' \
--PO 'map=.*/zcat5:r_s0[1,0,10]' \
datacard_znn.text -o workspace_znn_total.root;

text2workspace.py -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel --PO verbose \
--PO 'map=.*/zcat0:r_s0[1,0,10]' \
--PO 'map=.*/zcat1:r_s0[1,0,10]' \
--PO 'map=.*/zcat2:r_s0[1,0,10]' \
--PO 'map=.*/zcat3:r_s0[1,0,10]' \
--PO 'map=.*/zcat4:r_s0[1,0,10]' \
--PO 'map=.*/zcat5:r_s0[1,0,10]' \
datacard_znn.text -o workspace_znn_total0.root;

text2workspace.py -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel --PO verbose \
--PO 'map=.*/zcat1:r_s0[1,0,10]' \
--PO 'map=.*/zcat2:r_s0[1,0,10]' \
--PO 'map=.*/zcat3:r_s0[1,0,10]' \
--PO 'map=.*/zcat4:r_s0[1,0,10]' \
--PO 'map=.*/zcat5:r_s0[1,0,10]' \
datacard_znn.text -o workspace_znn_total1.root;

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

text2workspace.py -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel --PO verbose  \
--PO 'map=.*/NonFid:r_s0[1,0,10]'  \
--PO 'map=.*/DY_0:r_s0[1,0,10]'  \
--PO 'map=.*/DY_1:r_s0[1,0,10]'  \
--PO 'map=.*/DY_2:r_s0[1,0,10]'  \
--PO 'map=.*/DY_3:r_s0[1,0,10]'  \
--PO 'map=.*/DY_4:r_s0[1,0,10]'  \
--PO 'map=.*/zcat0:r_s0[1,0,10]'  \
--PO 'map=.*/zcat1:r_s0[1,0,10]'  \
--PO 'map=.*/zcat2:r_s0[1,0,10]'  \
--PO 'map=.*/zcat3:r_s0[1,0,10]'  \
--PO 'map=.*/zcat4:r_s0[1,0,10]'  \
--PO 'map=.*/zcat5:r_s0[1,0,10]'  \
datacard_zxx.text -o workspace_zxx_total0.root;

text2workspace.py -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel --PO verbose  \
--PO 'map=.*/DY_0:r_s0[1,0,10]'  \
--PO 'map=.*/DY_1:r_s0[1,0,10]'  \
--PO 'map=.*/DY_2:r_s0[1,0,10]'  \
--PO 'map=.*/DY_3:r_s0[1,0,10]'  \
--PO 'map=.*/DY_4:r_s0[1,0,10]'  \
--PO 'map=.*/zcat1:r_s0[1,0,10]'  \
--PO 'map=.*/zcat2:r_s0[1,0,10]'  \
--PO 'map=.*/zcat3:r_s0[1,0,10]'  \
--PO 'map=.*/zcat4:r_s0[1,0,10]'  \
--PO 'map=.*/zcat5:r_s0[1,0,10]'  \
datacard_zxx.text -o workspace_zxx_total1.root;
