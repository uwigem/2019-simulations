# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 18:06:31 2018

@author: Joshua Ip - Work
"""

import numpy as np
import matplotlib.pyplot as plt
import tellurium as te
import roadrunner
import antimony
import time


r = te.loada("""
    # In a toggle gene, there are two genes that repress each other. For simplicity,
    # I am naming the genes geneOn and geneOff. When geneOn is expressed, our reporter is 
    # expressed as well.
    
    # Some naming conventions:
    # rep = repressor
    # ind = inducer
    # rept = reporter
    
    # This section represents the transcription and translation of the toggle gene genes.
    AMRON: $geneOn -> RNAOn ; a_rna_rep1 / (1 + repOff^2) * geneOn
    AMROFF: $geneOff -> RNAOff ; a_rna_rep2 / (1 + repOn^2) * geneOff
    TSO: RNAOn -> RNAOn + repOn ; RNAOn * a_rep1
    AR2: RNAOff -> RNAOff + repOff ; RNAOff * a_rep2 

    # This section represents how both the mRNA and the reps can degrade due to natural processes. 
    DMR1: RNAOn -> ; RNAOn * d_rna_rep1
    DMR2: RNAOff -> ; RNAOff * d_rna_rep2
    DR1: repOn -> ; repOn * d_rep1
    DR2: repOff -> ; repOff * d_rep2
    
    # Toggle genees are toggled by inds. In this case, the ind that turns the gene on
    # removes the rep that is primarily expressed when the gene is off, thereby causing
    # the gene for the rep expressed when the gene is on to be expressed
    ACT1: repOff + indOn -> ; 6 * 10 ^ 5 * scalingFactor * repOff * indOn
    ACT2: repOn + indOff -> ; 6 * 10 ^ 5 * scalingFactor * repOn * indOff
    
    # When the gene is turned on, the reporter is also transcribed.
    AREPT: RNAOn -> RNAOn + rept ; a_rep1 * RNAOn
    DREPT: rept -> ; d_rept * rept
        
    # Parameters
    
    # scalingFactor allows us to change the timescale easily, since each of the values for the parameters is initialized to 
    # seconds. 60 * 60 scalingFactor makes the timescale hours instead of seconds.
    
    scalingFactor = 60 * 60;

    a_rna_rep1 = 0.000828 * scalingFactor; 
    a_rna_rep2 = 0.000828 * scalingFactor; 

    d_rna_rep1 = 0.00465 * scalingFactor; 
    d_rna_rep2 = 0.00465 * scalingFactor; 
    
    a_rep1 = 0.0346 * scalingFactor;
    a_rep2 = 0.0346 * scalingFactor;
    
    d_rep1 = 0.000138 * scalingFactor;
    d_rep2 = 0.000138 * scalingFactor;
    
    a_rept = 0.0346 * scalingFactor;
    d_rept = 0.000138 * scalingFactor;
    
    # Initial values
    avoNum = 6.02 * 10 ^ 23 
    yeastVol = 7.3 * 10 ^ -6 # from bionumbers
    geneOn = 1 / avoNum / yeastVol;
    geneOff = 1 / avoNum / yeastVol;
    
    RNAOn = 0;
    RNAOff = 0;
    
    repOn = 0;
    repOff = 30;
    
    indOn = 0;
    indOff = 0;
""")
prepertubation = r.simulate(0, 12, 1000)
r.indOn = 50
pertubation = r.simulate(12, 36, 1000)
r.indOn = 0
r.indOff = 50
postpertubation = r.simulate(36, 900, 10000)
result = np.vstack((prepertubation, pertubation, postpertubation))

plt.figure(1)
plt.plot(result[:,0],result[:,7])
#plt.plot(result[:,0],result[:,5])
#plt.plot(result[:,0],result[:,6])
plt.legend(["reporter", "inducer (On)", "inducer (Off)"])
plt.xlabel("Time (Hours)")
plt.ylabel("Copies")
r.draw()

