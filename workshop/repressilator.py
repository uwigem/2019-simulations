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
    ### Reaction Network
    #These represent the repressilator that is activated once the gene is turned on.
    
             
    ### Parameters
    # Initial values
""")

r.simulate(0, 24, 1000)
r.plot()

