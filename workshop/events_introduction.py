# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 21:57:18 2019

@author: LEGION-JCWP
"""

import tellurium as te
import roadrunner

r = te.loada("""
             ### Reaction Network
             J0: -> M ; a_m        #production of mRNA
             J1: M -> ; d_m*M      #degradation of mRNA 
             J2: M -> P ; a_p*M    #production of protein
             J3: P -> ; d_p*P      #degradation of protein
    
            # Parameters
            a_m = 10; d_m = 1     #prod and deg of mRNA
            a_p = 500; d_p = 0.05 #prod and deg of protein
    
            # Initial values 
            M = 0
            P = 0
            
            ### Events
            # Use greater than or equal rather than equals because Telllurium may not simulate an exact time depending on the simulation parameters
            E1: at (time >= 10): d_p = 50;
                
            # You can also delay the firing of an event for a certain amount of time after the requirement is met
            E2: at 12 after (d_p==50): d_p = 0.05;
            
            # Check out the documentation for more advanced settings for events
""")

r.simulate(0, 48, 1000)
r.plot()
