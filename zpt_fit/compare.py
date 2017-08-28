#! /usr/bin/env python                                                                                                                                                               
import sys, os, string, re, time, datetime
from multiprocessing import Process
from array import *

from ROOT import *

fin = TFile("mono-x.root","READ")
h_zjets = fin.Get("category_monojet/signal_zjets")

h_zjets_0 = fin.Get("category_signal_cat0/signal_zjets_0")
h_zjets_1 = fin.Get("category_signal_cat1/signal_zjets_1")
h_zjets_2 = fin.Get("category_signal_cat2/signal_zjets_2")
h_zjets_3 = fin.Get("category_signal_cat3/signal_zjets_3")
h_zjets_4 = fin.Get("category_signal_cat4/signal_zjets_4")
h_zjets_5 = fin.Get("category_signal_cat5/signal_zjets_5")

h_zjets_0.Add(h_zjets_1)
h_zjets_0.Add(h_zjets_2)
h_zjets_0.Add(h_zjets_3)
h_zjets_0.Add(h_zjets_4)
h_zjets_0.Add(h_zjets_5)


c = TCanvas("c","c",600,700)
h_zjets.SetLineColor(2)
h_zjets.Draw()
h_zjets_0.Draw("same")

c.SaveAs("ztest.root")
