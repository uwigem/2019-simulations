#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 19:06:55 2018

@author: zackmcnulty
"""
import numpy as np
import matplotlib.pyplot as plt
import tellurium as te
import roadrunner
import antimony
import time

# notes to consider:
# I have added in to the model the fact that rna is not used up as protein is made.
# we also need to consider whether we want G_on to be used up (I have decided yes for now)


r = te.loada("""
# This model describes simple central dogma
    J0: Na + M -> C1 ; k1*M*Na                   #production of nanobody complex
    J1: C1 -> Na + M; k_1*C1                    # reverse process of ^
    J2: C1 + Nd -> C2;  k2*C1*Nd                # dimerization
    J3: C2 -> C1 + Nd;  k_2*C2                   # reverse process of ^
    J4: C2 + G_off -> G_on;  k3*C2*G_off        #dimer acts as TF
    J5: G_on -> G_on + rna ;   a_r*G_on                #creation of mRNA
    J6: rna -> rna + P;       a_p*rna                     # rna to protein
    J7: P ->  ;         d_p*P                          # degradation protein
    J8: rna ->  ;       d_r*rna                         # degradation rna
    J9: G_on -> G_off + C2; k_3*G_on

    # Parameters
    a_r = 10; d_r = 1    #prod and deg of mRNA
    a_p = 500; d_p = 10     #prod and deg of protein
    k1 = 10               #not accurate
    k_1 =  0.01              #not accurate
    k2 = 12               #not accurate
    k_2 = 0.0001              #not accurate
    k3 = 5               #not accurate
    k_3 = 0.1               #not accurate


    # Initial values (every variable needs I.V.)
    M = 0.0001692/2   #arbitrary: we choose (molecule x)
    Na = 0.0001692    #from Dallas's model
    Nd = 0.0001692     #from Dallas's model
    C1 = 0
    C2 = 0
    G_on = 0
    G_off = 5*10^-5   #not accurate
    rna = 0
    P = 0
""")

#clears out any previous simulation results if it exists
r.reset()

#the simulation is run, and is saved in "r.model",
#but results are also stored in "result."
result = r.simulate(0,100000,1000) #(start, end, timepoints)
r.plot(result)
