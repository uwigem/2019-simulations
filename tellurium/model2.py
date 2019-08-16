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

limiting_binder = min(anchor_con, dimbinder_con)

# The total con of target molecule required for the maximum formation of the dimer
mol_max_dimer =((k_bc + dimbinder_con) * math.sqrt(k_ab) + (k_ab + anchor_con) * math.sqrt(k_bc)) / (math.sqrt(k_bc) + math.sqrt(k_ab))

# The maximum concentration of the dimer 
dimer_max_coop = (anchor_con + dimbinder_con + (math.pow(math.sqrt(k_ab) + math.sqrt(k_bc),2) / alpha) - (math.sqrt(math.pow(anchor_con + dimbinder_con + math.pow(math.sqrt(k_ab) + math.sqrt(k_bc),2) / alpha,2) - (4 * anchor_con * dimbinder_con))))/2

# TF50 is the concentration of molecule at which the dimer is at 50% of its max concentration in the formation step
### Update +- when we figure out which corresponds to which
TF50 = (anchor_con + dimbinder_con - k_ab - k_bc + (alpha * (dimer_max_coop/2 - anchor_con) * (dimer_max_coop/2 - dimbinder_con))/(dimer_max_coop/2) + anchor_con * (k_bc - k_ab)/(alpha * (dimer_max_coop/2 - anchor_con)) + dimbinder_con * (k_ab - k_bc)/(alpha * (dimer_max_coop/2 - dimbinder_con)) - (alpha/(dimer_max_coop/2) + 1/(anchor_con - dimer_max_coop/2) + 1/(dimbinder_con - dimer_max_coop/2)) * 
        math.sqrt(math.pow(alpha * (dimer_max_coop/2 - anchor_con) * (dimer_max_coop/2 - dimbinder_con) - dimer_max_coop/2 * k_ab, 2) - dimer_max_coop * k_bc * (alpha * (dimer_max_coop/2 - anchor_con) * (dimer_max_coop/2 - dimbinder_con) + dimer_max_coop/2 * k_ab) + math.pow(dimer_max_coop/2, 2) * math.pow(k_bc,2))/alpha)/2  

# TI50 is the concentration of molecule at which the dimer is at 50% of its max concentration in the autoinhibition step                                                
TI50 = (anchor_con + dimbinder_con - k_ab - k_bc + (alpha * (dimer_max_coop/2 - anchor_con) * (dimer_max_coop/2 - dimbinder_con))/(dimer_max_coop/2) + anchor_con * (k_bc - k_ab)/(alpha * (dimer_max_coop/2 - anchor_con)) + dimbinder_con * (k_ab - k_bc)/(alpha * (dimer_max_coop/2 - dimbinder_con)) + (alpha/(dimer_max_coop/2) + 1/(anchor_con - dimer_max_coop/2) + 1/(dimbinder_con - dimer_max_coop/2)) * 
        math.sqrt(math.pow(alpha * (dimer_max_coop/2 - anchor_con) * (dimer_max_coop/2 - dimbinder_con) - dimer_max_coop/2 * k_ab, 2) - dimer_max_coop * k_bc * (alpha * (dimer_max_coop/2 - anchor_con) * (dimer_max_coop/2 - dimbinder_con) + dimer_max_coop/2 * k_ab) + math.pow(dimer_max_coop/2, 2) * math.pow(k_bc,2))/alpha)/2  
              
# On a graph, this measures the width of the bell curve.
dynamic_range = TF50 - TI50

# alpha critical corresponds to the cooperativity value at which 50% of the limiting reagent will be engaged in a ternary complex. 
alpha_crit = min(k_ab, k_bc) / max(anchor_con, dimbinder_con)

# represents the maximal amount of the limiting terminal species
# that can partition into ternary complex for a given set of
# parameters. That means 
ternary_partition_fraction_coop = dimer_max_coop / limiting_binder



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
    
print("Maximum concentration of dimer: " + str(dimer_max_coop))
print("Concentration of molecule required for maximum dimer: " + str(mol_max_dimer))
print("TF50 : " + str(TF50))
print("TI50 : " + str(TI50))
print("Dynamic range : " + str(dynamic_range))





#mol_graphing_conc = 0.1
#dimer_graphing_conc = (mol_graphing_conc - (dimbinder_con + mol_graphing_conc + k_bc - math.pow(math.sqrt((dimbinder_con+mol_graphing_conc+ k_bc),2)-4*dimbinder_con*mol_graphing_conc))/2) * ((anchor_con + mol_graphing_conc + k_ab - math.pow(math.sqrt((anchor_con + mol_graphing_conc + k_ab),2) - 4* anchor_con * mol_graphing_conc))/2)/mol_graphing_conc    
        