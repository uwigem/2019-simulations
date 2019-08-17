# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 21:57:18 2019

@author: Joshua Ip
"""

import tellurium as te
import roadrunner

r = te.loada("""
             ### Reaction Network
             # J1 and J2 label the steps in the reaction network.
             # The equation after the semicolon is the rate of change
             J1: A + B -> C ; k1 * A * B
             
             # Use a dollar sign to indicate that a reactant is constant
             J2: C + $D -> E ; k2 * C * D
             
             # You can make reactions reversible, too
             J3: E -> C ; k3 * E
                     
             # To remove reactants from the system, make the products side of the chemical equation empty
             # This is used for decay steps
             J4: E -> ; k2 / 10
             
             # You can also add reactants to the system by making the reactants side of a chemical equation empty 
             J5: -> A + B ; k1 / 10 
             
             ### Parameters
             # the letter k is frequently used for rate constants.
             # Don't forget the semicolon after each statement
             k1 = 1;
             k2 = 0.5;
             k3 = 0.1;
             
             # Initial values are also parameters
             A = 1;
             B = 1;
             C = 0;
             D = 0;
             E = 0;
""")

# Once the system is set up, use r.simulate to run the simulation
# The first argument is the initial time
# The second argument is the final time
# The third argument is the number of steps
r.simulate(0, 12, 1000)

# r.plot() is used to graph the system. 
r.plot()
