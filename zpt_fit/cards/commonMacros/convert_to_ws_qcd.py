import ROOT
ROOT.gSystem.Load("libHiggsAnalysisCombinedLimit")
from HiggsAnalysis.CombinedLimit.ModelTools import *

cat  = "monojet"

fdir = ROOT.TFile('/home/zdemirag/cms_2017/zpt/CMSSW_8_1_0/src/analysis/zpt_plot/misc/qcd_studies/bkp/qcd_fit.root','READ')

wsin_combine = ROOT.RooWorkspace("monoxQCD","monoxQCD")
wsin_combine._import = SafeWorkspaceImporter(wsin_combine)#getattr(wsin_combine,"import")
 
samplehistos = fdir.GetListOfKeys()
#for s in samplehistos: 
#  obj = s.ReadObj()
#  if type(obj)!=type(ROOT.TH1D()): continue
#  if 'qcd' not in  obj.GetName() : continue
#  samplehist = obj
#  break

varl = ROOT.RooRealVar("met_"+cat,"met_"+cat,0,100000);

# Keys in the fdir 
keys_local = fdir.GetListOfKeys() 
for key in keys_local: 
  obj = key.ReadObj()
  print obj.GetName(), obj.GetTitle(), type(obj)
  if type(obj)!=type(ROOT.TH1D()): continue
  title = obj.GetTitle()
  print title
  if not title.startswith("qcd"): continue # Forget all of the histos which aren't the observable variable
  print "Working with", title
  name = obj.GetTitle()
  if not obj.Integral() > 0 : obj.SetBinContent(1,0.0001) # otherwise Combine will complain!
  print "Creating Data Hist for ", name
  if "central" in name:
    dhist = ROOT.RooDataHist("%s_signal_qcd"%(cat),"Dataset for qcd in monojet SR",ROOT.RooArgList(varl),obj)#cat+"_"+name,"DataSet - %s, %s"%(cat,name),ROOT.RooArgList(varl),obj)
  else:
    name = name.replace("qcd_","")
    print name
    dhist = ROOT.RooDataHist("%s_signal_qcd_%s"%(cat,name),"Dataset for qcd in monojet SR",ROOT.RooArgList(varl),obj)#cat+"_"+name,"DataSet - %s, %s"%(cat,name),ROOT.RooArgList(varl),obj)

  #dhist.Print("v")

  wsin_combine._import(dhist)

wsin_combine.writeToFile("%s_qcd.root"%(cat))

