from ROOT import *
from tdrStyle import setTDRStyle
setTDRStyle()

from array import array


for obs in ['pT4l','rapidity4l','njets_pt30_eta2p5','pt_leadingjet_pt30_eta2p5']:

  f = TFile("multidimfit"+obs+".root","READ")

  r = f.Get("fit_mdf")

  if (obs=='pT4l'):
    h_obs = TH2D(obs,obs,7,0,7,7,0,7)  
    label = ["0 to 15","15 to 30","30 to 45","45 to 80","80 to 120","120 to 200",">200"]
    axisLabel="p_{T}(H) (GeV)"
    poi0 = RooRealVar("SigmaBin0","SigmaBin0",0,10)  
    poi1 = RooRealVar("SigmaBin1","SigmaBin1",0,10)  
    poi2 = RooRealVar("SigmaBin2","SigmaBin2",0,10)  
    poi3 = RooRealVar("SigmaBin3","SigmaBin3",0,10)  
    poi4 = RooRealVar("SigmaBin4","SigmaBin4",0,10)  
    poi5 = RooRealVar("SigmaBin5","SigmaBin5",0,10)  
    poi6 = RooRealVar("SigmaBin6","SigmaBin6",0,10)      
    pois = RooArgList(poi0,poi1,poi2,poi3,poi4,poi5,poi6)

  if (obs=='rapidity4l'):
    h_obs = TH2D(obs,obs,6,0,6,6,0,6)  
    label = ["0.0 to 0.15","0.15 to 0.3","0.3 to 0.6","0.6 to 0.9","0.9 to 1.2","1.2 to 2.5"]
    axisLabel="y(H)"
    poi0 = RooRealVar("SigmaBin0","SigmaBin0",0,10)  
    poi1 = RooRealVar("SigmaBin1","SigmaBin1",0,10)  
    poi2 = RooRealVar("SigmaBin2","SigmaBin2",0,10)  
    poi3 = RooRealVar("SigmaBin3","SigmaBin3",0,10)  
    poi4 = RooRealVar("SigmaBin4","SigmaBin4",0,10)  
    poi5 = RooRealVar("SigmaBin5","SigmaBin5",0,10)  
    pois = RooArgList(poi0,poi1,poi2,poi3,poi4,poi5)
  
  if (obs=='njets_pt30_eta2p5'):
    h_obs = TH2D(obs,obs,5,0,5,5,0,5)  
    label = ["0","1","2","3","#geq 4"]
    axisLabel="N(jets)"
    poi0 = RooRealVar("SigmaBin0","SigmaBin0",0,10)  
    poi1 = RooRealVar("SigmaBin1","SigmaBin1",0,10)  
    poi2 = RooRealVar("SigmaBin2","SigmaBin2",0,10)  
    poi3 = RooRealVar("SigmaBin3","SigmaBin3",0,10)  
    poi4 = RooRealVar("SigmaBin4","SigmaBin4",0,10)  
    pois = RooArgList(poi0,poi1,poi2,poi3,poi4)
  
  if (obs=='pt_leadingjet_pt30_eta2p5'):
    h_obs = TH2D(obs,obs,5,0,5,5,0,5)  
    label = ["0 to 30","30 to 55","55 to 95","95 to 200",">200"]
    axisLabel="p_{T}(jet) (GeV)"
    poi0 = RooRealVar("SigmaBin0","SigmaBin0",0,10)  
    poi1 = RooRealVar("SigmaBin1","SigmaBin1",0,10)  
    poi2 = RooRealVar("SigmaBin2","SigmaBin2",0,10)  
    poi3 = RooRealVar("SigmaBin3","SigmaBin3",0,10)  
    poi4 = RooRealVar("SigmaBin4","SigmaBin4",0,10)  
    pois = RooArgList(poi0,poi1,poi2,poi3,poi4)
  

  print r.covQual()
  cm = r.reducedCovarianceMatrix(pois)  
  cm.Print()
  
  for i in range(len(label)):
    #line = "SigmaBin"+str(i)
    line = ""
    for j in range(len(label)):
      #if (i==(len(label)-1) or j==(len(label)-1)):
      #  line +=" "+str(round(r.correlation("SigmaBin"+str(max(i-1,0)),"SigmaBin"+str(max(j-1,0))),3))+";"
      #  h_obs.SetBinContent(i+1,j+1,r.correlation("SigmaBin"+str(max(i-1,0)),"SigmaBin"+str(max(j-1,0))))      
      #else:
      line +=" "+str(round(r.correlation("SigmaBin"+str(i),"SigmaBin"+str(j)),3))+";"
      h_obs.SetBinContent(i+1,j+1,r.correlation("SigmaBin"+str(i),"SigmaBin"+str(j)))
  
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
  latex2.DrawLatex(0.8, 0.94,"137.1 fb^{-1} (13 TeV)")
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
  
