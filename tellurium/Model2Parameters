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
import matplotlib.pyplot as plt

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

def plotCurve(anchor_con, dimbinder_con, k_ab, k_bc, alpha):
    mol_total = [1e-7, 1e-6, 1e-5, 1e-4, 1e-3, 1e-2, 1e-1, 1, 1e2]
    equilibrium_dimer = []
    for i in mol_total:
        equilibrium_dimer.append(((dimbinder_con+i+k_bc-math.sqrt(math.pow(dimbinder_con+i+k_bc,2)-4*dimbinder_con*i))/2)*((anchor_con+i+k_ab-math.sqrt(math.pow(anchor_con+i+k_ab,2)-4*anchor_con*i))/2)/i)

    #print(str(equilibrium_dimer))
    
    titration_curve = plt.figure()
    for i in range(len(mol_total)):
        mol_total[i] = math.log10(mol_total[i])
    plt.plot(mol_total, equilibrium_dimer, label="Concentration of Dimer")
    #plt.suptitle("Total Molecule in Sample vs. Concentration of Dimer")
    plt.xlabel('Log(Total Molecule (M))')
    plt.ylabel('Concentration of Dimer (M)')
    titration_curve.show()

plotCurve(anchor_con, dimbinder_con, k_ab, k_bc, alpha)

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
        
# Parameter Sweeping
#r = te.loada (titration_curve)

def plot_param_uncertainty(startVal, name, num_sims):
    stdDev = 0.6

    # assumes initial parameter estimate as mean and iterates 60% above and below.
    vals = np.linspace((1-stdDev)*startVal, (1+stdDev)*startVal, 100)
    for val in vals:
        # exec("r.%s = %f" % (name, val))
        #result = r.simulate(0,0.5,1000, selections = ['time', 'GeneOn'])
        #plt.plot(result[:,0],result[:,1])
        if name == "anchor_con":
            plotCurve(val, dimbinder_con, k_ab, k_bc, alpha)
        elif name == "dimbinder_con":
            plotCurve(anchor_con, val, k_ab, k_bc, alpha)
        elif name == "k_ab":
            plotCurve(anchor_con, dimbinder_con, val, k_bc, alpha)
        elif name == "k_bc":
            plotCurve(anchor_con, dimbinder_con, k_ab, val, alpha)
        elif name == "alpha":
            plotCurve(anchor_con, dimbinder_con, k_ab, k_bc, val)
        plt.title(name)
    plt.legend(["equilibrium_dimer"])
    plt.xlabel("log[molecule]")
    plt.ylabel("[dimer]")

#startVals = r.getGlobalParameterValues();
#names = list(enumerate([x for x in r.getGlobalParameterIds() if ("K" in x or "k" in x)]));
startVals = [anchor_con, dimbinder_con, k_ab, k_bc, alpha]
names = ["anchor_con", "dimbinder_con", "k_ab", "k_bc", "alpha"]
n = len(names) + 1
dim = math.ceil(math.sqrt(n))

for i, next_param in enumerate(names):
    plt.subplot(dim, dim, i + 1)
    plot_param_uncertainty(startVals[i], names[i], 100)
plt.tight_layout()
plt.show()