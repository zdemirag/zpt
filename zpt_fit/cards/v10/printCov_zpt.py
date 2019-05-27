from ROOT import *
from tdrStyle import setTDRStyle
setTDRStyle()

from array import array


for obs in ['r_z']:#['r_zcat0','r_zcat1','r_zcat2','r_zcat3','r_zcat4','r_zcat5']:
#for obs in ['pT4l','rapidity4l','njets_pt30_eta2p5','pt_leadingjet_pt30_eta2p5']:

  f = TFile("multidimfit.root","READ")

  r = f.Get("fit_mdf")

  h_obs = TH2D(obs,obs,6,0,6,6,0,6)  
  label = ["< 200","200 to 300","300 to 400","400 to 500","500 to 800",">= 800"]
  axisLabel="p_{T}^{miss} [GeV]"
  poi0 = RooRealVar("r_zcat0","r_zcat0",0,10)  
  poi1 = RooRealVar("r_zcat1","r_zcat1",0,10)  
  poi2 = RooRealVar("r_zcat2","r_zcat2",0,10)  
  poi3 = RooRealVar("r_zcat3","r_zcat3",0,10)  
  poi4 = RooRealVar("r_zcat4","r_zcat4",0,10)  
  poi5 = RooRealVar("r_zcat5","r_zcat5",0,10)  
  poi6 = RooRealVar("r_zcat6","r_zcat6",0,10)      
  pois = RooArgList(poi0,poi1,poi2,poi3,poi4,poi5,poi6)

  print r.covQual()
  cm = r.reducedCovarianceMatrix(pois)  
  cm.Print()
  
  for i in range(len(label)):
    #line = "r_zcat"+str(i)
    line = ""
    for j in range(len(label)):
      #if (i==(len(label)-1) or j==(len(label)-1)):
      #  line +=" "+str(round(r.correlation("r_zcat"+str(max(i-1,0)),"r_zcat"+str(max(j-1,0))),3))+";"
      #  h_obs.SetBinContent(i+1,j+1,r.correlation("r_zcat"+str(max(i-1,0)),"r_zcat"+str(max(j-1,0))))      
      #else:
      line +=" "+str(round(r.correlation("r_zcat"+str(i),"r_zcat"+str(j)),3))+";"
      h_obs.SetBinContent(i+1,j+1,r.correlation("r_zcat"+str(i),"r_zcat"+str(j)))
  
      if (i==0): h_obs.GetYaxis().SetBinLabel(j+1,label[j])
    h_obs.GetXaxis().SetBinLabel(i+1,label[i]+"         ")
      
    print line
  
  gStyle.SetPaintTextFormat("1.3f")
  gStyle.SetPalette(kTemperatureMap)
  
  c1 = TCanvas("c1","c1",1200,1000)
  c1.SetRightMargin(0.2)
  c1.SetLeftMargin(0.25)
  c1.SetBottomMargin(0.17)
  c1.cd()
  
  h_obs.GetXaxis().SetTitle(axisLabel)
  h_obs.GetYaxis().SetTitle(axisLabel)
  h_obs.GetXaxis().SetTitleOffset(1.2)
  h_obs.GetYaxis().SetTitleOffset(1.8)
  
  h_obs.GetZaxis().SetRangeUser(-1.0,1.0)
  
  h_obs.Draw("colztext")
  
  
  latex2 = TLatex()
  latex2.SetNDC()
  latex2.SetTextSize(0.4*c1.GetTopMargin())
  latex2.SetTextFont(42)
  latex2.SetTextAlign(31)
  latex2.DrawLatex(0.8, 0.94,"35.9 fb^{-1} (13 TeV)")
  latex2.SetTextAlign(11)
  latex2.SetTextSize(0.5*c1.GetTopMargin())
  latex2.SetTextFont(62)
  latex2.SetTextAlign(11)
  latex2.DrawLatex(0.25, 0.94, "CMS")
  latex2.SetTextSize(0.5*c1.GetTopMargin())
  latex2.SetTextFont(52)
  latex2.SetTextAlign(11)
  latex2.DrawLatex(0.32, 0.94, "Supplementary")
  
  c1.SaveAs("corrMatrix_"+obs+".pdf")
  c1.SaveAs("corrMatrix_"+obs+".png")
  
