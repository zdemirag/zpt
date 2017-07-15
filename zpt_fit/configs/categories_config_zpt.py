# Configuration for a simple monojet topology. Use this as a template for your own Run-2 mono-X analysis
# First provide ouput file name in out_file_name field 

out_file_name = 'mono-x.root'

bins = [ 250,350,500,700,1000,1500 ]

monojet_category = {
	    'name':"monojet"
            ,'in_file_name':"/afs/cern.ch/work/z/zdemirag/work/zpt/fit/CMSSW_7_4_7/src/zpt_fit/configs/fitting_zpt/fittingForest_all.root"
            ,"cutstring":"(met>250)"
            ,"varstring":["met",250,1500]
            ,"weightname":"weight"
            ,"bins":bins[:]
            ,"additionalvars":[['met',100,250,1500]]
            ,"pdfmodel":0
            ,"samples":
	   	{  
		  # Signal Region
                  #"Zvv_signal"           :['signal','zjets',1,1]
                  "Zll_signal"           :['signal','zll',1,0]
                  ,"Wlv_signal"           :['signal','wjets',1,0]
                  ,"ttbar_signal"         :['signal','top',1,0]
                  ,"ST_signal"            :['signal','top',1,0]
                  ,"QCD_signal"           :['signal','qcd',1,0]
                  ,"Diboson_signal"       :['signal','diboson',1,0]
                  ,"Data_signal"          :['signal','data',0,0]
                                     
                  # Single muon-Control
                  ,"Wlv_singlemuon"        :['Wmn','wjets',1,1]
                  ,"Zll_singlemuon"        :['Wmn','zll',1,0]
                  ,"ttbar_singlemuon"      :['Wmn','top',1,0]
                  ,"ST_singlemuon"         :['Wmn','top',1,0]
                  ,"QCD_singlemuon"        :['Wmn','qcd',1,0]
                  ,"Diboson_singlemuon"    :['Wmn','diboson',1,0]
                  ,"Data_singlemuon"       :['Wmn','data',0,0]

                  # Single electron-Control
                  ,"Wlv_singleelectron"    :['Wen','wjets',1,1]
                  ,"Zll_singleelectron"    :['Wen','zll',1,0]
                  ,"ttbar_singleelectron"  :['Wen','top',1,0]
                  ,"ST_singleelectron"     :['Wen','top',1,0]
                  ,"QCD_singleelectron"    :['Wen','qcd',1,0]
                  ,"Diboson_singleelectron":['Wen','diboson',1,0]
                  ,"Data_singleelectron"   :['Wen','data',0,0]
	   	},
}

signal_category_1 = {
	    'name':"signal_cat1"
            ,'in_file_name':"/afs/cern.ch/work/z/zdemirag/work/zpt/fit/CMSSW_7_4_7/src/zpt_fit/configs/fitting_zpt/fittingForest_all.root"
            ,"cutstring":"(met>250 && genBosonPt >250 && genBosonPt <350 )"
            ,"varstring":["met",250,1500]
            ,"weightname":"weight"
            ,"bins":bins[:]
            ,"additionalvars":[['met',100,250,1500]]
            ,"pdfmodel":0
            ,"samples":
	   	{  
		  # Signal Region
                  "Zvv_signal"           :['signal','zjets_1',1,1]
                  }
}

signal_category_2 = {
	    'name':"signal_cat2"
            ,'in_file_name':"/afs/cern.ch/work/z/zdemirag/work/zpt/fit/CMSSW_7_4_7/src/zpt_fit/configs/fitting_zpt/fittingForest_all.root"
            ,"cutstring":"(met>250 && genBosonPt >350 && genBosonPt <500 )"
            ,"varstring":["met",250,1500]
            ,"weightname":"weight"
            ,"bins":bins[:]
            ,"additionalvars":[['met',100,250,1500]]
            ,"pdfmodel":0
            ,"samples":
	   	{  
		  # Signal Region
                  "Zvv_signal"           :['signal','zjets_2',1,1]
                  }
}

signal_category_3 = {
	    'name':"signal_cat3"
            ,'in_file_name':"/afs/cern.ch/work/z/zdemirag/work/zpt/fit/CMSSW_7_4_7/src/zpt_fit/configs/fitting_zpt/fittingForest_all.root"
            ,"cutstring":"(met>250 && genBosonPt >500 && genBosonPt <700 )"
            ,"varstring":["met",250,1500]
            ,"weightname":"weight"
            ,"bins":bins[:]
            ,"additionalvars":[['met',100,250,1500]]
            ,"pdfmodel":0
            ,"samples":
	   	{  
		  # Signal Region
                  "Zvv_signal"           :['signal','zjets_3',1,1]
                  }
}

signal_category_4 = {
	    'name':"signal_cat4"
            ,'in_file_name':"/afs/cern.ch/work/z/zdemirag/work/zpt/fit/CMSSW_7_4_7/src/zpt_fit/configs/fitting_zpt/fittingForest_all.root"
            ,"cutstring":"(met>250 && genBosonPt >700 && genBosonPt <1000 )"
            ,"varstring":["met",250,1500]
            ,"weightname":"weight"
            ,"bins":bins[:]
            ,"additionalvars":[['met',100,250,1500]]
            ,"pdfmodel":0
            ,"samples":
	   	{  
		  # Signal Region
                  "Zvv_signal"           :['signal','zjets_4',1,1]
                  }
}

signal_category_5 = {
	    'name':"signal_cat5"
            ,'in_file_name':"/afs/cern.ch/work/z/zdemirag/work/zpt/fit/CMSSW_7_4_7/src/zpt_fit/configs/fitting_zpt/fittingForest_all.root"
            ,"cutstring":"(met>250 && genBosonPt >1000 && genBosonPt <1500 )"
            ,"varstring":["met",250,1500]
            ,"weightname":"weight"
            ,"bins":bins[:]
            ,"additionalvars":[['met',100,250,1500]]
            ,"pdfmodel":0
            ,"samples":
	   	{  
		  # Signal Region
                  "Zvv_signal"           :['signal','zjets_5',1,1]
                  }
}

categories = [monojet_category, signal_category_1, signal_category_2, signal_category_3, signal_category_4, signal_category_5]
