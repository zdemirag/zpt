#! /usr/bin/env python                                                                                                                                                              
from ROOT import *
from array import array
from tdrStyle import *
import math
from pretty import plot_ratio
setTDRStyle()

ptbinslow  = [100,125,150,175,200,225,250]
ptbinshigh = [250,275,300,350,400,450,500,650,800,1150,1500,2000] 
#[ 250.0, 300.0, 350.0, 400.0, 500.0, 750.0, 1000.0, 1500.0]
ptbins = [100,125,150,175,200,225,250,275,300,350,400,450,500,650,800,1150,1500,2000] 
#250.0, 300.0, 350.0, 400.0, 500.0, 750.0, 1000.0, 1500.0]

#ptbins = [250,275,300,350,400,450,500,650,800,1150,1500,2000]

def abcd(filename,mc=True):

    infile = TFile("/desktop/05a/v_004_11jetht/"+filename+".root","read") 
        #"/eos/cms/store/group/phys_exotica/monojet/zdemirag/panda/monojet/v_004_11jetht/"+filename+".root","read")
    intree = infile.Get("events")

    #high dphi   c        d
    #low  dphi   a        b
    #            low met  high met

    common = "(fabs(jot1Eta)<=2.4 && metFilter==1 && jot1Pt>100 && fabs(jot1Eta)<2.4 && jet1IsTight==1 && nTau==0 && jetNMBtags==0 && nLooseLep==0 && nLoosePhoton==0 && fabs(calomet-pfmet)/pfmet<0.5"
    #fabs(jot1Eta)<=2.4

    if filename is "JetHT":
        print "analyzing JetHT dataset therefore, the HT 900 requirement is added:"
        common = "(metFilter==1 && jet1Pt>100 && fabs(jet1Eta)<2.4 && jet1IsTight==1 && nTau==0 && jetNMBtags==0 && nLooseLep==0 && nLoosePhoton==0 && fabs(calomet-pfmet)/pfmet<0.5 && barrelHT>1000 && (trigger&16)!=0"
        #common = "(metFilter==1 && jet1Pt>100 && fabs(jet1Eta)<2.4 && jet1IsTight==1 && nTau==0 && jetNMBtags==0 && nLooseLep==0 && nLoosePhoton==0 && fabs(calomet-pfmet)/pfmet<0.5 && (trigger&16)!=0"

    if mc:
        common_weights = "*(sf_pu*normalizedWeight*sf_ewkV*sf_qcdV)"
    else:
        common_weights = "*(1.0)"

    selection_a = common + " && pfmet<=250 && dphipfmet<=0.5 )" 
    selection_b = common + " && pfmet>250  && dphipfmet<=0.5 )"
    selection_c = common + " && pfmet<=250 && dphipfmet>0.5 )"
    selection_d = common + " && pfmet>250  && dphipfmet>0.5 )"
    selection_inclow  = common + "&& pfmet>50  && dphipfmet<=0.5 )"
    selection_inchigh = common + "&& pfmet>50  && dphipfmet>0.5 )"

    h2d = TH2D("h2d"+filename,"h2d"+filename,100,0,2000,100,0,3.5)

    #ha = TH1D("ha"+filename,"ha"+filename,100,0,2000)
    #ha.Sumw2()
    #hb = TH1D("hb"+filename,"hb"+filename,100,0,2000)
    #hb.Sumw2()
    #hc = TH1D("hc"+filename,"hc"+filename,100,0,2000)
    #hc.Sumw2()
    #hd = TH1D("hd"+filename,"hd"+filename,100,0,2000)
    #hd.Sumw2()

    ha = TH1D("ha"+filename,"ha"+filename,len(ptbinslow)-1,array('d',ptbinslow))
    ha.Sumw2()
    hb = TH1D("hb"+filename,"hb"+filename,len(ptbinshigh)-1,array('d',ptbinshigh))
    hb.Sumw2()
    hc = TH1D("hc"+filename,"hc"+filename,len(ptbinslow)-1,array('d',ptbinslow))
    hc.Sumw2()
    hd = TH1D("hd"+filename,"hd"+filename,len(ptbinshigh)-1,array('d',ptbinshigh))
    hd.Sumw2()

    hinc_high = TH1D("hinc_high"+filename,"hinc_high"+filename,len(ptbins)-1,array('d',ptbins))
    hinc_high.Sumw2()

    hinc_low = TH1D("hinc_low"+filename,"hinc_low"+filename,len(ptbins)-1,array('d',ptbins))
    hinc_low.Sumw2()

    print "Plotting the pfmet distirbution for a,b,c,d selections for sample", filename

    intree.Draw("pfmet>>ha"+filename,selection_a+common_weights,"goff")
    intree.Draw("pfmet>>hb"+filename,selection_b+common_weights,"goff")
    intree.Draw("pfmet>>hc"+filename,selection_c+common_weights,"goff")
    intree.Draw("pfmet>>hd"+filename,selection_d+common_weights,"goff")

    intree.Draw("pfmet>>hinc_high"+filename,selection_inchigh+common_weights,"goff")
    intree.Draw("pfmet>>hinc_low"+filename,selection_inclow+common_weights,"goff")

    print "Selection A", selection_a, "integral", ha.Integral()
    print "Selection B", selection_b, "integral", hb.Integral()
    print "Selection C", selection_c, "integral", hc.Integral()
    print "Selection D", selection_d, "integral", hd.Integral()

    intree.Draw("dphipfmet:pfmet>>h2d"+filename,common+")"+common_weights,"goff")

    ha.SetDirectory(0); hb.SetDirectory(0); hc.SetDirectory(0); hd.SetDirectory(0); h2d.SetDirectory(0); hinc_low.SetDirectory(0); hinc_high.SetDirectory(0)

    return ha, hb, hc, hd, h2d, hinc_low, hinc_high

