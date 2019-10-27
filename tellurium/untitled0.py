# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 16:01:54 2019
@author: Joshua Ip
"""
import math
import matplotlib.pyplot as plt


# The solution that the model uses goes backwards, from the dimer concentrations to the total molecule required to reach those concentrations. 
def plotCurve(anchor_con, dimbinder_con, k_ab, k_bc, alpha):
    equilibrium_dimer = []
    for i in range(1,301):
        equilibrium_dimer.append(dimer_max_coop / 300 * i)
    for i in reversed(range(1,301)):
        equilibrium_dimer.append(dimer_max_coop / 300 * i)
    mol_total = []
    for i in range(0,300):
        intermediate = math.pow((alpha*(equilibrium_dimer[i]-anchor_con)*(equilibrium_dimer[i]-dimbinder_con)-equilibrium_dimer[i]*k_ab),2)-2*equilibrium_dimer[i]*(alpha*(equilibrium_dimer[i]-anchor_con)*(equilibrium_dimer[i]-dimbinder_con)+equilibrium_dimer[i]*k_ab)*k_bc+math.pow(equilibrium_dimer[i],2)*math.pow(k_bc,2)
        radical = math.sqrt(abs(intermediate))
        mol_total.append(0.5*(equilibrium_dimer[i] * alpha + anchor_con + dimbinder_con - k_ab - k_bc + (1/equilibrium_dimer[i]) * (alpha * anchor_con * dimbinder_con-radical)+(1/(alpha*(anchor_con-equilibrium_dimer[i])*(equilibrium_dimer[i]-dimbinder_con))*(math.pow(equilibrium_dimer[i],2)*math.pow(alpha,2)*(anchor_con+dimbinder_con)+(anchor_con+dimbinder_con)*(math.pow(alpha,2)*anchor_con*dimbinder_con+radical)-equilibrium_dimer[i]*(math.pow(alpha,2)*math.pow((anchor_con+dimbinder_con),2)-(anchor_con-dimbinder_con)*(k_ab-k_bc)+2*radical)))))
    for i in range(300,600):
        intermediate = math.pow((alpha*(equilibrium_dimer[i]-anchor_con)*(equilibrium_dimer[i]-dimbinder_con)-equilibrium_dimer[i]*k_ab),2)-2*equilibrium_dimer[i]*(alpha*(equilibrium_dimer[i]-anchor_con)*(equilibrium_dimer[i]-dimbinder_con)+equilibrium_dimer[i]*k_ab)*k_bc+math.pow(equilibrium_dimer[i],2)*math.pow(k_bc,2)
        radical = math.sqrt(abs(intermediate))
        mol_total.append(0.5*(equilibrium_dimer[i]*alpha+anchor_con+dimbinder_con-k_ab-k_bc+(1/equilibrium_dimer[i])*(alpha*anchor_con*dimbinder_con+radical)+(1/(alpha*(-anchor_con+equilibrium_dimer[i])*(equilibrium_dimer[i]-dimbinder_con))*(-(math.pow(equilibrium_dimer[i],2)*math.pow(alpha,2)*(anchor_con+dimbinder_con))+(anchor_con+dimbinder_con)*(-(math.pow(alpha,2)*anchor_con*dimbinder_con)+radical)+equilibrium_dimer[i]*(math.pow(alpha,2)*math.pow((anchor_con+dimbinder_con),2)-(anchor_con-dimbinder_con)*(k_ab-k_bc)-2*radical)))))
    for i in range(len(mol_total)):
        if mol_total[i] > 0:
            mol_total[i] = math.log10(mol_total[i])
        
    plt.plot(mol_total, equilibrium_dimer, label="Concentration of Dimer")
    plt.title("Equal anchor and dimerization binder")
    plt.xlabel('Log(Total Molecule (M))')
    plt.ylabel('Concentration of Dimer (M)')
    plt.show()

### Experimental Data ###
# in mols
anchor_con = 1e-6
dimbinder_con = 1e-6
k_ab = 6e-6
k_bc = 56.4e-9
# the cooperativity term, found experimentally 
alpha = 5e4

plotCurve(anchor_con, dimbinder_con, k_ab, k_bc, alpha)