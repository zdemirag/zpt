# Configuration for a simple monojet topology. Use this as a template for your own Run-2 mono-X analysis
# First provide ouput file name in out_file_name field 

out_file_name = 'mono-x.root'
bins = [ 250.0, 300.0, 350.0, 400.0, 500.0, 750.0, 1000.0, 1500.0]

monojet_category = {
	    'name':"monojet"
            ,'in_file_name':"/desktop/05a/fitting/fittingForest_all.root"
            ,"cutstring":"(met>250)"
            ,"varstring":["met",250,1500]
            ,"weightname":"weight"
            ,"bins":bins[:]
            ,"additionalvars":[['met',100,250,2000]]
            ,"pdfmodel":0
            ,"samples":
	   	{  
		  # Signal Region
                  "Zvv_signal"           :['signal','zjets',1,0]
                  ,"Zll_signal"           :['signal','zll',1,0]
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

signal_category_0 = {
	    'name':"signal_cat0"
            ,'in_file_name':"/desktop/05a/fitting/fittingForest_all.root"
            ,"cutstring":"(met>250 && genBosonPt >=-1 && genBosonPt <200 )"
            ,"varstring":["met",250,1500]
            ,"weightname":"weight"
            ,"bins":bins[:]
            ,"additionalvars":[['met',100,250,1500]]
            ,"pdfmodel":0
            ,"samples":
	   	{  
		  # Signal Region
                  "Zvv_signal"           :['signal','zjets_0',1,0]
                  }
}

signal_category_1 = {
	    'name':"signal_cat1"
            ,'in_file_name':"/desktop/05a/fitting/fittingForest_all.root"
            ,"cutstring":"(met>250 && genBosonPt >=200 && genBosonPt <350 )"
            ,"varstring":["met",250,1500]
            ,"weightname":"weight"
            ,"bins":bins[:]
            ,"additionalvars":[['met',100,250,1500]]
            ,"pdfmodel":0
            ,"samples":
	   	{  
		  # Signal Region
                  "Zvv_signal"           :['signal','zjets_1',1,0]
                  }
}

signal_category_2 = {
	    'name':"signal_cat2"
            ,'in_file_name':"/desktop/05a/fitting/fittingForest_all.root"
            ,"cutstring":"(met>250 && genBosonPt >=350 && genBosonPt <500 )"
            ,"varstring":["met",250,1500]
            ,"weightname":"weight"
            ,"bins":bins[:]
            ,"additionalvars":[['met',100,250,1500]]
            ,"pdfmodel":0
            ,"samples":
	   	{  
		  # Signal Region
                  "Zvv_signal"           :['signal','zjets_2',1,0]
                  }
}

signal_category_3 = {
	    'name':"signal_cat3"
            ,'in_file_name':"/desktop/05a/fitting/fittingForest_all.root"
            ,"cutstring":"(met>250 && genBosonPt >=500 && genBosonPt <1000 )"
            ,"varstring":["met",250,1500]
            ,"weightname":"weight"
            ,"bins":bins[:]
            ,"additionalvars":[['met',100,250,1500]]
            ,"pdfmodel":0
            ,"samples":
	   	{  
		  # Signal Region
                  "Zvv_signal"           :['signal','zjets_3',1,0]
                  }
}

signal_category_4 = {
	    'name':"signal_cat4"
            ,'in_file_name':"/desktop/05a/fitting/fittingForest_all.root"
            ,"cutstring":"(met>250 && genBosonPt >=1000)"
            ,"varstring":["met",250,1500]
            ,"weightname":"weight"
            ,"bins":bins[:]
            ,"additionalvars":[['met',100,250,1500]]
            ,"pdfmodel":0
            ,"samples":
	   	{  
		  # Signal Region
                  "Zvv_signal"           :['signal','zjets_4',1,0]
                  }
}

categories = [monojet_category, signal_category_0, signal_category_1, signal_category_2, signal_category_3, signal_category_4]#, signal_category_5,signal_category_6]
