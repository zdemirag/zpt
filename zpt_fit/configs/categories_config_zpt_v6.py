# Configuration for a simple monojet topology. Use this as a template for your own Run-2 mono-X analysis
# First provide ouput file name in out_file_name field 

out_file_name = 'mono-x.root'

bins =[250,275,300,350,400,450,500,650,800,1150,1500]

infile = "/desktop/05a/zdemirag/v2/fittingnlo/fittingForest_all.root"

monojet_category = {
	    'name':"monojet"
            ,'in_file_name':infile
            ,"cutstring":"(met>250)"
            ,"varstring":["met",250,3000]
            ,"weightname":"weight"
            ,"bins":bins[:]
            ,"additionalvars":[['met',100,250,3000]]
            ,"pdfmodel":0
            ,"samples":
	   	{  
		  # Signal Region
                  "Zvv_nlo_signal"           :['signal','zjets',1,0]
                  ,"Zll_nlo_signal"           :['signal','zll',1,0]
                  ,"Wlv_nlo_signal"           :['signal','wjets',1,0]
                  ,"ttbar_signal"         :['signal','top',1,0]
                  ,"ST_signal"            :['signal','top',1,0]
                  ,"QCD_signal"           :['signal','qcd',1,0]
                  ,"Diboson_signal"       :['signal','diboson',1,0]
                  ,"Data_signal"          :['signal','data',0,0]
                                     
                  # Single muon-Control
                  ,"Wlv_nlo_singlemuon"        :['Wmn','wjets',1,1]
                  ,"Zll_nlo_singlemuon"        :['Wmn','zll',1,0]
                  ,"ttbar_singlemuon"      :['Wmn','top',1,0]
                  ,"ST_singlemuon"         :['Wmn','top',1,0]
                  ,"QCD_singlemuon"        :['Wmn','qcd',1,0]
                  ,"Diboson_singlemuon"    :['Wmn','diboson',1,0]
                  ,"Data_singlemuon"       :['Wmn','data',0,0]

                  # Single electron-Control
                  ,"Wlv_nlo_singleelectron"    :['Wen','wjets',1,1]
                  ,"Zll_nlo_singleelectron"    :['Wen','zll',1,0]
                  ,"ttbar_singleelectron"  :['Wen','top',1,0]
                  ,"ST_singleelectron"     :['Wen','top',1,0]
                  ,"QCD_singleelectron"    :['Wen','qcd',1,0]
                  ,"Diboson_singleelectron":['Wen','diboson',1,0]
                  ,"Data_singleelectron"   :['Wen','data',0,0]
	   	},
}

signal_category_0 = {
	    'name':"signal_cat0"
            ,'in_file_name':infile
            ,"cutstring":"(met>250 && genBosonPt >=-1 && genBosonPt <200 )"
            ,"varstring":["met",250,3000]
            ,"weightname":"weight"
            ,"bins":bins[:]
            ,"additionalvars":[['met',100,250,3000]]
            ,"pdfmodel":0
            ,"samples":
	   	{  
		  # Signal Region
                  "Zvv_nlo_signal"           :['signal','zjets_0',1,0]
                  }
}

signal_category_1 = {
	    'name':"signal_cat1"
            ,'in_file_name':infile
            ,"cutstring":"(met>250 && genBosonPt >=200 && genBosonPt <300 )"
            ,"varstring":["met",250,3000]
            ,"weightname":"weight"
            ,"bins":bins[:]
            ,"additionalvars":[['met',100,250,3000]]
            ,"pdfmodel":0
            ,"samples":
	   	{  
		  # Signal Region
                  "Zvv_nlo_signal"           :['signal','zjets_1',1,0]
                  }
}

signal_category_2 = {
	    'name':"signal_cat2"
            ,'in_file_name':infile
            ,"cutstring":"(met>250 && genBosonPt >=300 && genBosonPt <400 )"
            ,"varstring":["met",250,3000]
            ,"weightname":"weight"
            ,"bins":bins[:]
            ,"additionalvars":[['met',100,250,3000]]
            ,"pdfmodel":0
            ,"samples":
	   	{  
		  # Signal Region
                  "Zvv_nlo_signal"           :['signal','zjets_2',1,0]
                  }
}

signal_category_3 = {
	    'name':"signal_cat3"
            ,'in_file_name':infile
            ,"cutstring":"(met>250 && genBosonPt >=400 && genBosonPt <500 )"
            ,"varstring":["met",250,3000]
            ,"weightname":"weight"
            ,"bins":bins[:]
            ,"additionalvars":[['met',100,250,3000]]
            ,"pdfmodel":0
            ,"samples":
	   	{  
		  # Signal Region
                  "Zvv_nlo_signal"           :['signal','zjets_3',1,0]
                  }
}


signal_category_4 = {
	    'name':"signal_cat4"
            ,'in_file_name':infile
            ,"cutstring":"(met>250 && genBosonPt >=500 && genBosonPt <800)"
            ,"varstring":["met",250,3000]
            ,"weightname":"weight"
            ,"bins":bins[:]
            ,"additionalvars":[['met',100,250,3000]]
            ,"pdfmodel":0
            ,"samples":
	   	{  
		  # Signal Region
                  "Zvv_nlo_signal"           :['signal','zjets_4',1,0]
                  }
}
signal_category_5 = {
	    'name':"signal_cat5"
            ,'in_file_name':infile
            ,"cutstring":"(met>250 && genBosonPt >=800)"
            ,"varstring":["met",250,3000]
            ,"weightname":"weight"
            ,"bins":bins[:]
            ,"additionalvars":[['met',100,250,3000]]
            ,"pdfmodel":0
            ,"samples":
	   	{  
		  # Signal Region
                  "Zvv_nlo_signal"           :['signal','zjets_5',1,0]
                  }
}

categories = [monojet_category, signal_category_0, signal_category_1, signal_category_2, signal_category_3, signal_category_4, signal_category_5]
