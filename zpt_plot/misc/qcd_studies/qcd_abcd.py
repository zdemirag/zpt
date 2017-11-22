#! /usr/bin/env python                                                                                                                                                              
from ROOT import *
from array import array
from tdrStyle import *
import math
from pretty import plot_ratio
setTDRStyle()

def abcd(filename,mc=True):

    infile = TFile("/eos/cms/store/group/phys_exotica/monojet/zdemirag/panda/monojet/v_004_11jetht/"+filename+".root","read")
    intree = infile.Get("events")

    #high dphi   c        d
    #low  dphi   a        b
    #            low met  high met

    common = "metFilter==1 && jet1Pt>100 && fabs(jet1Eta)<2.4 && jet1IsTight==1 && nTau==0 && jetNMBtags==0 && nLooseLep==0 && nLoosePhoton==0 && fabs(calomet-pfmet)/pfmet<0.5"

    if mc:
        common_weights = "*sf_pu*normalizedWeight*sf_ewkV*sf_qcdV"
    else:
        common_weights = "*(1.0)"

    selection_a = common + " && pfmet>50   && dphipfmet<0.5 " 
    selection_b = common + " && pfmet>250  && dphipfmet<0.5 "
    selection_c = common + " && pfmet>50   && dphipfmet>0.5 "
    selection_d = common + " && pfmet>250  && dphipfmet>0.5 "

    ha = TH1D("ha","ha",100,0,2000)
    ha.Sumw2()
    hb = TH1D("hb","hb",100,0,2000)
    hb.Sumw2()
    hc = TH1D("hc","hc",100,0,2000)
    hc.Sumw2()
    hd = TH1D("hd","hd",100,0,2000)
    hd.Sumw2()

    print "Plotting the pfmet distirbution for a,b,c,d selections for sample", filename

    intree.Draw("pfmet>>ha",selection_a+common_weights,"goff")
    intree.Draw("pfmet>>hb",selection_b+common_weights,"goff")
    intree.Draw("pfmet>>hc",selection_c+common_weights,"goff")
    intree.Draw("pfmet>>hd",selection_d+common_weights,"goff")

    return ha,hb,hc,hd

def main():

    # set up the output root file to include all zvv, wlv, qcd and jetht
    outfile = TFile("qcd_abcd.root","recreate")
    
    sample_list_mc   = ["QCD","WJets","ZtoNuNu"]
    sample_list_data = ["MET","JetHT"]

    ha,hb,hc,hd={},{},{},{}

    for i in range(len(sample_list_mc)):

        ha[i] = TH1D("ha"+sample_list_mc[i],"ha"+sample_list_mc[i],100,0,2000)
        ha[i].Sumw2()
        hb[i] = TH1D("hb"+sample_list_mc[i],"hb"+sample_list_mc[i],100,0,2000)
        hb[i].Sumw2()
        hc[i] = TH1D("hc"+sample_list_mc[i],"hc"+sample_list_mc[i],100,0,2000)
        hc[i].Sumw2()
        hd[i] = TH1D("hd"+sample_list_mc[i],"hd"+sample_list_mc[i],100,0,2000)
        hd[i].Sumw2()

        print "Calling the abcd function for sample", sample_list_mc[i]
        ha[i],hb[i],hc[i],hd[i] = abcd(sample_list_mc[i],True)

    # save a,b,c,d and the stack plots

    outfile.cd()    
    for i in range(len(sample_list_mc)):
        ha[i].Write()
        hb[i].Write()
        hc[i].Write()
        hd[i].Write()

    outfile.Write()
    outfile.Close()

    
main()
