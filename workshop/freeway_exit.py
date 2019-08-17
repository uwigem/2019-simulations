# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 15:24:35 2019

@author: LEGION-JCWP
"""

import tellurium as te
import roadrunner

r = te.loada("""
    J0: -> S1 ; v1 
    J1: S1 -> S2 ; v2 * S1
    J2: S3 -> S1 ; v4 * S3
    J3: S3 -> S2 ; v5 * S3
    J4: S2 -> ; v3 * S2
    J5: -> S3 ; v6 
    
    # Parameters
    v1 = 1
    v2 = 1
    v3 = 1
    v4 = 1
    v5 = 1
    v6 = 1
    
    # Initial values
    S1 = 0
    S2 = 0
    S3 = 0
""")

r.reset()
r.simulate(0,30,200)
r.plot()

