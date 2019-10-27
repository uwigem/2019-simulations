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


# The solution that the model uses goes backwards, from the dimer concentrations to the total molecule required to reach those concentrations. 
def plotCurve(anchor_con, dimbinder_con, k_ab, k_bc, alpha, label):
    # The total con of target molecule required for the maximum formation of the dimer
    mol_max_dimer =((k_bc + dimbinder_con) * math.sqrt(k_ab) + (k_ab + anchor_con) * math.sqrt(k_bc)) / (math.sqrt(k_bc) + math.sqrt(k_ab))
    
    # The maximum concentration of the dimer 
    dimer_max_coop = (anchor_con+dimbinder_con+(((math.sqrt(k_ab)+math.sqrt(k_bc))**2)/alpha)-(math.sqrt(((anchor_con+dimbinder_con+(((math.sqrt(k_ab)+math.sqrt(k_bc))**2)/alpha))**2)-(4*anchor_con*dimbinder_con))))/2

    equilibrium_dimer = []
    for i in range(1,300):
        equilibrium_dimer.append(dimer_max_coop / 300 * i)
    equilibrium_dimer.append(dimer_max_coop)
    for i in reversed(range(1,301)):
        equilibrium_dimer.append(dimer_max_coop / 300 * i)
    mol_total = []
    for i in range(0,299):
        intermediate = math.pow((alpha*(equilibrium_dimer[i]-anchor_con)*(equilibrium_dimer[i]-dimbinder_con)-equilibrium_dimer[i]*k_ab),2)-2*equilibrium_dimer[i]*(alpha*(equilibrium_dimer[i]-anchor_con)*(equilibrium_dimer[i]-dimbinder_con)+equilibrium_dimer[i]*k_ab)*k_bc+math.pow(equilibrium_dimer[i],2)*math.pow(k_bc,2)
        radical = math.sqrt(abs(intermediate))
        mol_total.append(0.5*(equilibrium_dimer[i] * alpha + anchor_con + dimbinder_con - k_ab - k_bc + (1/equilibrium_dimer[i]) * (alpha * anchor_con * dimbinder_con-radical)+(1/(alpha*(anchor_con-equilibrium_dimer[i])*(equilibrium_dimer[i]-dimbinder_con))*(math.pow(equilibrium_dimer[i],2)*math.pow(alpha,2)*(anchor_con+dimbinder_con)+(anchor_con+dimbinder_con)*(math.pow(alpha,2)*anchor_con*dimbinder_con+radical)-equilibrium_dimer[i]*(math.pow(alpha,2)*math.pow((anchor_con+dimbinder_con),2)-(anchor_con-dimbinder_con)*(k_ab-k_bc)+2*radical)))))
    mol_total.append(mol_max_dimer)
    for i in range(300,600):
        intermediate = math.pow((alpha*(equilibrium_dimer[i]-anchor_con)*(equilibrium_dimer[i]-dimbinder_con)-equilibrium_dimer[i]*k_ab),2)-2*equilibrium_dimer[i]*(alpha*(equilibrium_dimer[i]-anchor_con)*(equilibrium_dimer[i]-dimbinder_con)+equilibrium_dimer[i]*k_ab)*k_bc+math.pow(equilibrium_dimer[i],2)*math.pow(k_bc,2)
        radical = math.sqrt(abs((intermediate)))
        mol_total.append(0.5*(equilibrium_dimer[i]*alpha+anchor_con+dimbinder_con-k_ab-k_bc+(1/equilibrium_dimer[i])*(alpha*anchor_con*dimbinder_con+radical)+(1/(alpha*(-anchor_con+equilibrium_dimer[i])*(equilibrium_dimer[i]-dimbinder_con))*(-(math.pow(equilibrium_dimer[i],2)*math.pow(alpha,2)*(anchor_con+dimbinder_con))+(anchor_con+dimbinder_con)*(-(math.pow(alpha,2)*anchor_con*dimbinder_con)+radical)+equilibrium_dimer[i]*(math.pow(alpha,2)*math.pow((anchor_con+dimbinder_con),2)-(anchor_con-dimbinder_con)*(k_ab-k_bc)-2*radical)))))
    for i in range(len(mol_total)):
        if mol_total[i] > 0:
            mol_total[i] = math.log10(mol_total[i])
        
    plt.plot(mol_total, equilibrium_dimer, label=label)
    #plt.suptitle("Total Molecule in Sample vs. Concentration of Dimer")
    plt.title("Equal anchor and dimerization binder")
    plt.xlabel('Log(Total Molecule (M))')
    plt.ylabel('Concentration of Dimer (M)')


