void makeZnnParam(
  int dependentBin=1,
  bool debug=false
) {
  TFile *f=TFile::Open("../combined_signal.root");
  RooWorkspace *combinedws = (RooWorkspace*)f->Get("combinedws");
  //"FR0           rateParam ch1_monojet_signal zcat1 (199074-60125.344*@0-14467.811*@1-6774.424*@2-512.864*@3)/117193.960 RDY_1,RDY_2,RDY_3,RDY_4"
  TString paramStr = Form("FR%d rateParam ch1_monojet_signal zcat%d 1+(",dependentBin-1,dependentBin);
  int var=0; // combine variable counter
  vector<TString> vars;
  bool firstNumeratorTerm=true;
  for(int i=1; i<6; i++) { // gen PT bins
    if(i==dependentBin) continue; // dependent variable for first bin
    RooDataHist *rdh = ((RooDataHist*)combinedws->obj(Form("signal_cat%d_signal_zjets_%d",i,i)));
    float weight = rdh->sum(false);
    if(firstNumeratorTerm) firstNumeratorTerm=false;
    else                   paramStr+="+";
    paramStr+=Form("(1-@%d)*(%.3f",var,weight); var+=1; vars.push_back(Form("RDY_%d",i-1));
    for(int j=0; j<10; j++) { // reco MET bins
      rdh->get(j);
      if(rdh->weight()<=0.01) continue;
      paramStr+=Form("+%.3f*(@%d)", rdh->weightError(), var); // statistical variations on reco bin
      var+=1; vars.push_back(Form("stat_signalzjets%d_bin%d",i,j+1));
    }
    paramStr+=")";
  }
  RooDataHist *rdh = ((RooDataHist*)combinedws->obj(Form("signal_cat%d_signal_zjets_%d",dependentBin,dependentBin)));
  paramStr+=Form(")/(%.3f",rdh->sum(false));
  for(int j=0; j<10; j++) { // reco MET bins
    rdh->get(j);
    paramStr+=Form("+%.3f*(@%d)", rdh->weightError(), var);
    var+=1; vars.push_back(Form("stat_signalzjets%d_bin%d",dependentBin,j+1));
  }
  paramStr+=Form(") %s", vars[0].Data());
  for(int iVar=1; iVar<vars.size(); iVar++)
    paramStr+=Form(",%s",vars[iVar].Data());
  
  printf("###### copy and paste lines below at the bottom of the datacard ######\n");
  for(int i=1; i<6; i++) { if(i==dependentBin) continue; printf("RDY_%d extArg 1.0 [0.0,2.0]\n", i-1); }
  for(int i=1; i<6; i++) { 
    if(i==dependentBin) 
      printf("%s\n",paramStr.Data());
    else
      printf("FR%d rateParam * zcat%d @0 RDY_%d\n", i-1, i, i-1); // zcat0 is non-fiducial in Z(vv) analysis
  }
 
}
