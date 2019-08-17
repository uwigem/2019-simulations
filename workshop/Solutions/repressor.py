# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 21:57:18 2019

@author: LEGION-JCWP
"""

import tellurium as te
import roadrunner

r = te.loada("""
             ### Reaction Network
             J0: $X0 -> S1 ; v_1 * X0 * (K/(K+S3))
             J1: S1 -> S2 ; v_2 * S1
             J2: S2 -> S3 ; v_3 * S2
             J3: S3 -> X1 ; v_4 * S3
                 
             # Parameters
             K = 10
             v_1 = 1
             v_2 = 2
             v_3 = 3
             v_4 = 4
             
             # Initial values
             X0 = 5
             X1 = 0
             S1 = 0
             S2 = 0
             S3 = 0
""")

r.simulate(0, 2, 1000)
r.plot()
