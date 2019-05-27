void makeZXXNtuple(){

  const int nValues = 5;
  Float_t xbinsHighPt[nValues+1] = {200,300,400,500,800,1500};
  TH1D *hDDilHighPtLL     = new TH1D("hDDilHighPtLL"     , "hDDilHighPtLL"     , nValues, xbinsHighPt);
  TH1D *hDDilHighPtNN     = new TH1D("hDDilHighPtNN"     , "hDDilHighPtNN"     , nValues, xbinsHighPt);
  TH1D *hDDilHighPtXX     = new TH1D("hDDilHighPtXX"     , "hDDilHighPtXX"     , nValues, xbinsHighPt);
  TH1D *hDTheoHighPt      = new TH1D("hDTheoHighPt"      , "hDTheoHighPt"      , nValues, xbinsHighPt);
  TH1D *hDTheoHighPtNoEWK = new TH1D("hDTheoHighPtNoEWK" , "hDTheoHighPtNoEWK" , nValues, xbinsHighPt);

  TH1D *hDDilHighPtLL_norm      = new TH1D("hDDilHighPtLL_norm"     , "hDDilHighPtLL_norm"     , nValues, xbinsHighPt);
  TH1D *hDDilHighPtNN_norm      = new TH1D("hDDilHighPtNN_norm"     , "hDDilHighPtNN_norm"     , nValues, xbinsHighPt);
  TH1D *hDDilHighPtXX_norm      = new TH1D("hDDilHighPtXX_norm"     , "hDDilHighPtXX_norm"     , nValues, xbinsHighPt);
  TH1D *hDTheoHighPt_norm       = new TH1D("hDTheoHighPt_norm"      , "hDTheoHighPt_norm"      , nValues, xbinsHighPt);
  TH1D *hDTheoHighPtNoEWK_norm  = new TH1D("hDTheoHighPtNoEWK_norm" , "hDTheoHighPtNoEWK_norm" , nValues, xbinsHighPt);
  
  /*
  double rsZLL[nValues]  = {1.116,1.039,1.109,1.094,1.141};
  double rsZLLUp[nValues] = {0.041,0.040,0.048,0.055,0.118};
  double rsZNN[nValues]  = {1.128,1.084,1.067,1.043,0.964};
  double rsZNNUp[nValues] = {0.066,0.059,0.061,0.060,0.080};
  double rsZXX[nValues]  = {1.107,1.042,1.068,1.033,0.990};
  double rsZXXUp[nValues] = {0.038,0.037,0.040,0.040,0.063};
  */

  double rsZLL[nValues]  = {1.116,1.039,1.109,1.094,1.141};
  double rsZLLUp[nValues] = {0.047,0.044,0.049,0.057,0.122};
  double rsZNN[nValues]  = {1.128,1.084,1.067,1.043,0.964};
  double rsZNNUp[nValues] = {0.069,0.062,0.063,0.062,0.084};
  double rsZXX[nValues]  = {1.119,1.065,1.072,1.045,1.000};
  double rsZXXUp[nValues] = {0.042,0.038,0.040,0.041,0.064};

  double rsZLL_norm[nValues]   = {1.026,0.957,1.029,1.010,1.070};
  double rsZLLUp_norm[nValues] = {0.005,0.006,0.017,0.029,0.097};
  double rsZNN_norm[nValues]   = {1.085,1.042,1.026,1.003,0.927};
  double rsZNNUp_norm[nValues] = {0.022,0.010,0.020,0.022,0.056};
  double rsZXX_norm[nValues]   = {1.026,0.966,0.990,0.957,0.917};
  double rsZXXUp_norm[nValues] = {0.016,0.014,0.017,0.019,0.048};

  double xs[nValues]        = {2110.30,373.15,86.97,40.05,3.20};
  double xsUp[nValues]      = {0.156,0.177,0.198,0.215,0.285};

  double xs_norm[nValues]   = {0.807406,0.142768,0.033275,0.015323,0.001224};
  double xs_normUp[nValues] = {0.00553,0.01722,0.03625,0.05324,0.12347};

  double xs_noEWK[nValues]        = {2308.32,402.61,96.95,47.11,4.01};
  double xs_noEWKUp[nValues]      = {0.156,0.177,0.198,0.215,0.285};

  double xs_noEWK_norm[nValues]   = {0.807384,0.140821,0.033910,0.016478,0.001403};
  double xs_noEWK_normUp[nValues] = {0.00553,0.01722,0.03625,0.05324,0.12347};

  for(int i=0; i<nValues; i++){
    xs[i]       = xs[i]       / 1000.;
    xs_noEWK[i] = xs_noEWK[i] / 1000.;
    hDDilHighPtLL     ->SetBinContent(i+1,   rsZLL  [i]*xs[i]);
    hDDilHighPtLL     ->SetBinError  (i+1,   rsZLLUp[i]*xs[i]);
    hDDilHighPtNN     ->SetBinContent(i+1,   rsZNN  [i]*xs[i]);
    hDDilHighPtNN     ->SetBinError  (i+1,   rsZNNUp[i]*xs[i]);
    hDDilHighPtXX     ->SetBinContent(i+1,   rsZXX  [i]*xs[i]);
    hDDilHighPtXX     ->SetBinError  (i+1,   rsZXXUp[i]*xs[i]);
    hDTheoHighPt      ->SetBinContent(i+1, xs[i]);
    hDTheoHighPt      ->SetBinError  (i+1, xsUp[i]*xs[i]);
    hDTheoHighPtNoEWK ->SetBinContent(i+1,         xs_noEWK[i]);
    hDTheoHighPtNoEWK ->SetBinError  (i+1, xsUp[i]*xs_noEWK[i]);

    hDDilHighPtLL_norm     ->SetBinContent(i+1,    rsZLL_norm  [i]*xs_norm[i]);
    hDDilHighPtLL_norm     ->SetBinError  (i+1,    rsZLLUp_norm[i]*xs_norm[i]);
    hDDilHighPtNN_norm     ->SetBinContent(i+1,    rsZNN_norm  [i]*xs_norm[i]);
    hDDilHighPtNN_norm     ->SetBinError  (i+1,    rsZNNUp_norm[i]*xs_norm[i]);
    hDDilHighPtXX_norm     ->SetBinContent(i+1,    rsZXX_norm  [i]*xs_norm[i]);
    hDDilHighPtXX_norm     ->SetBinError  (i+1,    rsZXXUp_norm[i]*xs_norm[i]);
    hDTheoHighPt_norm      ->SetBinContent(i+1,            xs_norm[i]);
    hDTheoHighPt_norm      ->SetBinError  (i+1,       xs_normUp[i]*xs_norm[i]);
    hDTheoHighPtNoEWK_norm ->SetBinContent(i+1,              xs_noEWK_norm[i]);
    hDTheoHighPtNoEWK_norm ->SetBinError  (i+1, xs_normUp[i]*xs_noEWK_norm[i]);
  }

  TFile myOutputFile("zPtMeasurements.root","RECREATE");
  hDDilHighPtLL      ->Write();
  hDDilHighPtNN      ->Write();
  hDDilHighPtXX      ->Write();
  hDTheoHighPt       ->Write();
  hDTheoHighPtNoEWK  ->Write();
  hDDilHighPtLL_norm    ->Write();
  hDDilHighPtNN_norm    ->Write();
  hDDilHighPtXX_norm    ->Write();
  hDTheoHighPt_norm     ->Write();
  hDTheoHighPtNoEWK_norm->Write();
  myOutputFile.Close();
}
