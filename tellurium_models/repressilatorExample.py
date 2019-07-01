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

    #These represent the repressilator that is activated once the gene is turned on.
    
    AMR1: $DNA_REP1 -> RNA_REP1 ; a_rna_rep1 / (1 + REP3^2) * DNA_REP1
    AMR2: $DNA_REP2 -> RNA_REP2 ; a_rna_rep2 / (1 + REP1^2) * DNA_REP2
    AMR3: $DNA_REP3 -> RNA_REP3 ; a_rna_rep3 / (1 + REP2^2) * DNA_REP3 

    DMR1: RNA_REP1 -> ; RNA_REP1 * d_rna_rep1
    DMR2: RNA_REP2 -> ; RNA_REP2 * d_rna_rep2
    DMR3: RNA_REP3 -> ; RNA_REP3 * d_rna_rep3

    AR1: -> REP1 ; RNA_REP1 * a_rep1
    AR2: -> REP2 ; RNA_REP2 * a_rep2 
    AR3: -> REP3 ; RNA_REP3 * a_rep3

    DR1: REP1 -> ; REP1 * d_rep1
    DR2: REP2 -> ; REP2 * d_rep2
    DR3: REP3 -> ; REP3 * d_rep3
             
    # Parameters
    
    # scalingFactor allows us to change the timescale easily, since each of the values for the parameters is initialized to 
    # seconds. 60 * 60 scalingFactor makes the timescale hours instead of seconds.
    scalingFactor = 60 * 60;
    
    a_rna_rep1 = 0.000828 * scalingFactor; 
    a_rna_rep2 = 0.000828 * scalingFactor; 
    a_rna_rep3 = 0.000828 * scalingFactor; 

    d_rna_rep1 = 0.00465 * scalingFactor; 
    d_rna_rep2 = 0.00465 * scalingFactor; 
    d_rna_rep3 = 0.00465 * scalingFactor; 
    
    a_rep1 = 0.0346 * scalingFactor;
    a_rep2 = 0.0346 * scalingFactor;
    a_rep3 = 0.0346 * scalingFactor;
    
    d_rep1 = 0.000138 * scalingFactor;
    d_rep2 = 0.000138 * scalingFactor;
    d_rep3 = 0.000138 * scalingFactor;
    
    # Initial values
    DNA_REP1 = 1;
    DNA_REP2 = 1;
    DNA_REP3 = 1;
    
    RNA_REP1 = 0;
    RNA_REP2 = 0;
    RNA_REP3 = 0;
    
    REP1 = 1;
    REP2 = 0;
    REP3 = 0;
""")
r.simulate(0, 24, 1000)
r.plot()
r.draw()