def plot_param_uncertainty(startVal, name, num_sims):
    stdDev = 0.9999
    print("Plotting Uncertainty")
    vals = []
    # assumes initial parameter estimate as mean and iterates 60% above and below.
    for i in range(-num_sims, 1):
        vals.append(startVal * 10 ** i)
    for i in range(1, num_sims + 1):
        vals.append(startVal * 10 ** i)
    for val in vals:
        # exec("r.%s = %f" % (name, val))
        #result = r.simulate(0,0.5,1000, selections = ['time', 'GeneOn'])
        #plt.plot(result[:,0],result[:,1])
        label = "{:.2E}".format(val) + " M"
        if name == "anchor_con":
            plotCurve(val, dimbinder_con, k_ab, k_bc, alpha, label)
            plt.title("Effect of different concentrations of anchor binder")
        elif name == "dimbinder_con":
            plotCurve(anchor_con, val, k_ab, k_bc, alpha, label)
            plt.title("Effect of different concentrations of dimerization binder")
        elif name == "k_ab":
            plotCurve(anchor_con, dimbinder_con, val, k_bc, alpha, label)
            plt.title("Effect of different K_ab values")

        elif name == "k_bc":
            plotCurve(anchor_con, dimbinder_con, k_ab, val, alpha, label)
            plt.title("Effect of different K_bc values")

        else:
            plotCurve(anchor_con, dimbinder_con, k_ab, k_bc, val, label)
            plt.title("Effect of different cooperativities")
        plt.legend()

### Experimental Data ###
# Eventually I want to have this propagated by json or command line arguments or something
# in mols
anchor_con = 1e-6
dimbinder_con = 1e-6
k_ab = 6e-6
k_bc = 56.4e-9
# the cooperativity term, found experimentally 
alpha = 1e3

limiting_binder = min(anchor_con, dimbinder_con)

# alpha critical corresponds to the cooperativity value at which 50% of the limiting reagent will be engaged in a ternary complex. 
alpha_crit = min(k_ab, k_bc) / max(anchor_con, dimbinder_con)
plt.show()

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
    
alpha_crit = max(k_ab,k_bc) / (max(anchor_con, dimbinder_con) - 0.5 * min(anchor_con, dimbinder_con))
alpha_greater_than_alpha_crit = (alpha >= alpha_crit)

#mol_graphing_conc = 0.1
#dimer_graphing_conc = (mol_graphing_conc - (dimbinder_con + mol_graphing_conc + k_bc - math.pow(math.sqrt((dimbinder_con+mol_graphing_conc+ k_bc),2)-4*dimbinder_con*mol_graphing_conc))/2) * ((anchor_con + mol_graphing_conc + k_ab - math.pow(math.sqrt((anchor_con + mol_graphing_conc + k_ab),2) - 4* anchor_con * mol_graphing_conc))/2)/mol_graphing_conc    
        
# Parameter Sweeping
startVals = [anchor_con, dimbinder_con, k_ab, k_bc, alpha]
names = ["anchor_con", "dimbinder_con", "k_ab", "k_bc", "alpha"]
n = len(names) + 1
dim = math.ceil(math.sqrt(n))

for i, next_param in enumerate(names):
    plt.plot()
    plot_param_uncertainty(startVals[i], names[i], 5)
    plt.show()