#include "TROOT.h"
#include "TInterpreter.h"
#include "TFile.h"
#include "TCanvas.h"
#include "TH1F.h"
#include "TStyle.h"
#include "TPad.h"
#include "Math/QuantFuncMathCore.h"
#include "TMath.h"
#include "TGraphAsymmErrors.h"
#include "TSystem.h"
#include "TLegend.h"
#include <iostream>
#include "CMS_lumi.C"

bool isDebug = true;

void eraselabel(TPad *p,Double_t h){
  p->cd();
  TPad *pe = new TPad("pe","pe",0.02,0,p->GetLeftMargin(),h);   
  pe->Draw();
  pe->SetFillColor(p->GetFillColor()); 
  pe->SetBorderMode(0);
}

void atributes(TH1D *histo, TString xtitle = "", TString ytitle = "Fraction", TString units = ""){

  histo->SetTitle("");
  //histo->SetMarkerStyle(20);
  //histo->SetMarkerSize(0.8);
  //histo->SetLineWidth(4);
  if(strcmp(units.Data(),"")==0){
    histo->GetXaxis()->SetTitle(xtitle.Data());
    histo->GetXaxis()->SetLabelOffset(0.01);
    histo->GetXaxis()->SetTitleOffset( 0.8);
    histo->GetXaxis()->SetLabelSize  (0.10);
    histo->GetXaxis()->SetTitleSize  (0.11);
  } else {
    histo->GetXaxis()->SetTitle(Form("%s [%s]",xtitle.Data(),units.Data()));
    histo->GetXaxis()->SetLabelOffset(0.00);
    histo->GetXaxis()->SetTitleOffset(  1);
    histo->GetXaxis()->SetLabelSize  (0.08);
    histo->GetXaxis()->SetTitleSize  (0.095);
  }
  histo->GetXaxis()->SetLabelFont  (   42);
  histo->GetXaxis()->SetNdivisions (  505);
  histo->GetXaxis()->SetTitleFont  (   42);
  histo->GetXaxis()->SetTickLength (0.07 );

  histo->GetYaxis()->SetTitle(ytitle.Data());
  histo->GetYaxis()->SetLabelFont  (   42);
  histo->GetYaxis()->SetLabelOffset(0.015);
  histo->GetYaxis()->SetLabelSize  (0.120);
  histo->GetYaxis()->SetNdivisions (  505);
  histo->GetYaxis()->SetTitleFont  (   42);
  histo->GetYaxis()->SetTitleOffset(  0.6);
  histo->GetYaxis()->SetTitleSize  (0.090);
  histo->GetYaxis()->SetTickLength (0.03 );

  histo->SetLineColor  (kBlack);
  histo->SetMarkerStyle(kFullCircle);
}

