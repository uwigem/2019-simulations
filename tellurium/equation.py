# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 16:01:54 2019

@author: Joshua Ip
"""
import sys
import tellurium as te
import roadrunner
import math
import numpy as np
import matplotlib as plt

### Experimental Data ###
# Eventually I want to have this propagated by json or command line arguments or something
# in mols
anchor_con = 1e-6
dimbinder_con = 1e-6
k_ab = 1e-5
k_bc = 5.6e-6
# the cooperativity term, found experimentally 
alpha = 5e3

# The total con of target molecule required for the maximum formation of the dimer
mol_max_dimer =((k_bc + dimbinder_con) * math.sqrt(k_ab) + (k_ab + anchor_con) * math.sqrt(k_bc)) / (math.sqrt(k_bc) + math.sqrt(k_ab))

# 
dimer_max_noncoop = (anchor_con + dimbinder_con + k_bc + k_ab + 2 * math.sqrt(k_ab * k_bc) - math.sqrt(math.pow(anchor_con + dimbinder_con + k_bc + k_ab + 2 * math.sqrt(k_ab * k_bc), 2) - 4 * anchor_con * dimbinder_con)) / 2

# On a graph, this measures the width of the bell curve.
dynamic_range = TF50 - TI50


if ((anchor_con + k_ab) >= 10 * (dimbinder_con + k_bc)) or (10 * (anchor_con+k_ab) <= (dimbinder_con + k_bc)):
    resolvability = 1
    print("Resolvability assumption met")
else:
    resolvability = 0
    print("Resolvability assumption not met")
    
if (anchor_con >= 10 * k_ab) or (k_ab >= 10 * anchor_con):
    print("AB dominates the reaction")
elif (dimbinder_con >= 10 * k_bc) or (k_bc >= 10 * dimbinder_con):
    print("BC dominates the reaction")
else:
    print("Domination assumption not met")
        

def complex(mol_total, anchor_total, dimerization_total, Kab, Kbc):
    phiab = (anchor_total + mol_total + Kab - math.sqrt((anchor_total + mol_total + Kab)**2 - 4 * anchor_total * mol_total)) / 2 
    phibc = (dimerization_total + mol_total + Kbc - math.sqrt((dimerization_total  + mol_total + Kbc)**2 - 4 * dimerization_total  * mol_total)) / 2 
    result = phiab * phibc / mol_total
    return result



# 
print(complex(3, 1, 1, 1, 1))