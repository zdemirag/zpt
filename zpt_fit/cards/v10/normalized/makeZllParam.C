void makeZllParam(
  TString channel="ee", // "mm"
  int dependentBin=1,
  bool debug=false
) {
  TFile *f=TFile::Open(Form("../zll/datacard_Pt_%s.root",channel.Data()));
  // This will be the string for the dependent parameterization 1 + sum((1-r_i)N_i)/ N_m
  TString paramStr = Form("FR%d rateParam * DY_%d 1+(",dependentBin-1,dependentBin-1);
  int var=0; // combine variable counter @0,@1,@2,...
  vector<TString> vars; // list of variables corresponding to the counter
  
  // Start building the numerator term, it does not contain the stats from the dependent fiducial bin
  bool firstNumeratorTerm=true;
  for(int i=1; i<6; i++) { // gen PT bins
    if(i==dependentBin) continue; 
    TH1D *nominal = (TH1D*)f->Get(Form("histo_DY_%d",i-1)); assert(nominal);
    float weight = nominal->Integral();
    if(firstNumeratorTerm) firstNumeratorTerm=false;
    else                   paramStr+="+";
    paramStr+=Form("(1-@%d)*(%.3f",var,weight); var+=1; vars.push_back(Form("RDY_%d",i-1)); // (1-r)x(the expectation...
    for(int j=0; j<10; j++) { // reco MET bins
      float binWeight = nominal->GetBinContent(j+1);
      float binError = nominal->GetBinError(j+1);
      if(binWeight<=0) { if(debug) printf("histo_DY_%d bin %d has 0 entries, skipping\n",i-1,j); continue; }
      if(binError/binWeight<0.005) { if(debug) printf("histo_DY_%d bin %d has less than 0.5%% unc, skipping\n",i-1,j); continue; }
      if(debug) printf("histo_DY_%d bin %d has %.3f entries, %.1f%% unc\n",i-1,j,binWeight,binError/binWeight*100.);
      paramStr+=Form("+%.3f*(@%d)", binError, var); // statistical variations on reco bin
      var+=1; vars.push_back(Form("DYStat_%d_%d%s",i-1,j,channel.Data()));
    }
    paramStr+=")"; // (1-r)x(the expectation +/- bin stats)
  }
  TH1D *nominal = (TH1D*)f->Get(Form("histo_DY_%d",dependentBin-1)); assert(nominal);
  paramStr+=Form(")/(%.3f",nominal->Integral()); // denominator term (N-m ...
  for(int j=0; j<10; j++) { // reco MET bins
    float binWeight = nominal->GetBinContent(j+1);
    float binError = nominal->GetBinError(j+1);
    if(binWeight<=0) { if(debug) printf("histo_DY_%d bin %d has 0 entries, skipping\n",dependentBin-1,j); continue; }
    if(binError/binWeight<0.005) { if(debug) printf("histo_DY_%d bin %d has less than 0.5%% unc, skipping\n",dependentBin-1,j); continue; }
    if(debug) printf("histo_DY_%d bin %d has %.3f entries, %.1f%% unc\n",dependentBin-1,j,binWeight,binError/binWeight*100.);
    paramStr+=Form("+%.3f*(@%d)", binError, var);
    var+=1; vars.push_back(Form("DYStat_%d_%d%s",dependentBin-1,j,channel.Data()));
  } // denominator term (N_m +/- bin stats)
  // list out the independent bin scalings and the stat nuisances in the order in which they appear in the formula
  paramStr+=Form(") %s", vars[0].Data()); 
  for(int iVar=1; iVar<vars.size(); iVar++)
    paramStr+=Form(",%s",vars[iVar].Data());
  // Done building the paramStr, now print out the parameterization for the datacard
  printf("###### copy and paste lines below at the bottom of the datacard ######\n");
  for(int i=1; i<6; i++) { if(i==dependentBin) continue; printf("RDY_%d extArg 1.0 [0.0,2.0]\n", i-1); }
  for(int i=1; i<6; i++) { 
    if(i==dependentBin) 
      printf("%s\n",paramStr.Data());
    else
      printf("FR%d rateParam * DY_%d @0 RDY_%d\n", i-1, i-1, i-1);
  }
}
