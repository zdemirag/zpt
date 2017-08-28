from ROOT import *
from collections import defaultdict
import math
from array import array
from tdrStyle import *
setTDRStyle()

blind = False

new_dic = defaultdict(dict)

def plotPreFitPostFit(region,category,sb=False,setPull=True):

  datalab = {"singlemuon":"Wmn", "signal":"signal", "singleelectron":"Wen"}

  f_mlfit = TFile('mlfit.root','READ')

  f_data = TFile("mono-x.root","READ")
  f_data.cd("category_"+category)
  h_data = gDirectory.Get(datalab[region]+"_data")

  h_postfit_sig = f_mlfit.Get("shapes_fit_s/"+category+"_"+category+"_signal/total_background")
  h_prefit_sig = f_mlfit.Get("shapes_prefit/"+category+"_"+category+"_signal/total_background")
  
  b_width = [50,50,50,50,100,100,300,400,0]

  channel = {"singlemuon":category+"_singlemu", "signal":category+"_signal", "singleelectron":category+"_singleel"}
  mainbkg = {"singlemuon":"wjets", "signal":"wjets", "singleelectron":"wjets"}


  ##prefit
  h_signal0_pre = f_mlfit.Get("shapes_prefit/monojet_signal/zcat0")
  h_signal1_pre = f_mlfit.Get("shapes_prefit/monojet_signal/zcat1")
  h_signal2_pre = f_mlfit.Get("shapes_prefit/monojet_signal/zcat2")
  h_signal3_pre = f_mlfit.Get("shapes_prefit/monojet_signal/zcat3")
  h_signal4_pre = f_mlfit.Get("shapes_prefit/monojet_signal/zcat4")
  h_signal5_pre = f_mlfit.Get("shapes_prefit/monojet_signal/zcat5")

  h_signal0_pre.Add(h_signal1_pre)
  h_signal0_pre.Add(h_signal2_pre)
  h_signal0_pre.Add(h_signal3_pre)
  h_signal0_pre.Add(h_signal4_pre)
  h_signal0_pre.Add(h_signal5_pre)  

  print "ZEEEE", h_signal0_pre.Integral()

  
  ##postfit
  h_signal0 = f_mlfit.Get("shapes_fit_s/monojet_signal/zcat0")
  h_signal1 = f_mlfit.Get("shapes_fit_s/monojet_signal/zcat1")
  h_signal2 = f_mlfit.Get("shapes_fit_s/monojet_signal/zcat2")
  h_signal3 = f_mlfit.Get("shapes_fit_s/monojet_signal/zcat3")
  h_signal4 = f_mlfit.Get("shapes_fit_s/monojet_signal/zcat4")
  h_signal5 = f_mlfit.Get("shapes_fit_s/monojet_signal/zcat5")

  h_signal0.Add(h_signal1)
  h_signal0.Add(h_signal2)
  h_signal0.Add(h_signal3)
  h_signal0.Add(h_signal4)
  h_signal0.Add(h_signal5)

  processes = [
      'qcd',
      'zll',
      'top',
      'diboson',  
      'ewk',
      'wjets',
      'zjets'
  ]
 
  colors = {
    'diboson':"#DAA520",
    'qcd'    :"#FDFEFE",
    'top'    :"#FFD700",
    'ewk'    :"#000000",
    'zll'    :"#F08080",
    'wjets'  :"#E6E6FA",
    'zjets'  :"#B0C4DE"
  }

  binLowE = []

  # Pre-Fit
  h_prefit = {}
  h_prefit['total'] = f_mlfit.Get("shapes_prefit/"+channel[region]+"/total")
  print "shapes_prefit/"+channel[region]+"/total"
  for i in range(1,h_prefit['total'].GetNbinsX()+2):
    binLowE.append(h_prefit['total'].GetBinLowEdge(i))

  h_all_prefit = TH1F("h_all_prefit","h_all_prefit",len(binLowE)-1,array('d',binLowE))    
  h_other_prefit = TH1F("h_other_prefit","h_other_prefit",len(binLowE)-1,array('d',binLowE))    
  h_stack_prefit = THStack("h_stack_prefit","h_stack_prefit")    

  for process in processes:
    h_prefit[process] = f_mlfit.Get("shapes_prefit/"+channel[region]+"/"+process)
    if (not h_prefit[process]): continue
    if (str(h_prefit[process].Integral())=="nan"): continue
    for i in range(1,h_prefit[process].GetNbinsX()+1):
      content = h_prefit[process].GetBinContent(i)
      width = h_prefit[process].GetBinLowEdge(i+1)-h_prefit[process].GetBinLowEdge(i)
      h_prefit[process].SetBinContent(i,content*width)
    h_prefit[process].SetLineColor(TColor.GetColor(colors[process]))
    h_prefit[process].SetFillColor(TColor.GetColor(colors[process]))
    h_all_prefit.Add(h_prefit[process])
    if (not process==mainbkg[region]): 
      h_other_prefit.Add(h_prefit[process])
    h_stack_prefit.Add(h_prefit[process])
    

  # Post-Fit
  h_postfit = {}
  h_postfit['totalsig'] = f_mlfit.Get("shapes_fit_s/"+channel[region]+"/total")
  h_postfit['total'] = f_mlfit.Get("shapes_fit_s/"+channel[region]+"/total")
  h_all_postfit = TH1F("h_all_postfit","h_all_postfit",len(binLowE)-1,array('d',binLowE))    
  h_other_postfit = TH1F("h_other_postfit","h_other_postfit",len(binLowE)-1,array('d',binLowE))    
  h_minor_postfit = TH1F("h_minor_postfit","h_minor_postfit",len(binLowE)-1,array('d',binLowE))

  h_stack_postfit = THStack("h_stack_postfit","h_stack_postfit")    
  

  h_postfit['totalv2'] = f_mlfit.Get("shapes_fit_s/"+channel[region]+"/total_background")
  ##Adding Signal
  if region is 'signal':
    h_postfit['totalv2'].Add(f_mlfit.Get("shapes_fit_s/"+channel[region]+"/total_signal"))

  print "shapes_fit_s/ch"+channel[region]+"/total_background"

  for i in range(1, h_postfit['totalv2'].GetNbinsX()+1):
    error = h_postfit['totalv2'].GetBinError(i)
    content = h_postfit['totalv2'].GetBinContent(i)
    #print 'TOTAL',i, content, error, error/content*100

  for process in processes:
    print "\n\n",process
    h_postfit[process] = f_mlfit.Get("shapes_fit_s/"+channel[region]+"/"+process)
    if (not h_postfit[process]): continue
    if (str(h_postfit[process].Integral())=="nan"): continue
    for i in range(1,h_postfit[process].GetNbinsX()+1):
      error = h_postfit[process].GetBinError(i)
      content = h_postfit[process].GetBinContent(i)
      width = h_postfit[process].GetBinLowEdge(i+1)-h_postfit[process].GetBinLowEdge(i)
      h_postfit[process].SetBinContent(i,content*width)

    h_postfit[process].SetLineColor(1)
    h_postfit[process].SetFillColor(TColor.GetColor(colors[process]))
    h_all_postfit.Add(h_postfit[process])
    if (not process==mainbkg[region]):
      h_other_postfit.Add(h_postfit[process])
    h_postfit[process].Scale(1,"width")    

    if region in 'signal':
      if process is 'zll':
        h_postfit[process].SetFillColor(TColor.GetColor(colors['zll']))
        h_postfit[process].SetLineColor(1)
        h_stack_postfit.Add(h_postfit[process])

    if process is 'zll':
      continue

    else:
      h_stack_postfit.Add(h_postfit[process])
      

  ##NOW ADDING THE SIGNAL, i.e. Zvv
  #if process is 'signal':
  print "ADDDDDDD"
  h_signal0.SetLineColor(1)
  h_signal0.SetFillColor(TColor.GetColor("#B0C4DE"))

  if region is 'signal':
    h_stack_postfit.Add(h_signal0)

  #print h_all_postfit.Integral()
  #h_all_postfit.Add(h_signal0)
  #print h_all_postfit.Integral()
  #h_all_prefit.Add(h_signal0_pre)


  h_all_postfit.Scale(1,"width")
  if region is 'signal':
    h_all_postfit.Add(h_signal0)

  #print "\n\n PREFIT YIELDS"
  h_all_prefit.Scale(1,"width")
  if region is 'signal':
    h_all_prefit.Add(h_signal0_pre)

  gStyle.SetOptStat(0)


  if setPull:
    c = TCanvas("c","c",600,800)  
  else:
    c = TCanvas("c","c",600,700)  
  SetOwnership(c,False)
  c.cd()
  c.SetLogy()

  if setPull:
    c.SetBottomMargin(0.38)
    c.SetRightMargin(0.06)
  else:
    c.SetBottomMargin(0.3)
    c.SetRightMargin(0.06)

  c.SetTickx(1);
  c.SetTicky(1);
  #c.SetTopMargin(0.07)
  #c.SetLeftMargin(0.18)
  
  dummy = h_all_prefit.Clone("dummy")
  #dummy = TH1F("dummy","dummy",len(binLowE)-1,array('d',binLowE))
  #for i in range(1,dummy.GetNbinsX()):
  #  dummy.SetBinContent(i,0.01)
  dummy.SetFillColor(0)
  dummy.SetLineColor(0)
  dummy.SetLineWidth(0)
  dummy.SetMarkerSize(0)
  dummy.SetMarkerColor(0) 
  dummy.GetYaxis().SetTitle("Events / GeV")
  dummy.GetXaxis().SetTitle("")
  dummy.GetXaxis().SetTitleSize(0)
  dummy.GetXaxis().SetLabelSize(0)
  if region is 'signal':
    dummy.SetMaximum(50*dummy.GetMaximum())
  else:
    dummy.SetMaximum(25*dummy.GetMaximum())
  #dummy.SetMaximum(dummy.GetMaximum())
  dummy.SetMinimum(0.002)
  dummy.GetYaxis().SetTitleOffset(1.15)
  dummy.Draw()
  

  h_other_prefit.SetLineColor(1)
  #h_other_prefit.SetFillColor(kOrange+1)
  #h_other_prefit.SetFillColor(33)
  #h_other_prefit.SetFillColor(kRed-10)
  h_other_prefit.SetFillColor(kBlue-10)
  #h_other_prefit.SetFillColor(kGray)
  h_other_prefit.Scale(1,"width")

  #h_stack_prefit.Scale(1,"width")
  #h_stack_prefit.Draw("histsame")

  h_all_prefit.SetLineColor(2)
  h_all_prefit.SetLineWidth(2)

  #h_all_postfit.SetLineColor(4)
  h_all_postfit.SetLineColor(kAzure-4)
  h_all_postfit.SetLineWidth(2)

  if region in 'signal':

    h_postfit['totalsig'].SetLineColor(1);
    h_postfit['totalsig'].SetFillColor(1);
    h_postfit['totalsig'].SetFillStyle(3144);
    if sb:
      h_postfit['totalsig'].Draw("samehist")

    h_stack_postfit.Draw("histsame")
    
  else:
    h_other_prefit.Draw("histsame")
    h_all_prefit.Draw("histsame")
    h_all_postfit.Draw("histsame")



  h_data.SetMarkerStyle(20)
  h_data.SetLineColor(1)
  h_data.SetMarkerSize(1.2)
  h_data.Scale(1,"width")
  if not blind:
    h_data.Draw("epsame")

  #print "\n\n DATA"
  #for i in range(1,h_data.GetNbinsX()+1):
    #print "$"+str(round(h_data.GetBinContent(i),2))+"$        " , " & ",


  if region == "singlemuon":
    legname = "W #rightarrow #mu#nu"
  if region == "dimuon":
    legname = "Z #rightarrow #mu#mu"
  if region == "singleelectron":
    legname = "W #rightarrow e#nu"
  if region == "dielectron":
    legname = "Z #rightarrow ee"

  
  #legend.SetTextSize(0.04)
  if region in 'signal' :
    #legend = TLegend(.55,.61,.90,.90)
    #legend = TLegend(.6,.55,.90,.90)
    legend = TLegend(0.50, 0.60, 0.92, .92);
    legend.SetFillStyle(0);
    legend.SetBorderSize(0);
    legend.AddEntry(h_data, "Data", "elp")    
    #legend.AddEntry(h_postfit['zjets'], "Z(#nu#nu)+jets", "f")
    legend.AddEntry(h_signal0, "Z(#nu#nu)+jets", "f")
    legend.AddEntry(h_postfit['wjets'], "W(l#nu)+jets", "f")
    #legend.AddEntry(h_postfit['zjets'], "Z #rightarrow #nu#nu", "f")
    #legend.AddEntry(h_postfit['wjets'], "W #rightarrow l#nu", "f")
    legend.AddEntry(h_postfit['diboson'], "WW/ZZ/WZ", "f")
    legend.AddEntry(h_postfit['top'], "Top quark", "f")
    legend.AddEntry(h_postfit['qcd'], "QCD", "f")
    legend.AddEntry(h_postfit['zll'], "Z(ll)+jets", "f")

    #legend.AddEntry(h_sigmj,"Higgs Invisible, m_{H} = 125 GeV","l")
    #legend.AddEntry(h_v,"Vector, M_{med} = 1.6 TeV","l")
    #legend.AddEntry(h_av,"Axial-vector, m_{med} = 1.6 TeV","l")
    #legend.AddEntry(h_all_postfit, "Expected (post-fit)", "l")
    #legend.AddEntry(h_all_prefit, "Expected (pre-fit) ", "l")
    if sb:
      legend.AddEntry(h_postfit['totalsig'], "S+B post-fit", "f")

  else:
    legend = TLegend(.5,.65,.90,.90)
    #legend = TLegend(.6,.6,.92,.92)
    legend.AddEntry(h_data,"Data","elp")
    legend.AddEntry(h_all_postfit, "Post-fit ("+legname+")", "l")
    legend.AddEntry(h_all_prefit, "Pre-fit ("+legname+")", "l")
    legend.AddEntry(h_other_prefit, "Other Backgrounds", "f")    

  legend.SetShadowColor(0);
  legend.SetFillColor(0);
  legend.SetLineColor(0);
  legend.Draw("same")

  latex2 = TLatex()
  latex2.SetNDC()
  latex2.SetTextSize(0.6*c.GetTopMargin())
  latex2.SetTextFont(42)
  latex2.SetTextAlign(31) # align right
  #latex2.DrawLatex(0.9, 0.95,"2.77 fb^{-1} (13 TeV)")
  latex2.DrawLatex(0.94, 0.95,"35.9 fb^{-1} (13 TeV)")
  latex2.SetTextSize(0.6*c.GetTopMargin())
  latex2.SetTextFont(62)
  latex2.SetTextAlign(11) # align right
  #latex2.DrawLatex(0.19, 0.85, "CMS")
  if region is "signal" and category is "monojet":
    latex2.DrawLatex(0.200, 0.85, "CMS")
  else:
    latex2.DrawLatex(0.175, 0.85, "CMS")
    
  #latex2.SetTextSize(0.5*c.GetTopMargin())
  latex2.SetTextSize(0.6*c.GetTopMargin())
  latex2.SetTextFont(52)
  latex2.SetTextAlign(11)
  offset = 0.005
  #latex2.DrawLatex(0.28+offset, 0.85, "Preliminary")          

  categoryLabel = TLatex();
  categoryLabel.SetNDC();
  categoryLabel.SetTextSize(0.5*c.GetTopMargin());
  categoryLabel.SetTextFont(42);
  categoryLabel.SetTextAlign(11);
  #if region is "signal" and category is "monojet":
  #  categoryLabel.DrawLatex(0.200,0.80,"monojet");
  #  categoryLabel.Draw("same");
  #elif region is "signal" and category is "monov":
  #  categoryLabel.DrawLatex(0.175,0.80,"mono-V");
  #  categoryLabel.Draw("same");

  gPad.RedrawAxis()


  if setPull:
    pad2 = TPad("pad2", "pad2", 0.0, 0.0, 1.0, 1.0)
    pad2.SetTopMargin(0.63)
    pad2.SetBottomMargin(0.25)
    pad2.SetRightMargin(0.06)
  else:
    pad2 = TPad("pad2", "pad2", 0.0, 0.0, 1.0, 0.9)
    pad2.SetTopMargin(0.7)
    pad2.SetRightMargin(0.06)

  SetOwnership(pad2,False)
  pad2.SetFillColor(0)
  #pad2.SetGridy(1)
  pad2.SetFillStyle(0)
  pad2.Draw()
  pad2.cd(0)


  met = []; dmet = [];
  ratio_pre = []; ratio_pre_hi = []; ratio_pre_lo = [];
  ratio_post = []; ratio_post_hi = []; ratio_post_lo = [];

  cutstring = "("

  for i in range(1,h_all_prefit.GetNbinsX()+1):

    #ndata = array("d", [0.0])
    #metave = array("d",[0.0])
    #h_data.GetPoint(i-1, metave[0], ndata[0])

    #ndata = h_data.GetY()[i-1]
    ndata = h_data.GetBinContent(i)
    #print ndata

    if (ndata>0.0):
      e_data_hi = h_data.GetBinError(i)/ndata
      e_data_lo = h_data.GetBinError(i)/ndata
    else:
      e_data_hi = 0.0
      e_data_lo = 0.0
      

    n_all_pre = h_all_prefit.GetBinContent(i)
    n_other_pre = h_other_prefit.GetBinContent(i)
    n_all_post = h_all_postfit.GetBinContent(i)


    #n_all_pre = h_all_prefit.GetBinContent(i)
    #n_all_post = h_all_postfit.GetBinContent(i)

    
    #print h_all_prefit.GetBinLowEdge(i),h_all_prefit.GetBinLowEdge(i+1),n_all_pre,n_other_pre,n_all_post,((n_all_post-n_other_pre)/(n_all_pre-n_other_pre))
    cutstring=cutstring+str((n_all_post-n_other_pre)/(n_all_pre-n_other_pre))+"*(met>"+str(h_all_prefit.GetBinLowEdge(i))+"&&met<="+str(h_all_prefit.GetBinLowEdge(i+1))+")"
    if i<h_all_prefit.GetNbinsX():
      cutstring+="+"

    met.append(h_all_prefit.GetBinCenter(i))
    dmet.append((h_all_prefit.GetBinLowEdge(i+1)-h_all_prefit.GetBinLowEdge(i))/2)

    if (n_all_pre>0.0):
      ratio_pre.append(ndata/n_all_pre)
      ratio_pre_hi.append(ndata*e_data_hi/n_all_pre)
      ratio_pre_lo.append(ndata*e_data_lo/n_all_pre)
    else:
      ratio_pre.append(0.0)
      ratio_pre_hi.append(0.0)
      ratio_pre_lo.append(0.0)

    if (n_all_post>0.0):
      ratio_post.append(ndata/n_all_post)
      ratio_post_hi.append(ndata*e_data_hi/n_all_post)
      ratio_post_lo.append(ndata*e_data_lo/n_all_post)      
    else:
      ratio_post.append(0.0)
      ratio_post_hi.append(0.0)
      ratio_post_lo.append(0.0)

  cutstring+=")"
  #print 'cutstring for',region,cutstring

  a_met = array("d", met)
  v_met = TVectorD(len(a_met),a_met)
          
  a_dmet = array("d", dmet)
  v_dmet = TVectorD(len(a_dmet),a_dmet)
    
  a_ratio_pre = array("d", ratio_pre)
  a_ratio_pre_hi = array("d", ratio_pre_hi)
  a_ratio_pre_lo = array("d", ratio_pre_lo)
  
  v_ratio_pre = TVectorD(len(a_ratio_pre),a_ratio_pre)
  v_ratio_pre_hi = TVectorD(len(a_ratio_pre_hi),a_ratio_pre_hi)
  v_ratio_pre_lo = TVectorD(len(a_ratio_pre_lo),a_ratio_pre_lo)

  a_ratio_post = array("d", ratio_post)
  a_ratio_post_hi = array("d", ratio_post_hi)
  a_ratio_post_lo = array("d", ratio_post_lo)

  v_ratio_post = TVectorD(len(a_ratio_post),a_ratio_post)
  v_ratio_post_hi = TVectorD(len(a_ratio_post_hi),a_ratio_post_hi)
  v_ratio_post_lo = TVectorD(len(a_ratio_post_lo),a_ratio_post_lo)

  g_ratio_pre = TGraphAsymmErrors(v_met,v_ratio_pre,v_dmet,v_dmet,v_ratio_pre_lo,v_ratio_pre_hi)
  g_ratio_pre.SetLineColor(2)
  g_ratio_pre.SetMarkerColor(2)
  g_ratio_pre.SetMarkerStyle(20)

  g_ratio_post = TGraphAsymmErrors(v_met,v_ratio_post,v_dmet,v_dmet,v_ratio_post_lo,v_ratio_post_hi)
  #g_ratio_post.SetLineColor(4)
  g_ratio_post.SetLineColor(kAzure-4)
  #g_ratio_post.SetMarkerColor(4)
  g_ratio_post.SetMarkerColor(kAzure-4)
  g_ratio_post.SetMarkerStyle(20)
  
  ratiosys = h_postfit['totalv2'].Clone();
  for hbin in range(0,ratiosys.GetNbinsX()+1): 
        
    ratiosys.SetBinContent(hbin+1,1.0)
    if (h_postfit['totalv2'].GetBinContent(hbin+1)>0):
      ratiosys.SetBinError(hbin+1,h_postfit['totalv2'].GetBinError(hbin+1)/h_postfit['totalv2'].GetBinContent(hbin+1))

      #print hbin+1, h_data.GetBinContent(hbin+1), h_postfit['totalv2'].GetBinContent(hbin+1),h_postfit['totalv2'].GetBinError(hbin+1)
      
    else:
      ratiosys.SetBinError(hbin+1,0)

    #print "Test", ratiosys.GetBinError(hbin+1)


  #dummy2 = h_all_prefit.Clone("dummy2")
  dummy2 = TH1F("dummy2","dummy2",len(binLowE)-1,array('d',binLowE))
  for i in range(1,dummy2.GetNbinsX()):
    dummy2.SetBinContent(i,1.0)
  dummy2.GetYaxis().SetTitle("Data / Pred.")
  if region in 'signal':
    if setPull:
      dummy2.GetXaxis().SetTitle("")
    else:
      dummy2.GetXaxis().SetTitle("E_{T}^{miss} [GeV]")
  else:
    if setPull:
      dummy2.GetXaxis().SetTitle("")
    else:
      dummy2.GetXaxis().SetTitle("Hadronic Recoil [GeV]")
  
  dummy2.SetLineColor(0)
  dummy2.SetMarkerColor(0)
  dummy2.SetLineWidth(0)
  dummy2.SetMarkerSize(0)
  dummy2.GetYaxis().SetLabelSize(0.04)
  #if region is 'signal':
  dummy2.GetYaxis().SetLabelSize(0.03)
  dummy2.GetXaxis().SetLabelSize(0)
  dummy2.GetYaxis().SetNdivisions(5);
  #dummy2.GetYaxis().SetNdivisions(0);
  #dummy2.GetYaxis().SetNdivisions(510);
  #dummy2.GetXaxis().SetNdivisions(510)
  dummy2.GetYaxis().CenterTitle()
  dummy2.GetYaxis().SetTitleSize(0.03)
  #dummy2.GetYaxis().SetTitleOffset(1.3)
  dummy2.GetYaxis().SetTitleOffset(1.6)
  #dummy2.SetMaximum(1.15*(max(v_ratio_pre)+max(v_ratio_pre_hi)))
  #if channel[region] is '2' or channel[region] is '6':
  #  dummy2.SetMaximum(1.8)
  #  dummy2.SetMinimum(0.2)
  #else:
  #  dummy2.SetMaximum(1.2)
  #  dummy2.SetMinimum(0.8)

  if region is 'signal':
    #dummy2.SetMaximum(2.4)                                                                        
    #dummy2.SetMinimum(0.1) 
    #dummy2.SetMaximum(1.85)                                                                        
    #dummy2.SetMinimum(0.15) 

    #dummy2.SetMaximum(1.6)                                                                        
    #dummy2.SetMinimum(0.4) 

    dummy2.SetMaximum(1.15)                                                                        
    dummy2.SetMinimum(0.85) 

    #dummy2.SetMaximum(1.20)                                                                        
    #dummy2.SetMinimum(0.80) 

  else:
    #dummy2.SetMaximum(1.6)                                                                        
    #dummy2.SetMinimum(0.4) 

    #dummy2.SetMaximum(1.2)                                                                        
    #dummy2.SetMinimum(0.8) 
    dummy2.SetMaximum(1.20)                                                                        
    dummy2.SetMinimum(0.80) 
    #dummy2.SetMaximum(1.05)                                                                        
    #dummy2.SetMinimum(0.95) 
    #dummy2.SetMaximum(1.85)                                                                        
    #dummy2.SetMinimum(0.15) 


  dummy2.SetMaximum(1.3)                                                                        
  dummy2.SetMinimum(0.7) 
  #dummy2.SetMaximum(1.2)                                                                        
  #dummy2.SetMinimum(0.8) 
  dummy2.Draw("hist")

  ratiosys.SetFillColor(kGray) #SetFillColor(ROOT.kYellow)
  ratiosys.SetLineColor(kGray) #SetLineColor(1)
  ratiosys.SetLineWidth(1)
  ratiosys.SetMarkerSize(0)
  ratiosys.Draw("e2same")

  f1 = TF1("f1","1",-5000,5000);
  f1.SetLineColor(1);
  f1.SetLineStyle(2);
  f1.SetLineWidth(2);
  f1.Draw("same")

  if not blind:
    g_ratio_pre.Draw("epsame")
    g_ratio_post.Draw("epsame")

  #legend2 = TLegend(0.15,0.26,0.46,0.25)
    #legend2 = TLegend(0.15,0.3,0.7,0.25)
  legend2 = TLegend(0.147651,0.2314815,0.6979866,0.2810847,"","brNDC");

  legend2.AddEntry(g_ratio_post, "Background (post-fit)", "ple")
  legend2.AddEntry(g_ratio_pre, "Background (pre-fit)", "ple")
  
  legend2.SetNColumns(2)

  legend2.SetShadowColor(0);  
  #legend2.SetFillStyle(0);
  legend2.SetFillColor(0);
  legend2.SetLineColor(0);
  #legend2.Draw("same")

  if setPull:

    pad = TPad("pad", "pad", 0.0, 0.0, 1.0, 1.0)
    SetOwnership(pad,False)

    pad.SetTopMargin(0.76)
    pad.SetRightMargin(0.06)
    pad.SetFillColor(0)
    #pad.SetGridy(1)
    pad.SetFillStyle(0)
    pad.Draw()
    pad.cd(0)

    ##Compute the pulls
    data_pull = h_data.Clone("pull")
    data_pull.Add(h_postfit['totalv2'],-1)
    #data_pull.Add(h_sigmj,-1)

    data_pull.Sumw2()
    addedsqrt = 0
    mean = 0
    sigma = 0
    chi2 = 0
    TH1.StatOverflows(1) 

    dummy_pull = TH1F("dummy33","dummy33",len(binLowE)-1,array('d',binLowE))

    for hbin in range(0,data_pull.GetNbinsX()+1):
      if (h_postfit['totalv2'].GetBinContent(hbin)>0):

        addedsqrt +=  (data_pull.GetBinContent(hbin)*data_pull.GetBinContent(hbin))/(h_postfit['totalv2'].GetBinError(hbin)*h_postfit['totalv2'].GetBinError(hbin))
        
        sigma = math.sqrt(h_postfit['totalv2'].GetBinError(hbin)* h_postfit['totalv2'].GetBinError(hbin) + h_data.GetBinError(hbin)*h_data.GetBinError(hbin))
        
        data_pull.SetBinContent(hbin,data_pull.GetBinContent(hbin)/sigma)
      #data_pull.SetBinContent(hbin,data_pull.GetBinContent(hbin)/h_postfit['totalv2'].GetBinError(hbin))
        
        data_pull.SetBinError(hbin,0)
        mean  += data_pull.GetBinContent(hbin)
        chi2  += (data_pull.GetBinContent(hbin)*data_pull.GetBinContent(hbin))
      #sigma += ((data_pull.GetBinContent(hbin)-0.242807588371)*(data_pull.GetBinContent(hbin)-0.242807588371))


    data_pull.SaveAs("test.root")
      
    print "MEAN: ", mean
    print "CHI2: ", math.sqrt(chi2)/data_pull.GetNbinsX()
    
    print "Added2", addedsqrt, "divided: ", addedsqrt/data_pull.GetNbinsX()
    
    data_pull.SetLineColor(kAzure-4)
    data_pull.SetFillColor(kAzure-4)
    data_pull.SetMarkerColor(kAzure-4)

    #data_pull.SetLineColor(4)
    #data_pull.SetFillColor(4)
    #data_pull.SetMarkerColor(4)


    data_pull_sig = h_data.Clone("pull")
    data_pull_sig.Sumw2()
    for hbin in range(0,data_pull_sig.GetNbinsX()+1):
      if (h_postfit['totalv2'].GetBinContent(hbin)>0):
      #print "bin",hbin,"data pull diff", data_pull_sig.GetBinContent(hbin), "sys", h_postfit['totalv2'].GetBinError(hbin)
        data_pull_sig.SetBinContent(hbin,data_pull_sig.GetBinContent(hbin)/h_postfit['totalv2'].GetBinError(hbin))
        data_pull_sig.SetBinError(hbin,0)
        
    data_pull_sig.SetLineColor(2)
    data_pull_sig.SetFillColor(2)
    data_pull_sig.SetFillStyle(3004)
    data_pull_sig.SetMarkerColor(2)


    legend3 = TLegend(0.20,0.21,0.60,0.23,"","brNDC");
    legend3.AddEntry(data_pull    , "Background only", "f")
  #legend3.AddEntry(data_pull_sig, "H_{inv} + Background", "f")
    legend3.AddEntry(data_pull_sig, "AV 1.5 TeV + Background", "f")
    legend3.SetNColumns(2)
    legend3.SetShadowColor(0);  
    legend3.SetFillColor(0);
    legend3.SetLineColor(0);

    dummy3 = TH1F("dummy3","dummy3",len(binLowE)-1,array('d',binLowE))
    for i in range(1,dummy3.GetNbinsX()):
      dummy3.SetBinContent(i,1.0)
    dummy3.GetYaxis().SetTitle("#frac{(Data-Pred.)}{#sigma}")
    if region in 'signal':
      dummy3.GetXaxis().SetTitle("E_{T}^{miss} [GeV]")
    else:
      dummy3.GetXaxis().SetTitle("Hadronic Recoil [GeV]")
    dummy3.SetLineColor(0)
    dummy3.SetMarkerColor(0)
    dummy3.SetLineWidth(0)
    dummy3.SetMarkerSize(0)
    dummy3.GetYaxis().SetLabelSize(0.04)
    if region is 'signal':
      dummy3.GetYaxis().SetLabelSize(0.03)
    dummy3.GetYaxis().SetNdivisions(5);
  #dummy3.GetYaxis().SetNdivisions(0);
  #dummy2.GetYaxis().SetNdivisions(510);
  #dummy3.GetXaxis().SetNdivisions(510)
    dummy3.GetYaxis().CenterTitle()
    dummy3.GetYaxis().SetTitleSize(0.03)
    dummy3.GetYaxis().SetTitleOffset(1.3)
    
    dummy3.SetMaximum(3.5)
    dummy3.SetMinimum(-3.5)

    dummy3.Draw("hist")

  #data_pull.Draw("PE1 same")
    data_pull.Draw("hist same")
  #data_pull_sig.Draw("hist same")
  #legend3.Draw("same");

    
    latex_chi = TLatex()
    latex_chi.SetNDC()
    latex_chi.SetTextSize(0.025)
  #latex_chi.DrawLatex(0.16,0.20,"#Chi^{2} = "+str(round(addedsqrt/data_pull.GetNbinsX(),2)) + "      Mean = "+ str(round(mean,2)))
  #latex_chi.DrawLatex(0.16,0.20,"#Chi^{2} = "+str(round(addedsqrt/data_pull.GetNbinsX(),2)) )
  #latex_chi.DrawLatex(0.16,0.19,"Mean = "+str(round(mean,2)))

  #latex_chi.Draw("same")


    pad2.RedrawAxis("G sameaxis")
    
    gPad.RedrawAxis()


  folder ="/afs/cern.ch/user/z/zdemirag/www/zpt/panda/"
  c.SaveAs(folder+"/PULLS_prefit_postfit_"+region+".pdf")
  c.SaveAs(folder+"/PULLS_prefit_postfit_"+region+".png")
  c.SaveAs(folder+"/PULLS_prefit_postfit_"+region+".C")
  c.SaveAs(folder+"/PULLS_prefit_postfit_"+region+".root")


#plotPreFitPostFit("singlemuon","monojet", setPull=True)
#plotPreFitPostFit("singleelectron","monojet", setPull=True)
plotPreFitPostFit("signal","monojet", setPull=False)
