# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 18:42:50 2018

@author: Joshua Ip - Work
"""

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d import Axes3D
import tellurium as te
from tellurium import ParameterScan as ps
import roadrunner
import antimony
import time

antimonyString = ('''
model feedback()
  // Reactions:
  J0: Nan1 + Mol1 -> Nan1Mol; (K1*Nan1*Mol1);
  J1: Nan1Mol -> Nan1 + Mol1; (K_1*Nan1Mol); 
  J2: Nan1Mol + Nan2 -> Nan1MolNan2; (K2*Nan1Mol*Nan2)
  J3: Nan1MolNan2 + Gene1Off -> Gene1On; (K3*Nan1MolNan2*Gene1Off);
  J4: -> Nan3; (K4*Gene1On);

  J5: Nan3 + Mol2 -> Nan3Mol; (K5*Nan3*Mol2)
  J6: Nan3Mol -> Nan3 + Mol2; (K_5*Nan3Mol)
  J7: Nan3Mol + Nan4 -> Nan3MolNan4; (K6 * Nan4 * Nan3Mol)
  J8: Nan3MolNan4 + Gene2Off -> Gene2On; (K7 * Nan3MolNan4 * Gene2Off)
  J9: -> Reporter; Gene2On * K8 - Reporter

  // Species initializations:
  Nan1 = 0.0001692; 
  Mol1 = 0
  Nan2 = 0.0001692; 
  
  Nan3 = 0.0; 
  Mol2 = 0;
  Nan4 = 0.0001692; 
  
  Nan1Mol = 0;
  Nan1MolNan2 = 0; 
  
  Gene1Off = 5*10^-5; 
  Gene1On = 0;

  Gene2Off = 5*10^-5; 
  Gene2On = 0;

  // Variable initialization:
  K1 = 6.1*10^5; 
  K_1 = 8*10^-5; 
  K2 = 3.3*10^5; 
  K3 = 1*10^5; 
  K4 = 0.0001692;
  K_4 = 0.5

  K5 = 6.1*10^5; 
  K_5 = 8*10^-5; 
  K6 = 3.3*10^5; 
  K7 = 1*10^5; 
  K8 = 6.1 * 10^5;
  
  at time >= 0.5: Mol1 = 0.0001692/2;
  at time >= 1.0: Mol2 = 0.0001692/2;
end''')

r = te.loada(antimonyString)

r.simulate(0, 2, 1000, selections = ["time", "Reporter"])
r.plot()

