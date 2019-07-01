# -*- coding: utf-8 -*-
"""
Created on Wed May 30 16:39:36 2018

@author: Joshua Ip - Work
"""

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

import CIDmodel3 as model

def column(matrix, i):
    return [row[i] for row in matrix]

def measureReporter(moleculeAdded, anc, dim, secondsToSimulate, debug = False):
    for timeshiftToStopWeirdODEIntegratorErrors in range(-10,10):
        try:
            r.reset()
            r.resetToOrigin()
            r.MoleculeAdded = moleculeAdded
            r.K_d_anchor_binder = 10.0 ** anc
            r.K_d_dimerization_binder = 10.0 ** dim
            r.k_off_anchor_binder = r.K_d_anchor_binder * r.k_on_anchor_binder
            r.k_off_anchor_binder = r.K_d_dimerization_binder * r.k_on_dimerization_binder
            arrayOfRates = r.simulate(0, secondsToSimulate, secondsToSimulate / 30 + timeshiftToStopWeirdODEIntegratorErrors)
            measuredReporter = np.amax(column(arrayOfRates, 16))
            if debug:
                print("      Molecule added: " + str(r.MoleculeAdded))
                print("      Measured reporter of: " + str(measuredReporter))
                r.plot(show = False)
                #input("Press Enter to continue...")
            return measuredReporter;
        except:
            if debug:
                print("Threw CVODE error! Attempting timeshift of " + str(timeshiftToStopWeirdODEIntegratorErrors + 1))
            continue;   
    raise RuntimeError('Unable to resolve ODE integrator errors despite timeshift of 20 steps')

r = te.loadAntimonyModel(model.antimonyString);

# This is the range of anchor and dimerization binder binding affinities we will scan through
ancArray = np.arange(-12.0, -5.0, 1.00)
dimArray = np.arange(-9.0, -3.0, 1.00)

# These parameters inform how the simulation is run each time
SECONDS_TO_SIMULATE = 14 * 60 * 60      # 14 hours
PERCENT_CHANGE_PER_STEP = 0.03
INITIAL_MOLECULE_ADDED = 0.0001

# If DEBUG is True, the script outputs some debug information to the console. A lot of debug information.
# It also plots the curve, but that's not really working right. One thing to fix.
DEBUG = True


matrixOfLowerLimits = np.empty((dimArray.size, ancArray.size))
matrixOfUpperLimits = np.empty((dimArray.size, ancArray.size))

for ancIndex, anc in enumerate(ancArray):
    if DEBUG:
        #For graphing
        measuredReporterArray = np.empty(0)
        moleculeAddedArray = np.empty(0)
    
    r.K_d_anchor_binder = 10 ** anc
    print("Anchor Binder K_d: " + str(r.K_d_anchor_binder))    
    arrayOfLowerLimits = np.empty(dimArray.size)
    arrayOfUpperLimits = np.empty(dimArray.size)

    for dimIndex, dim in enumerate(dimArray):
        r.K_d_dimerization_binder = 10 ** dim
        print("   Dimerization Binder K_d: " + str(r.K_d_dimerization_binder))
        
        # finds the lower limit of detection
        moleculeAdded = INITIAL_MOLECULE_ADDED
        noiseValue = 0.1
        
        while True:
            measuredReporter = measureReporter(moleculeAdded, anc, dim, SECONDS_TO_SIMULATE, DEBUG)
            
            if DEBUG:
                # for graphing
                moleculeAddedArray = np.append(moleculeAddedArray, moleculeAdded)
                measuredReporterArray = np.append(measuredReporterArray, measuredReporter)

            if measuredReporter > noiseValue:
                lowerLimitOfDetection = moleculeAdded
                break;
            else:
                moleculeAdded = moleculeAdded * (1.00 + PERCENT_CHANGE_PER_STEP)
                
        # records the lower limit of detection
        arrayOfLowerLimits[dimIndex] = lowerLimitOfDetection
        
        # Finds the upper limit of detection
        changeInMolecule = 0.01 * moleculeAdded
        maxReporter = 0

        while True:
            measuredReporter = measureReporter(moleculeAdded, anc, dim, SECONDS_TO_SIMULATE, DEBUG)

            if DEBUG:
                # for graphing
                moleculeAddedArray = np.append(moleculeAddedArray, moleculeAdded)
                measuredReporterArray = np.append(measuredReporterArray, measuredReporter)
            
            sensitivity = np.absolute((measuredReporter - maxReporter) / changeInMolecule)
            if  sensitivity < 0.01:
                upperLimitOfDetection = moleculeAdded
                arrayOfUpperLimits[dimIndex] = upperLimitOfDetection
                break;
            else:
                maxReporter = measuredReporter
                changeInMolecule = PERCENT_CHANGE_PER_STEP * moleculeAdded
                moleculeAdded = moleculeAdded + changeInMolecule
                
        print("      Dynamic Range: " + str(np.round(lowerLimitOfDetection, 5)) + " - " + str(np.round(upperLimitOfDetection, 5)))

        if DEBUG:
            plt.plot(measuredReporterArray, moleculeAddedArray, label = 'DimAff = ' + str(np.round(dim, 5)) + ' AncAff = ' + str(np.round(anc, 5)), alpha = 0.5)
            #print("   Lower Limit: " + str(lowerLimitOfDetection))
            #print("   Upper Limit: " + str(upperLimitOfDetection))
    
    if DEBUG:
        plt.ylabel("Reporter response")
        plt.xlabel("Molecule added")
        plt.legend()
        plt.show()
    
    matrixOfLowerLimits[:, ancIndex] = arrayOfLowerLimits 
    matrixOfUpperLimits[:, ancIndex] = arrayOfUpperLimits 
    

# plots the 

fig = plt.figure()
ax = fig.gca(projection='3d')

X = ancArray
Y = dimArray
X, Y = np.meshgrid(ancArray, dimArray)

# Plot the surface.
surf = ax.plot_surface(X, Y, matrixOfUpperLimits, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

# Customize the z axis.
ax.set_zlim(0, 80.0)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
ax.set_xlabel('Anchor Nanobody Binding Affinity (K_d)')
ax.set_ylabel('Dimerization Nanobody Binding Affinity (K_d)')
ax.set_zlabel('Upper limit of detection (Molecule concentration outside cell, mM)')
# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()


