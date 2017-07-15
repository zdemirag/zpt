#########################################################################################
# Setup the basics ----> USER DEFINED SECTION HERE ------------------------------------//

fName    = "mono-x.root"
fOutName = "combined_signal.root"

categories = ["signal_cat1","signal_cat2","signal_cat3","signal_cat4","signal_cat5"] # --> Should be labeled as in original config 
#--------------------------------------------------------------------------------------//
#########################################################################################

# Leave the following alone!
# Headers 
#from combineControlRegions import *
from counting_experiment import *
from convert import * 

from HiggsAnalysis.CombinedLimit.ModelTools import *

import ROOT as r 
r.gROOT.SetBatch(1)

_fOut    = r.TFile(fOutName,"RECREATE") 
_f       = r.TFile.Open(fName) 
out_ws   = r.RooWorkspace("combinedws") 
out_ws._import = SafeWorkspaceImporter(out_ws)

convertToCombineWorkspace(out_ws,_f,categories,[],[],"met_monojet")  # use the same converter tool, but no need for fancy stuff, last argument is if we want to simply name the variable!
_fOut.WriteTObject(out_ws)

print "Produced Signals Models in --> ", _fOut.GetName()
