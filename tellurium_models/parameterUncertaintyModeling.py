#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 19:10:41 2018

@author: zackmcnulty
"""
# -*- coding: utf-8 -*-
# Dallas Warren
# Washington iGEM - Simulations
# Model of chemically induced dimerization.
# Nanobody kinetic rates based on antibody kinetic rates.
# Nanobody concentrations based on a protein's average concentration in cell.
# Molecule concentration as an arbitrary number.
# Gene kinetic rates and concentrations fudged.
"""
Tellurium oscillation
"""
import numpy as np
import tellurium as te
import roadrunner
import antimony
import matplotlib.pyplot as plt
import time

import CIDmodelBasic as model

r = te.loada (model.antimonyString)

def plot_param_uncertainty(model, startVal, name, num_sims):
    stdDev = 0.3*startVal
    #vals = np.linspace((1-stdDev)*startVal, (1+stdDev)*startVal, 100)
    vals = np.random.normal(loc = startVal, scale=stdDev, size = (num_sims, ))
    for val in vals:
        exec("r.%s = %f" % (name, val))
        result = r.simulate(0, .5, 1000)
        r.reset();
        plt.plot(result[:,0],result[:,7])
        plt.title("Response to uncertainty in " + name)
    plt.legend(["GeneOn"])
    plt.xlabel("Time (minutes)")
    plt.ylabel("Concentration")
    plt.ylim([0, 4*10**-5])
    plt.xlim([0, 0.5])




startVals = r.getGlobalParameterValues();
names = r.getGlobalParameterIds();
n = len(names) + 1;
dim = math.ceil(math.sqrt(n))
for i in range(1,n):
    plt.subplot(dim,dim,i)
    plot_param_uncertainty(r, startVals[i-1], names[i-1], 100)



plt.tight_layout()
plt.gcf().set_size_inches(10,10)
plt.show()
