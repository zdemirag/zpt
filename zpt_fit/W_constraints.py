import ROOT
from counting_experiment import *
# Define how a control region(s) transfer is made by defining cmodel provide, the calling pattern must be unchanged!
# First define simple string which will be used for the datacard 
model = "wjets"
def cmodel(cid,nam,_f,_fOut, out_ws, diag):
  
  # Some setup
  _fin    = _f.Get("category_%s"%cid)
  _wspace = _fin.Get("wspace_%s"%cid)


  # ############################ USER DEFINED ###########################################################
  # First define the nominal transfer factors (histograms of signal/control, usually MC 
  # note there are many tools available inside include/diagonalize.h for you to make 
  # special datasets/histograms representing these and systematic effects 
  # but for now this is just kept simple 
  processName  = "WJets" # Give a name of the process being modelled
  metname      = "met"    # Observable variable name 
  targetmc     = _fin.Get("signal_wjets")      # define monimal (MC) of which process this config will model
  controlmc    = _fin.Get("Wmn_wjets")  # defines in / out acceptance
  controlmc_e  = _fin.Get("Wen_wjets")  # defines in / out acceptance

  # Create the transfer factors and save them (not here you can also create systematic variations of these 
  # transfer factors (named with extention _sysname_Up/Down
  WScales = targetmc.Clone(); WScales.SetName("wmn_weights_%s"%cid)
  WScales.Divide(controlmc)
  _fOut.WriteTObject(WScales)  # always write out to the directory 

  WScales_e = targetmc.Clone(); WScales_e.SetName("wen_weights_%s"%cid)
  WScales_e.Divide(controlmc_e)
  _fOut.WriteTObject(WScales_e)  # always write out to the directory 

  #######################################################################################################

  _bins = []  # take bins from some histogram, can choose anything but this is easy 
  for b in range(targetmc.GetNbinsX()+1):
    _bins.append(targetmc.GetBinLowEdge(b+1))

  # Here is the important bit which "Builds" the control region, make a list of control regions which 
  # are constraining this process, each "Channel" is created with ...
  # 	(name,_wspace,out_ws,cid+'_'+model,TRANSFERFACTORS) 
  # the second and third arguments can be left unchanged, the others instead must be set
  # TRANSFERFACTORS are what is created above, eg WScales

  CRs = [
   Channel("singlemuon",_wspace,out_ws,cid+'_'+model,WScales),
   Channel("singleelectron",_wspace,out_ws,cid+'_'+model,WScales_e)
  ]


  # ############################ USER DEFINED ###########################################################
  # Add systematics in the following, for normalisations use name, relative size (0.01 --> 1%)
  # for shapes use add_nuisance_shape with (name,_fOut)
  # note, the code will LOOK for something called NOMINAL_name_Up and NOMINAL_name_Down, where NOMINAL=WScales.GetName()
  # these must be created and writted to the same dirctory as the nominal (fDir)

  #CRs[0].add_nuisance("SingleMuonEff",0.01)
  #CRs[1].add_nuisance("SingleElEff",0.02)

  # Statistical uncertainties too!, one per bin 
  for b in range(targetmc.GetNbinsX()):
    err = WScales.GetBinError(b+1)
    if not WScales.GetBinContent(b+1)>0: continue 
    relerr = err/WScales.GetBinContent(b+1)
    if relerr<0.001: continue
    byb_u = WScales.Clone(); byb_u.SetName("wmn_weights_%s_%s_stat_error_%s_bin%d_Up"%(cid,cid,"singlemuonCR",b))
    byb_u.SetBinContent(b+1,WScales.GetBinContent(b+1)+err)
    byb_d = WScales.Clone(); byb_d.SetName("wmn_weights_%s_%s_stat_error_%s_bin%d_Down"%(cid,cid,"singlemuonCR",b))
    byb_d.SetBinContent(b+1,WScales.GetBinContent(b+1)-err)
    _fOut.WriteTObject(byb_u)
    _fOut.WriteTObject(byb_d)
    print "Adding an error -- ", byb_u.GetName(),err
    CRs[0].add_nuisance_shape("%s_stat_error_%s_bin%d"%(cid,"singlemuonCR",b),_fOut)

  # Statistical uncertainties too!, one per bin 
  for b in range(targetmc.GetNbinsX()):
    err_e = WScales_e.GetBinError(b+1)
    if not WScales_e.GetBinContent(b+1)>0: continue 
    relerr_e = err_e/WScales_e.GetBinContent(b+1)
    if relerr_e<0.001: continue
    byb_u_e = WScales_e.Clone(); byb_u_e.SetName("wen_weights_%s_%s_stat_error_%s_bin%d_Up"%(cid,cid,"singleelectronCR",b))
    byb_u_e.SetBinContent(b+1,WScales_e.GetBinContent(b+1)+err_e)
    byb_d_e = WScales_e.Clone(); byb_d_e.SetName("wen_weights_%s_%s_stat_error_%s_bin%d_Down"%(cid,cid,"singleelectronCR",b))
    byb_d_e.SetBinContent(b+1,WScales_e.GetBinContent(b+1)-err_e)
    _fOut.WriteTObject(byb_u_e)
    _fOut.WriteTObject(byb_d_e)
    print "Adding an error -- ", byb_u_e.GetName(),err_e
    CRs[1].add_nuisance_shape("%s_stat_error_%s_bin%d"%(cid,"singleelectronCR",b),_fOut)


  tag = ""
  fztoz_trig = r.TFile.Open("misc/trigger_ratio_newbin.root") 

  ## Here now adding the trigger uncertainty
  wtow_trig_down = fztoz_trig.Get("trig_sys_down"+tag)
  ratio_wtowtrig_down = WScales.Clone(); ratio_wtowtrig_down.SetName("wmn_weights_%s_mettrig_Down"%cid);
  ratio_wtowtrig_down.Multiply(wtow_trig_down)
  _fOut.WriteTObject(ratio_wtowtrig_down)

  wtow_trig_up = fztoz_trig.Get("trig_sys_up"+tag)
  ratio_wtowtrig_up = WScales.Clone(); ratio_wtowtrig_up.SetName("wmn_weights_%s_mettrig_Up"%cid);
  ratio_wtowtrig_up.Multiply(wtow_trig_up)
  _fOut.WriteTObject(ratio_wtowtrig_up)

  CRs[0].add_nuisance_shape("mettrig",_fOut)

  ## Here now adding the trigger uncertainty
  ewtow_trig_down = fztoz_trig.Get("trig_sys_down"+tag)
  eratio_wtowtrig_down = WScales_e.Clone(); eratio_wtowtrig_down.SetName("wen_weights_%s_mettrig_Down"%cid);
  eratio_wtowtrig_down.Multiply(ewtow_trig_down)
  _fOut.WriteTObject(eratio_wtowtrig_down)

  ewtow_trig_up = fztoz_trig.Get("trig_sys_up"+tag)
  eratio_wtowtrig_up = WScales_e.Clone(); eratio_wtowtrig_up.SetName("wen_weights_%s_mettrig_Up"%cid);
  eratio_wtowtrig_up.Multiply(ewtow_trig_up)
  _fOut.WriteTObject(eratio_wtowtrig_up)

  CRs[1].add_nuisance_shape("mettrig",_fOut)


  fwtowpdf = r.TFile.Open("misc/wtow_pdf_sys_newbin.root")                                                                                               

  wtow_pdf_down   = fwtowpdf.Get("ratio_Down"+tag)
  ratio_wtowpdf_down = targetmc.Clone();  ratio_wtowpdf_down.SetName("wmn_weights_%s_wtowpdf_Down"%cid);
  ratio_wtowpdf_down.Divide(controlmc)
  ratio_wtowpdf_down.Multiply(wtow_pdf_down)
  _fOut.WriteTObject(ratio_wtowpdf_down)

  wtow_pdf_up   = fwtowpdf.Get("ratio"+tag)
  ratio_wtowpdf_up = targetmc.Clone();  ratio_wtowpdf_up.SetName("wmn_weights_%s_wtowpdf_Up"%cid);
  ratio_wtowpdf_up.Divide(controlmc)
  ratio_wtowpdf_up.Multiply(wtow_pdf_up)
  _fOut.WriteTObject(ratio_wtowpdf_up)

  ewtow_pdf_down   = fwtowpdf.Get("ratio_Down"+tag)
  eratio_wtowpdf_down = targetmc.Clone();  eratio_wtowpdf_down.SetName("wen_weights_%s_wtowpdf_Down"%cid);
  eratio_wtowpdf_down.Divide(controlmc_e)
  eratio_wtowpdf_down.Multiply(ewtow_pdf_down)
  _fOut.WriteTObject(eratio_wtowpdf_down)

  ewtow_pdf_up   = fwtowpdf.Get("ratio"+tag)
  eratio_wtowpdf_up = targetmc.Clone();  eratio_wtowpdf_up.SetName("wen_weights_%s_wtowpdf_Up"%cid);
  eratio_wtowpdf_up.Divide(controlmc_e)
  eratio_wtowpdf_up.Multiply(ewtow_pdf_up)
  _fOut.WriteTObject(eratio_wtowpdf_up)

  CRs[0].add_nuisance_shape("wtowpdf",_fOut)
  CRs[1].add_nuisance_shape("wtowpdf",_fOut)

  ## Veto uncertainties  
  #fwtowveto = r.TFile.Open("misc/veto_sys.root")
  fwtowveto = r.TFile.Open("misc/veto_sys_newbin.root")

  ## Wmuon CR first
  veto_el_up       = fwtowveto.Get("eleveto"+tag)
  ratio_veto_el_up = WScales.Clone(); ratio_veto_el_up.SetName("wmn_weights_%s_eveto_Up"%cid)
  ratio_veto_el_up.Multiply(veto_el_up)
  _fOut.WriteTObject(ratio_veto_el_up)

  veto_el_down       = fwtowveto.Get("eleveto_Down"+tag)
  ratio_veto_el_down = WScales.Clone(); ratio_veto_el_down.SetName("wmn_weights_%s_eveto_Down"%cid)
  ratio_veto_el_down.Multiply(veto_el_down)
  _fOut.WriteTObject(ratio_veto_el_down)

  veto_mu_up       = fwtowveto.Get("muveto"+tag)
  ratio_veto_mu_up = WScales.Clone(); ratio_veto_mu_up.SetName("wmn_weights_%s_muveto_Up"%cid)
  ratio_veto_mu_up.Multiply(veto_mu_up)
  _fOut.WriteTObject(ratio_veto_mu_up)

  veto_mu_down       = fwtowveto.Get("muveto_Down"+tag)
  ratio_veto_mu_down = WScales.Clone(); ratio_veto_mu_down.SetName("wmn_weights_%s_muveto_Down"%cid)
  ratio_veto_mu_down.Multiply(veto_mu_down)
  _fOut.WriteTObject(ratio_veto_mu_down)

  veto_tau_up       = fwtowveto.Get("tauveto"+tag)
  ratio_veto_tau_up = WScales.Clone(); ratio_veto_tau_up.SetName("wmn_weights_%s_tauveto_Up"%cid)
  ratio_veto_tau_up.Multiply(veto_tau_up)
  _fOut.WriteTObject(ratio_veto_tau_up)

  veto_tau_down       = fwtowveto.Get("tauveto_Down"+tag)
  ratio_veto_tau_down = WScales.Clone(); ratio_veto_tau_down.SetName("wmn_weights_%s_tauveto_Down"%cid)
  ratio_veto_tau_down.Multiply(veto_tau_down)
  _fOut.WriteTObject(ratio_veto_tau_down)

  CRs[0].add_nuisance_shape("eveto",_fOut)
  CRs[0].add_nuisance_shape("muveto",_fOut)
  CRs[0].add_nuisance_shape("tauveto",_fOut)

  ## W electron CR first
  eveto_el_up       = fwtowveto.Get("eleveto"+tag)
  eratio_veto_el_up = WScales_e.Clone(); eratio_veto_el_up.SetName("wen_weights_%s_eveto_Up"%cid)
  eratio_veto_el_up.Multiply(eveto_el_up)
  _fOut.WriteTObject(eratio_veto_el_up)

  eveto_el_down       = fwtowveto.Get("eleveto_Down"+tag)
  eratio_veto_el_down = WScales_e.Clone(); eratio_veto_el_down.SetName("wen_weights_%s_eveto_Down"%cid)
  eratio_veto_el_down.Multiply(eveto_el_down)
  _fOut.WriteTObject(eratio_veto_el_down)

  eveto_mu_up       = fwtowveto.Get("muveto"+tag)
  eratio_veto_mu_up = WScales_e.Clone(); eratio_veto_mu_up.SetName("wen_weights_%s_muveto_Up"%cid)
  eratio_veto_mu_up.Multiply(eveto_mu_up)
  _fOut.WriteTObject(eratio_veto_mu_up)

  eveto_mu_down       = fwtowveto.Get("muveto_Down"+tag)
  eratio_veto_mu_down = WScales_e.Clone(); eratio_veto_mu_down.SetName("wen_weights_%s_muveto_Down"%cid)
  eratio_veto_mu_down.Multiply(eveto_mu_down)
  _fOut.WriteTObject(eratio_veto_mu_down)

  eveto_tau_up       = fwtowveto.Get("tauveto"+tag)
  eratio_veto_tau_up = WScales_e.Clone(); eratio_veto_tau_up.SetName("wen_weights_%s_tauveto_Up"%cid)
  eratio_veto_tau_up.Multiply(eveto_tau_up)
  _fOut.WriteTObject(eratio_veto_tau_up)

  eveto_tau_down       = fwtowveto.Get("tauveto_Down"+tag)
  eratio_veto_tau_down = WScales_e.Clone(); eratio_veto_tau_down.SetName("wen_weights_%s_tauveto_Down"%cid)
  eratio_veto_tau_down.Multiply(eveto_tau_down)
  _fOut.WriteTObject(eratio_veto_tau_down)

  CRs[1].add_nuisance_shape("eveto",_fOut)
  CRs[1].add_nuisance_shape("muveto",_fOut)
  CRs[1].add_nuisance_shape("tauveto",_fOut)
  

  #######################################################################################################

  cat = Category(model,cid,nam,_fin,_fOut,_wspace,out_ws,_bins,metname,targetmc.GetName(),CRs,diag)
  #cat.setDependant("zjets","wjetssignal")  # Can use this to state that the "BASE" of this is already dependant on another process
  # EG if the W->lv in signal is dependant on the Z->vv and then the W->mv is depenant on W->lv, then 
  # give the arguments model,channel name from the config which defines the Z->vv => W->lv map! 
  # Return of course
  return cat

