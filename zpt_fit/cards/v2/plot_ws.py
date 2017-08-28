  f_data = TFile("higgsCombineTest.MaxLikelihoodFit.mH120.000000.123456.root","READ")
  myworkspace = f_data.Get("w")
  met = myworkspace.var("met_"+category)
  datahist = f_data.Get("toys/toy_asimov")

  CMS_channel = myworkspace.cat("CMS_channel")
  datacut = "CMS_channel==CMS_channel::monojet_signal"
  datahist = datahist.reduce(RooFit.Cut(datacut))
  binned = datahist.binnedClone()
  h_data = binned.createHistogram("h_data",met)
  #h_data = datahist.createHistogram("h_data",met)
  h_data.Sumw2()
