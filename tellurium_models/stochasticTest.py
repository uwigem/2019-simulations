# -*- coding: utf-8 -*-
"""
Created on Wed May 30 16:39:36 2018

@author: Joshua Ip - Work
"""
import tellurium as te
import numpy as np

import CIDmodelAdvanced as model

r = te.loadAntimonyModel(antimonyString);

r.integrator = 'gillespie';/
r.integrator.seed = 1234;
r.integrator.variable_step_size = False;

# selections specifies the output variables in a simulation
selections = ['time'] + r.getBoundarySpeciesIds() + r.getFloatingSpeciesIds() 
numberOfOutputs = len(selections)
timesToSimulate = 10;
pointsToSimulate = 101;
sumOfSimulations = np.zeros(shape = [pointsToSimulate, numberOfOutputs])

for k in range(timesToSimulate):
    r.resetToOrigin()
    currentSim = r.simulate(0, 24, pointsToSimulate, selections)
    
    # we record the sum of the simulations to calculate the average later
    sumOfSimulations += currentSim

    # since show = false, each trace is added to the current plot instead of starting a new one
    # this is analogous to MATLAB hold on. Alpha causes the opacity to be 50%, so the new lines won't crowd each other out
    #r.plot(currentSim, alpha = 0.5, show = False)


# adds the mean curve for each specified selection. Adds legend, titles, labels to the plot.
fig = te.plot(currentSim[:, 0], sumOfSimulations[:,1:]/timesToSimulate, 
              names = [x + ' (mean)' for x in selections[1:]], 
              title = "Stochastic simulation", 
              xtitle = "time", ytitle = "copies" )
r.simulate(0, 48, 1000, ["time", "Rep", "GeneOff", "GeneOn", "Mol"])