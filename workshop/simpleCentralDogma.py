# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 21:57:18 2019

@author: LEGION-JCWP
"""

import tellurium as te
import roadrunner

r = te.loada("""
            ### Reaction Network
            J0:
            J1:
            J2:
            J3:
            
            # Parameters
            a_m = 10; d_m = 1     #prod and deg of mRNA
            a_p = 500; d_p = 0.05 #prod and deg of protein
    
            # Initial values 
            M = 0
            P = 0
""")

r.simulate(0, 24, 1000)
r.plot()
