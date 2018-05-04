# Configuration for a simple monojet topology. Use this as a template for your own Run-2 mono-X analysis
# First provide ouput file name in out_file_name field 

out_file_name = 'mono-x_onebin.root'

bins =[250,1500]
systematics=["pu"]

infile = "/desktop/05a/zdemirag/fittingnlo_test4/fittingForest_all.root"

monojet_category = {
	    'name':"monojet"
            ,'in_file_name':infile
            ,"cutstring":"(met>250)"
            ,"varstring":["met",250,3000]
            ,"weightname":"weight"
            ,"bins":bins[:]
            ,"additionalvars":[]#[['met',100,250,3000]]
            ,"pdfmodel":0
            ,"samples":
	   	{  
		  # Signal Region
                  "Zvv_nlo_signal"        :['signal','zjets',1,0]
                  ,"Zll_nlo_signal"       :['signal','zll',1,0]
                  ,"Wlv_nlo_signal"       :['signal','wjets',1,0]
                  ,"ttbar_signal"         :['signal','top',1,0]
                  ,"ST_signal"            :['signal','top',1,0]
                  ,"QCD_signal"           :['signal','qcd',1,0]
                  ,"Diboson_signal"       :['signal','diboson',1,0]
                  ,"Data_signal"          :['signal','data',0,0]
                                     
                  # Single muon-Control
                  ,"Wlv_nlo_singlemuon"    :['Wmn','wjets',1,1]
                  ,"Zll_nlo_singlemuon"    :['Wmn','zll',1,0]
                  ,"ttbar_singlemuon"      :['Wmn','top',1,0]
                  ,"ST_singlemuon"         :['Wmn','top',1,0]
                  ,"QCD_singlemuon"        :['Wmn','qcd',1,0]
                  ,"Diboson_singlemuon"    :['Wmn','diboson',1,0]
                  ,"Data_singlemuon"       :['Wmn','data',0,0]

                  # Single electron-Control
                  ,"Wlv_nlo_singleelectron":['Wen','wjets',1,1]
                  ,"Zll_nlo_singleelectron":['Wen','zll',1,0]
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
            ,"cutstring":"(met>250 && genBosonPt >=-1)"
            ,"varstring":["met",250,3000]
            ,"weightname":"weight"
            ,"bins":bins[:]
            #,"additionalvars":[['met',100,250,3000]]
            ,"pdfmodel":0
            ,"samples":
	   	{  
		  # Signal Region
                    "Zvv_nlo_signal"           :['signal','zjets_0',1,1]
                  }
}

categories = [monojet_category, signal_category_0]
