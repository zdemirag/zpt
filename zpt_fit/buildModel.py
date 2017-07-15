import ROOT as r
import array, sys

r.gSystem.AddIncludePath("-I$CMSSW_BASE/src/ ");
r.gSystem.AddIncludePath("-I$ROOFITSYS/include");
r.gSystem.Load("libRooFit.so")
r.gSystem.Load("libRooFitCore.so")

# Configurations Read in from Separate .py files
sys.path.append("configs")
#import categories_config_vtag as x
x = __import__(sys.argv[1]) 

# book category should read list of samples and append them to as histograms 
# expect formats of 
# Region : Process : contributing MC samples
# 	   Process : contributing MC samples
# 	   ...
r.gROOT.SetBatch(1)
# All c++ functionalities
r.gROOT.ProcessLine('.L ./ModelBuilder.cc+')
fout = r.TFile(x.out_file_name,'RECREATE')

# Loop and build components for categories
for cat_id,cat in enumerate(x.categories):
  fin  = r.TFile.Open(cat['in_file_name'])
  fout.cd(); fdir = fout.mkdir("category_%s"%cat['name'])

  mb = r.ModelBuilder(cat_id,cat['name'])
  mb.fIn  = fin
  mb.fOut = fdir
  mb.cutstring  = cat['cutstring']
  mb.setvariable(cat['varstring'][0],cat['varstring'][1],cat['varstring'][2])
  mb.setweight(cat['weightname'])
  mb._pdfmodel=cat['pdfmodel']

  for avar in cat['additionalvars']: mb.addvariable(avar[0],avar[1],avar[2],avar[3])

  # create a template histogram from bins
  bins = cat["bins"]
  histo_base = r.TH1F("base_%d"%cat_id,"base"
        ,len(bins)-1
	,array.array('d',bins))

  mb.lTmp = histo_base.Clone()
  
  if "extra_cuts" in cat.keys():
   for ecut in cat["extra_cuts"]: mb.add_cut(ecut[0],ecut[1])

  # Run through regions and add MC/data processes for each 
  # Each region has 'signal' and 'backgrounds'
  samples = cat['samples'].keys()
  for sample in samples:
      entry = cat['samples'][sample]
      mb.addSample(sample,entry[0],entry[1],entry[2],entry[3],1)  # name, region, process, is_mc, is_signal  
      #mb.addSample(sample,entry[0],entry[1],entry[2],entry[3],0)  # name, region, process, is_mc, is_signal  
  mb.save()

  # Add any 'cutstring' for future reference
  cstr = r.TNamed("cut_category_%s"%cat['name'],cat["cutstring"])
  fdir.cd(); cstr.Write()

print "done!, Model saved in -> ", fout.GetName()