void finalPlotZllXS(int nsel = 2, bool isNormalized = false,
                    TString plotName = "zPtMeasurements.root", TString outputName = "zPtMeasurements",
                    bool isLogY = true) {

  // nsel == 0 (zll), 1 (znn), 2 (zxx)

  gInterpreter->ExecuteMacro("PaperStyle.C");
  gStyle->SetOptStat(0);

  TString units = "GeV";
  TString XTitle = "p_{T}";
  TString theYTitle = "#sigma / GeV [pb]";
  TString legendText = "";

  TString normName = "";
  if(isNormalized) {
    theYTitle = "1/#sigma d#sigma/dp_{T} [ GeV^{-1}]";
    outputName = outputName + "_normalized";
    normName = "_norm";
  }

  TFile* file1 = new TFile(plotName, "read");  if(!file1) {printf("File %s does not exist\n",plotName.Data()); return;}
  TH1D* hDDilHighPtLL  = (TH1D*)file1->Get(Form("hDDilHighPtLL%s"     ,normName.Data()));
  TH1D* hDDilHighPtNN  = (TH1D*)file1->Get(Form("hDDilHighPtNN%s"     ,normName.Data()));
  TH1D* hDDilHighPtXX  = (TH1D*)file1->Get(Form("hDDilHighPtXX%s"     ,normName.Data()));
  TH1D* hDTheoHighPt  = (TH1D*)file1->Get(Form("hDTheoHighPt%s"      ,normName.Data()));
  TH1D* hDTheoHighPtNoEWK = (TH1D*)file1->Get(Form("hDTheoHighPtNoEWK%s" ,normName.Data()));

  TH1D* hData;
  TH1D* hPred1 = hDTheoHighPt;
  TH1D* hPred2 = hDTheoHighPtNoEWK;

  if     (nsel == 0){
    hData     = hDDilHighPtLL;
    legendText = "Z #rightarrow ll data";
    outputName = outputName + "_zll";
  }
  else if(nsel == 1){
    hData     = hDDilHighPtNN;
    legendText = "Z #rightarrow #nu#nu data";
    outputName = outputName + "_znn";
  }
  else if(nsel == 2){
    hData     = hDDilHighPtXX;
    legendText = "Z #rightarrow ll/#nu#nu data";
    outputName = outputName + "_zxx";
  }
  else {
    return;
  }

  double pull; 
  double pullerr;

  Int_t ww = 800;
  Int_t wh = 800;
  TCanvas *c1 = new TCanvas("c1", "c1", ww, wh);

  TPad* pad0 = new TPad("pad0", "pad0", 0, 0.355, 1, 0.975);
  TPad* pad1 = new TPad("pad1", "pad1", 0, 0.000, 1, 0.345);

  pad0->SetTopMargin   (0.08);
  pad0->SetBottomMargin(0.00);  // 0.02

  pad1->SetTopMargin   (0.05);  // 0.08
  pad1->SetBottomMargin(0.30);  // 0.35

  pad0->Draw();
  pad1->Draw();

  pad0->cd();
  gStyle->SetOptStat(0);
  if(isLogY == true) pad0->SetLogy();

  if(strcmp(units.Data(),"")==0){
    hPred1->GetXaxis()->SetTitle(XTitle.Data());
    hPred1->GetXaxis()->SetLabelOffset(0.005);
    hPred1->GetXaxis()->SetTitleOffset(  0.9);
  } else {
    hPred1->GetXaxis()->SetTitle(Form("%s [%s]",XTitle.Data(),units.Data()));
    hPred1->GetXaxis()->SetLabelOffset(0.00);
    hPred1->GetXaxis()->SetTitleOffset(  1.1);
  }

  hPred1->GetYaxis()->SetTitle(theYTitle.Data());
  hPred1->GetYaxis()->SetLabelFont  (   42);
  hPred1->GetYaxis()->SetLabelOffset(0.015);
  hPred1->GetYaxis()->SetLabelSize  (0.060);
  hPred1->GetYaxis()->SetNdivisions (  505);
  hPred1->GetYaxis()->SetTitleFont  (   42);
  hPred1->GetYaxis()->SetTitleOffset(  1.0);
  hPred1->GetYaxis()->SetTitleSize  (0.050);
  hPred1->GetYaxis()->SetTickLength (0.03 );

  hPred1->GetXaxis()->SetLabelFont  (   42);
  hPred1->GetXaxis()->SetLabelSize  (0.040);
  hPred1->GetXaxis()->SetNdivisions (  505);
  hPred1->GetXaxis()->SetTitleFont  (   42);
  hPred1->GetXaxis()->SetTitleSize  (0.040);
  hPred1->GetXaxis()->SetTickLength (0.07 );
 
  hData->SetLineColor  (kBlack);
  hData->SetMarkerSize(1.5);
  hData->SetMarkerStyle(4);

  hPred1->SetLineColor(kRed);
  hPred1->SetMarkerStyle(3);
  hPred1->SetMarkerColor(kRed);

  hPred2->SetLineColor(kBlue);
  hPred2->SetMarkerStyle(4);
  hPred2->SetMarkerColor(kBlue);

  hData ->SetTitle("");
  hPred1->SetTitle("");
  hPred2->SetTitle("");
  hData ->Scale(1,"width");
  hPred1->Scale(1,"width");
  hPred2->Scale(1,"width");

  if(isLogY == true) hPred1->GetYaxis()->SetRangeUser(hPred1->GetMinimum()/10,hPred1->GetMaximum()*500);
  else               hPred1->GetYaxis()->SetRangeUser(0.0,hPred1->GetMaximum()*1.5);
  hPred1->Draw();
  hPred2->Draw("same");
  hData->Draw("ep,same");

  gStyle->SetOptStat(0);
  TLegend* legend = new TLegend(0.40,0.80,0.80,0.90);
  legend->SetBorderSize(     0);
  legend->SetFillColor (     0);
  legend->SetTextAlign (    12);
  legend->SetTextFont  (    42);
  legend->SetTextSize  (0.03);
  legend->AddEntry(hData,legendText.Data());
  legend->AddEntry(hPred1, "aMC@NLO with EWK corr.");
  legend->AddEntry(hPred2, "aMC@NLO without EWK corr.");

  CMS_lumi( c1, 4, 1);
  legend->Draw();

  /////////////////////////////////////////////pad1///////////////////////////////////////////////////////////////
  pad1->cd();
  gStyle->SetOptStat(0);

  TH1D* hNum = (TH1D*) hData->Clone(); hNum->Reset();
  TH1D* hDen = (TH1D*) hData->Clone(); hDen->Reset();

  TH1D* hRatio = (TH1D*) hData->Clone(); hRatio->Reset();
  TH1D* hBand = (TH1D*) hData->Clone(); hBand->Reset();

  hNum->Add(hPred1);
  hDen->Add(hData);

  for(int i=1; i<=hNum->GetNbinsX(); i++){
    pull = 1.0; pullerr = 0.0;
    if(hNum->GetBinContent(i) > 0 && hDen->GetBinContent(i) > 0){
      pull = (hNum->GetBinContent(i)/hDen->GetBinContent(i));
      pullerr = pull*hDen->GetBinError(i)/hDen->GetBinContent(i);
    }
    else {
      printf("0 events in %d\n",i);
    }
    if(isDebug) printf("ratio(%2d): data/pred = %.3f +/- %.3f predUnc: %.3f\n",i,pull,pullerr,hNum->GetBinError(i)/hNum->GetBinContent(i));
    hRatio->SetBinContent(i,pull);
    hRatio->SetBinError(i,pullerr);
    hBand->SetBinContent(i,1);
    hBand->SetBinError  (i,hNum->GetBinError(i)/hNum->GetBinContent(i)); 
  }
  units = units.ReplaceAll("BIN","");
  atributes(hRatio,XTitle.Data(),"aMC@NLO/Data",units.Data());

  hRatio->Draw("e");
  hBand->SetFillColor(12);
  hBand->SetFillStyle(3003);
  hBand->SetMarkerSize(0);
  hBand->SetLineWidth(0);
  hBand->Draw("E2same");
 
  // Draw a line throgh y=0
  double theLines[2] = {1.0, 0.5};
  TLine* baseline = new TLine(hRatio->GetXaxis()->GetXmin(), theLines[0],
                              hRatio->GetXaxis()->GetXmax(), theLines[0]);
  baseline->SetLineStyle(kDashed);
  baseline->Draw();
  // Set the y-axis range symmetric around y=0
  Double_t dy = TMath::Max(TMath::Abs(hRatio->GetMaximum()),
                           TMath::Abs(hRatio->GetMinimum())) + theLines[1];
  // Double_t dy = TMath::Max(TMath::Abs(TMath::Abs(hRatio->GetMaximum())-1),TMath::Abs(TMath::Abs(hRatio->GetMinimum()))-1);
  hRatio->GetYaxis()->SetRangeUser(0.501,1.499);
  hRatio->GetYaxis()->CenterTitle();
  eraselabel(pad1,hData->GetXaxis()->GetLabelSize());
 
  TLegend* leg = new TLegend(0.20,0.80,0.40,0.90);                                                    
  leg ->SetFillStyle(0);
  leg ->SetFillColor(kWhite);
  leg ->SetBorderSize(0);
  leg->SetTextSize(0.0);                                                                         
  leg->AddEntry(hBand,"Theory prediction","f");
  leg->AddEntry(hRatio,"Experimental data","lpe");
  leg->Draw();
 
  // Draw a line throgh y=0
  theLines[0]=1.0;theLines[1]=0.5;
  baseline = new TLine(hRatio->GetXaxis()->GetXmin(), theLines[0],
		       hRatio->GetXaxis()->GetXmax(), theLines[0]);
  baseline->SetLineStyle(kDashed);
  baseline->Draw();
  // Set the y-axis range symmetric around y=0
  dy = TMath::Max(TMath::Abs(hRatio->GetMaximum()),
		  TMath::Abs(hRatio->GetMinimum())) + theLines[1];
  hRatio->GetYaxis()->SetRangeUser(0.501,1.499);
  hRatio->GetYaxis()->CenterTitle();
  eraselabel(pad1,hData->GetXaxis()->GetLabelSize());

  printf("Total cross section: %f - %f\n", hData->Integral(),hPred1->Integral());

  char CommandToExec[300];
  sprintf(CommandToExec,"mkdir -p plots");
  gSystem->Exec(CommandToExec);  

  if(strcmp(outputName.Data(),"") != 0){
    TString myOutputFile;
    myOutputFile = Form("plots/%s.eps",outputName.Data());
    //c1->SaveAs(myOutputFile.Data());
    myOutputFile = Form("plots/%s.png",outputName.Data());
    c1->SaveAs(myOutputFile.Data());
    myOutputFile = Form("plots/%s.pdf",outputName.Data());
    c1->SaveAs(myOutputFile.Data());
  }

}
