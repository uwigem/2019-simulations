# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 15:45:25 2019

@author: LEGION-JCWP
"""

import tellurium as te
import roadrunner

r = te.loada("""
     #you can put a $ sign before a species to set it to a boundary species (concentration doesn't change)
    J0: $X0 -> S1 ; v_1 * X0
    J1: S1 -> S2 ; v_2 * S1
    J2: S2 -> S3 ; v_3 * S2
    J3: S3 -> S4 ; v_4 * S3
    J4: S4 -> $X5 ; v_5 * S4
     
    # Parameters
    v_1 = 1 
    v_2 = 3
    v_3 = 5
    v_4 = 2
    v_5 = 1
    
    # Initial values
    X0 = 10
    X5 = 10
    S1 = 0
    S2 = 0
    S3 = 0
    S4 = 0
""")

