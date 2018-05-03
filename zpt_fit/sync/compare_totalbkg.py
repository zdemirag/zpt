import ROOT

ROOT.gSystem.Load("libRooFit.so")
ROOT.gSystem.Load("libRooFitCore.so")
ROOT.gROOT.SetStyle("Plain")
ROOT.gSystem.SetIncludePath( "-I$ROOFITSYS/include/" )

from pretty import plot_ratio
from tdrStyle import *
setTDRStyle()

def makehistogram(filename,directory,process):

    f_data = ROOT.TFile(filename,"READ")
    h      = f_data.Get(directory+"/"+process)
    h.SetDirectory(0)
    h.Scale(1,"width")
    print "The integral for", filename, h.Integral()
    return h

def main():

    process_mit  = ["Wen_data","Wen_wjets","Wmn_data","Wmn_wjets","signal_data","signal_zjets","signal_wjets"]
    filefolder = "/home/zdemirag/cms_2017/zpt/CMSSW_8_1_0/src/analysis/zpt_fit/"

    for proc in range(0,len(process_mit)):    
        h1 = makehistogram(filefolder+"mono-x.root"      ,"category_monojet",process_mit[proc])
        h2 = makehistogram(filefolder+"mono-x_sync.root" ,"category_monojet",process_mit[proc])  

        c = ROOT.TCanvas("c","c",600,700)
        #c.SetLogy()
        c.SetBottomMargin(0.3)
        c.SetRightMargin(0.06)
        c.SetTitle("")
        c.cd()

        h1.SetLineColor(1)
        h1_clone = h1.Clone()
                                 
        h1.GetYaxis().SetTitle("Events")
        h1.GetXaxis().SetTitle("")
        h1.GetXaxis().SetTitleOffset(1.15)
        h1.GetXaxis().SetTitleSize(0)
        h1.GetXaxis().SetLabelSize(0)
        h1.Draw("hist")
        h2.SetLineColor(2)
        h2.SetLineWidth(2)
        h2.Draw("histsame")

            
        leg = ROOT.TLegend(.45,.7,.9,.9)
        leg.SetFillStyle(0)
        leg.SetBorderSize(0)
        leg.AddEntry(h1 ,"zeynep","l")
        leg.AddEntry(h2 ,"sid","l")
        
        leg.Draw("same")
            
        Pad = ROOT.TPad("pad", "pad", 0.0, 0.0, 1.0, 0.9)
        Pad.SetTopMargin(0.7)
        Pad.SetRightMargin(0.06)
        Pad.SetFillColor(0)
        Pad.SetGridy(1)
        Pad.SetFillStyle(0)
        Pad.Draw()
        Pad.cd(0)
        
        
        ratio = plot_ratio(False,h1_clone,h2,"met","zeynep/sid",0.95,1.05,5)
        ratio.SetLineColor(2)
        ratio.SetMarkerColor(2)
        ratio.GetXaxis().SetTitle("met [GeV]")
        ratio.SetMarkerStyle(20)
        ratio.Draw("ep")
                    
    
        c.SaveAs("/afs/cern.ch/user/z/zdemirag/www/zpt/panda/sync/bkg_"+process_mit[proc]+".pdf")
        c.SaveAs("/afs/cern.ch/user/z/zdemirag/www/zpt/panda/sync/bkg_"+process_mit[proc]+".png")
        c.SaveAs("/afs/cern.ch/user/z/zdemirag/www/zpt/panda/sync/bkg_"+process_mit[proc]+".C")
                
main()
