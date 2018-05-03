#! /usr/bin/env python                                                                                                                                                           
from ROOT import *
from array import array
from tdrStyle import *
import math
from pretty import plot_ratio
setTDRStyle()

infile = TFile("qcd_abcd_Down.root","read")

def ratio(model):

    ha = infile.Get("ha"+model)
    hb = infile.Get("hb"+model)
    hc = infile.Get("hc"+model)
    hd = infile.Get("hd"+model)

    hinc_low = infile.Get("hinc_low"+model)
    hinc_high = infile.Get("hinc_high"+model)
    
    inc_fit = hinc_high.Clone()
    inc_fit.Divide(hinc_low)

    fitregion = hc.Clone()
    fitregion.Divide(ha)

    closureregion = hd.Clone()
    closureregion.Divide(hb)

    c = TCanvas("c","c",700,700)
    if model is "QCD":
        frame = c.DrawFrame(100,1e-4,1500,1e4);
    else:
        frame = c.DrawFrame(100,1e-1,1500,1e8);
    c.SetLogy()

    frame.GetXaxis().SetTitle("p_{T}^{miss} [GeV]")
    frame.GetYaxis().SetTitle("Events")
    frame.GetXaxis().SetTitleOffset(1.15)
    frame.GetXaxis().SetTitleSize(0.05)
    frame.GetXaxis().SetLabelSize(0.04)
    ha.Draw("HISTSAME")
    hb.SetLineColor(2)
    hb.Draw("HISTSAME")
    hc.SetLineColor(4)
    hc.Draw("HISTSAME")
    hd.SetLineColor(8)
    hd.Draw("HISTSAME")

    c.Update()
    
    leg = TLegend(.55,.7,.9,.9)                                                                                                                                                     
    leg.SetFillStyle(0)                                                                                                                                                             
    leg.SetBorderSize(0)                                                                                                                                                            
    leg.AddEntry(ha ,"Region A","l")                                                                                                                                     
    leg.AddEntry(hb ,"Region B","l")                                                                                                                                     
    leg.AddEntry(hc ,"Region C","l")                                                                                                                                     
    leg.AddEntry(hd ,"Region D","l")                                                                                                                                     
    leg.Draw("same")
    
    c.SaveAs("/afs/cern.ch/user/z/zdemirag/www/zpt/panda/qcd/Down/all_"+model+".pdf")
    c.SaveAs("/afs/cern.ch/user/z/zdemirag/www/zpt/panda/qcd/Down/all_"+model+".png")
    c.SaveAs("/afs/cern.ch/user/z/zdemirag/www/zpt/panda/qcd/Down/all_"+model+".C")
    
    return fitregion, closureregion, hb, hd, hinc_low, hinc_high, inc_fit


def main(model):
    
    fitregion, closureregion, control, signal, hinc_low, hinc_high, inc_fit = ratio(model)
    
    c1 = TCanvas("c1","c1",700,700)
    c1.cd()
    fitregion.GetYaxis().SetTitle("Ratio")
    fitregion.GetXaxis().SetTitle("p_{T}^{miss} [GeV]")
    fitregion.GetXaxis().SetTitleOffset(1.15)
    fitregion.GetXaxis().SetTitleSize(0.05)
    fitregion.GetXaxis().SetLabelSize(0.04)
    c1.SetLogy()
    fitregion.SetMarkerStyle(20)

    fitregion.Draw("HIST")
    fitregion.Draw()

    fitregion.Fit("expo")

    c1.SaveAs("/afs/cern.ch/user/z/zdemirag/www/zpt/panda/qcd/Down/fitregion_"+model+".png")
    c1.SaveAs("/afs/cern.ch/user/z/zdemirag/www/zpt/panda/qcd/Down/fitregion_"+model+".pdf")
    c1.SaveAs("/afs/cern.ch/user/z/zdemirag/www/zpt/panda/qcd/Down/fitregion_"+model+".C")


    c2 = TCanvas("c2","c2",700,700)
    c2.cd()
    closureregion.GetYaxis().SetTitle("Ratio")
    closureregion.GetXaxis().SetTitle("p_{T}^{miss} [GeV]")
    closureregion.GetXaxis().SetTitleOffset(1.15)
    closureregion.GetXaxis().SetTitleSize(0.05)
    closureregion.GetXaxis().SetLabelSize(0.04)
    c2.SetLogy()
    closureregion.SetMarkerStyle(20)

    closureregion.Draw("HIST")
    closureregion.Draw()

    c2.SaveAs("/afs/cern.ch/user/z/zdemirag/www/zpt/panda/qcd/Down/closureregion_"+model+".png")
    c2.SaveAs("/afs/cern.ch/user/z/zdemirag/www/zpt/panda/qcd/Down/closureregion_"+model+".pdf")
    c2.SaveAs("/afs/cern.ch/user/z/zdemirag/www/zpt/panda/qcd/Down/closureregion_"+model+".C")

    c3 = TCanvas("c3","c3",700,700)
    c3.cd()
    inc_fit.GetYaxis().SetTitle("Ratio")
    inc_fit.GetXaxis().SetTitle("p_{T}^{miss} [GeV]")
    inc_fit.GetXaxis().SetTitleOffset(1.15)
    inc_fit.GetXaxis().SetTitleSize(0.05)
    inc_fit.GetXaxis().SetLabelSize(0.04)
    c3.SetLogy()
    inc_fit.SetMarkerStyle(20)

    inc_fit.Draw("HIST")
    inc_fit.Draw()

    #func = TF1("func","exp([0]+[1]*x) + exp([2]+[3]*x)")
    func = TF1("func","exp([0]+([1]*exp([2]+[3]*x)))+[4]")
    func.SetParName(0,"constant 1")
    func.SetParName(1,"slope 1")
    func.SetParName(2,"constant 2")
    func.SetParName(3,"slope 2")
    func.SetParName(4,"platau")

    #func.SetParameter(0,-2)
    #func.SetParameter(1,0.01)
    #func.SetParameter(0,-6)
    #func.SetParameter(1,0.04)

    func.SetParameter(0,-20)
    func.SetParameter(1,2)
    func.SetParameter(2,2)
    func.SetParameter(3,-0.001)
    func.SetParameter(4,0.005)

    inc_fit.Fit(func)

    c3.SaveAs("/afs/cern.ch/user/z/zdemirag/www/zpt/panda/qcd/Down/inc_fit_"+model+".png")
    c3.SaveAs("/afs/cern.ch/user/z/zdemirag/www/zpt/panda/qcd/Down/inc_fit_"+model+".pdf")
    c3.SaveAs("/afs/cern.ch/user/z/zdemirag/www/zpt/panda/qcd/Down/inc_fit_"+model+".C")

main("QCD")
main("JetHT")
main("MET")
