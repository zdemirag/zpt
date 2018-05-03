from ROOT import *
from array import array
from tdrStyle import *
setTDRStyle()

import math

def plot_ratio(process,category):

    highest = {}
    highest2 = {}
    lowest = {}

    f = TFile('../v6/combined_model.root','READ')
        
    if (process=='wen'):
        dirname = "W_constraints_category_"+category 
        base    = "wen_weights_"+category
        label   = "R_{W(e#nu)}"
        addsys  = 0.01
        
    if (process=='wmn'):
        dirname = "W_constraints_category_"+category 
        base    = "wmn_weights_"+category
        label   = "R_{W(#mu#nu)}"
        addsys  = 0.01
        

    ratio = f.Get(dirname+"/"+base)
    up_final = ratio.Clone("ratio")
    up_ewk = ratio.Clone("ratio")
    down_final = ratio.Clone("ratio")

    for b in range(ratio.GetNbinsX()+1):
        up_final.SetBinContent(b,0.0)
        up_ewk.SetBinContent(b,0.0)
        down_final.SetBinContent(b,0.0)
        highest[b] = 0
        highest2[b] = 0
        lowest [b] = 100.0

    f.cd(dirname)
    for key in gDirectory.GetListOfKeys():
        if (key.GetClassName(),"TH1"):
            if process in key.GetName():
                if ('Up' in key.GetName()):
                    up = f.Get(dirname+"/"+key.GetName())
                    print key.GetName()
                    for b in range(ratio.GetNbinsX()+1):
                        diff = up.GetBinContent(b) - ratio.GetBinContent(b)
                        highest[b] =  math.sqrt(highest[b]**2 + diff**2)
                        up_final.SetBinContent(b,highest[b])
                if ('Down' in key.GetName()):
                    down = f.Get(dirname+"/"+key.GetName())
                    print key.GetName()
                    for b in range(ratio.GetNbinsX()+1):
                        if down.GetBinContent(b) < lowest[b]:
                            lowest[b] = down.GetBinContent(b)
                        else:
                            lowest[b] = lowest[b]
                        down_final.SetBinContent(b,lowest[b])
              
    gStyle.SetOptStat(0)

    c = TCanvas("c","c",600,600)  
    c.SetTopMargin(0.06)
    c.cd()
    c.SetRightMargin(0.04)
    c.SetTopMargin(0.07)
    c.SetLeftMargin(0.12)


    uncertband    = ratio.Clone("ratio")
    uncertband2   = ratio.Clone("ratio2")
    uncertband3   = ratio.Clone("ratio3")
    for b in range(ratio.GetNbinsX()+1):
        #err1 = abs(down_final.GetBinContent(b) -  ratio.GetBinContent(b))
        err1 = abs(up_final.GetBinContent(b) -  ratio.GetBinContent(b))
        #uncertband.SetBinError(b,max(err1,err2))
        #uncertband.SetBinError(b,err1)
        #print up_final.GetBinContent(b), addsys
        #uncertband.SetBinError(b,up_final.GetBinContent(b) + addsys*uncertband.GetBinContent(b))
        uncertband.SetBinError(b,up_final.GetBinContent(b))
        uncertband2.SetBinError(b,up_ewk.GetBinContent(b))
        uncertband3.SetBinError(b,up_final.GetBinContent(b) + addsys*uncertband.GetBinContent(b))

        #HACK
        #if b == ratio.GetNbinsX():
        #    uncertband.SetBinError(b,up_final.GetBinContent(b-1) + addsys)
        #    uncertband2.SetBinError(b,up_ewk.GetBinContent(b-1))

        #print "Uncert",b,ratio.GetBinContent(b),down_final.GetBinContent(b),up_final.GetBinContent(b), max(err1,err2)

    #uncertband.SetFillStyle(3144);
    #uncertband.SetFillColor(33);

    uncertband2.SetFillColor(33);
    uncertband3.SetFillColor(ROOT.kBlue+1);
    uncertband.SetFillColor(33);

    uncertband3.GetYaxis().SetTitle(label)
    uncertband3.GetYaxis().CenterTitle()
    uncertband3.GetYaxis().SetTitleSize(0.4*c.GetLeftMargin())
    uncertband3.GetXaxis().SetTitle("Hadronic recoil p_{T} [GeV]")
    uncertband3.GetXaxis().SetTitleSize(0.4*c.GetBottomMargin())
    #uncertband3.SetMaximum(2.0*ratio.GetMaximum())
    uncertband3.SetMinimum(0.5*ratio.GetMinimum())
    uncertband3.GetYaxis().SetTitleOffset(1.15)

    ratio.SetMarkerStyle(20)
    ratio.SetLineColor(1)
    ratio.SetLineWidth(2)

    uncertband3.Draw("e2")    
    ratio.Draw("same")

    legend = TLegend(.45,.75,.82,.92)
    legend.AddEntry(ratio,"Transfer Factor (Stat Uncert)" , "p")
    uncertband3.SetFillColor(33)
    legend.AddEntry(uncertband3 ,"Stat + Syst. (Exp)" , "f")
                
    legend.SetShadowColor(0);
    legend.SetFillColor(0);
    legend.SetLineColor(0);

    legend.Draw("same")

    latex2 = TLatex()
    latex2.SetNDC()
    latex2.SetTextSize(0.035)
    latex2.SetTextAlign(31) # align right
    latex2.DrawLatex(0.87, 0.95, "(13 TeV)");

    latex3 = TLatex()
    latex3.SetNDC()
    latex3.SetTextSize(0.75*c.GetTopMargin())
    latex3.SetTextFont(62)
    latex3.SetTextAlign(11) # align right
    latex3.DrawLatex(0.22, 0.85, "CMS");
    latex3.SetTextSize(0.5*c.GetTopMargin())
    latex3.SetTextFont(52)
    latex3.SetTextAlign(11)
    latex3.DrawLatex(0.20, 0.8, "Preliminary");
    
    gPad.RedrawAxis()

    #folder = "/afs/cern.ch/user/z/zdemirag/www/Monojet/moriond_80x/unblinding/fits/"

    folder = '/afs/cern.ch/user/z/zdemirag/www/zpt/panda/v6'


    c.SaveAs(folder+"/rfactor_"+category+"_"+process+".pdf")
    c.SaveAs(folder+"/rfactor_"+category+"_"+process+".png")
    c.SaveAs(folder+"/rfactor_"+category+"_"+process+".C")

    #c.SaveAs("rfactor_"+process+".root")

    #f_out = TFile(process+".root","recreate")
    #f_out.cd()
    #ratio.Write()
    #f_out.Close()

    del c
 
plot_ratio('wen','monojet')
plot_ratio('wmn','monojet')

