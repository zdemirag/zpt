#!/bin/sh

cp datacard_zmm.text datacard_zmm_normalized0.text
cp datacard_zmm.text datacard_zmm_normalized1.text
cp datacard_zee.text datacard_zee_normalized0.text
cp datacard_zee.text datacard_zee_normalized1.text
cp datacard_znn.text datacard_znn_normalized0.text
cp datacard_znn.text datacard_znn_normalized1.text

root -l -q -b ../makeZllParam.C'("mm",1)'|tail -9 >> datacard_zmm_normalized0.text
root -l -q -b ../makeZllParam.C'("mm",2)'|tail -9 >> datacard_zmm_normalized1.text
root -l -q -b ../makeZllParam.C'("ee",1)'|tail -9 >> datacard_zee_normalized0.text
root -l -q -b ../makeZllParam.C'("ee",2)'|tail -9 >> datacard_zee_normalized1.text
root -l -q -b makeZnnParam.C'(1)'     |tail -9 >> datacard_znn_normalized0.text
root -l -q -b makeZnnParam.C'(2)'     |tail -9 >> datacard_znn_normalized1.text

combineCards.py zee=datacard_zee_normalized0.text zmm=datacard_zmm_normalized0.text > datacard_zll_normalized0.text
combineCards.py zee=datacard_zee_normalized1.text zmm=datacard_zmm_normalized1.text > datacard_zll_normalized1.text
combineCards.py zee=datacard_zee_normalized0.text zmm=datacard_zmm_normalized0.text znn=datacard_znn_normalized0.text > datacard_zxx_normalized0.text
combineCards.py zee=datacard_zee_normalized1.text zmm=datacard_zmm_normalized1.text znn=datacard_znn_normalized1.text > datacard_zxx_normalized1.text

text2workspace.py -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel --PO verbose  \
--PO 'map=.*/NonFid:r_s1[1,0,10]'  \
--PO 'map=.*/DY_0:r_s0[1,0,10]'  \
--PO 'map=.*/DY_1:r_s0[1,0,10]'  \
--PO 'map=.*/DY_2:r_s0[1,0,10]'  \
--PO 'map=.*/DY_3:r_s0[1,0,10]'  \
--PO 'map=.*/DY_4:r_s0[1,0,10]'  \
datacard_zll_normalized0.text -o workspace_zll_normalized0.root;

text2workspace.py -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel --PO verbose  \
--PO 'map=.*/NonFid:r_s1[1,0,10]'  \
--PO 'map=.*/DY_0:r_s0[1,0,10]'  \
--PO 'map=.*/DY_1:r_s0[1,0,10]'  \
--PO 'map=.*/DY_2:r_s0[1,0,10]'  \
--PO 'map=.*/DY_3:r_s0[1,0,10]'  \
--PO 'map=.*/DY_4:r_s0[1,0,10]'  \
datacard_zll_normalized1.text -o workspace_zll_normalized1.root;

text2workspace.py -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel --PO verbose  \
--PO 'map=.*/zcat0:r_s1[1,0,10]'  \
--PO 'map=.*/zcat1:r_s0[1,0,10]'  \
--PO 'map=.*/zcat2:r_s0[1,0,10]'  \
--PO 'map=.*/zcat3:r_s0[1,0,10]'  \
--PO 'map=.*/zcat4:r_s0[1,0,10]'  \
--PO 'map=.*/zcat5:r_s0[1,0,10]'  \
datacard_znn_normalized0.text -o workspace_znn_normalized0.root;

text2workspace.py -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel --PO verbose  \
--PO 'map=.*/zcat0:r_s0[1,0,10]'  \
--PO 'map=.*/zcat1:r_s0[1,0,10]'  \
--PO 'map=.*/zcat2:r_s0[1,0,10]'  \
--PO 'map=.*/zcat3:r_s0[1,0,10]'  \
--PO 'map=.*/zcat4:r_s0[1,0,10]'  \
--PO 'map=.*/zcat5:r_s0[1,0,10]'  \
datacard_znn_normalized0_nonfidicual.text -o workspace_znn_normalized0_nonfidicual.root;

text2workspace.py -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel --PO verbose  \
--PO 'map=.*/zcat0:r_s1[1,0,10]'  \
--PO 'map=.*/zcat1:r_s0[1,0,10]'  \
--PO 'map=.*/zcat2:r_s0[1,0,10]'  \
--PO 'map=.*/zcat3:r_s0[1,0,10]'  \
--PO 'map=.*/zcat4:r_s0[1,0,10]'  \
--PO 'map=.*/zcat5:r_s0[1,0,10]'  \
datacard_znn_normalized1.text -o workspace_znn_normalized1.root;

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
datacard_zxx_normalized0.text -o workspace_zxx_normalized0.root;

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
datacard_zxx_normalized1.text -o workspace_zxx_normalized1.root;