def main():

    sample_list_mc   = ["QCD","WJets","ZtoNuNu"]
    #sample_list_data = ["MET","JetHT"]
    sample_list_data = ["MET"]

    #sample_list_mc   = ["QCD"]
    #sample_list_data = ["JetHT","MET"]

    sample_list = sample_list_mc + sample_list_data

    ha,hb,hc,hd,h2d,hinc_low,hinc_high={},{},{},{},{},{},{}

    for i in range(len(sample_list)):

        ha[i] = TH1D("ha"+sample_list[i],"ha"+sample_list[i],len(ptbinslow)-1,array('d',ptbinslow))
        ha[i].Sumw2()
        hb[i] = TH1D("hb"+sample_list[i],"hb"+sample_list[i],len(ptbinshigh)-1,array('d',ptbinshigh))
        hb[i].Sumw2()
        hc[i] = TH1D("hc"+sample_list[i],"hc"+sample_list[i],len(ptbinslow)-1,array('d',ptbinslow))
        hc[i].Sumw2()
        hd[i] = TH1D("hd"+sample_list[i],"hd"+sample_list[i],len(ptbinshigh)-1,array('d',ptbinshigh))
        hd[i].Sumw2()
        hinc_low[i] = TH1D("hinc_low"+sample_list[i],"hinc_low"+sample_list[i],len(ptbins)-1,array('d',ptbins))
        hinc_low[i].Sumw2()
        hinc_high[i] = TH1D("hinc_high"+sample_list[i],"hinc_high"+sample_list[i],len(ptbins)-1,array('d',ptbins))
        hinc_high[i].Sumw2()

        h2d[i] = TH2D("h2d"+sample_list[i],"h2d"+sample_list[i],100,0,2000,100,0,3.5)

        if sample_list[i] in sample_list_mc:
            print "Calling the abcd function for sample", sample_list[i], "setting the weights True"
            ha[i],hb[i],hc[i],hd[i], h2d[i], hinc_low[i], hinc_high[i] = abcd(sample_list[i],True)
        else:
            print "Calling the abcd function for sample", sample_list[i], "setting the weights False"
            ha[i],hb[i],hc[i],hd[i], h2d[i], hinc_low[i], hinc_high[i]  = abcd(sample_list[i],False)
            
    # save a,b,c,d and the stack plots
    # set up the output root file to include all zvv, wlv, qcd and jetht
    outfile = TFile("qcd_abcd.root","recreate")

    outfile.cd()    
    for i in range(len(sample_list)):
        ha[i].Write()
        hb[i].Write()
        hc[i].Write()
        hd[i].Write()
        h2d[i].Write()
        hinc_low[i].Write()
        hinc_high[i].Write()

    outfile.Write()
    outfile.Close()

    
main()
