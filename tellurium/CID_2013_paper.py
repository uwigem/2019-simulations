# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 15:04:56 2019

@author: LEGION-JCWP
"""

import tellurium as te
import roadrunner
""" This model assumes that K_AB > A_total and that """


r = te.loada("""
J0: A + B -> AB ; K_A_B * A * B - K_AB * AB
J1: B + C -> BC ; K_B_C * B * C - K_BC * BC
J4: AB + C -> ABC ; K_AB_C * AB * C - K_ABC * ABC
J5: BC + A -> ABC ; K_BC_A * BC * A - K_BCA * ABC

# *******************************
# Parameters
A = 1;
B = 1;
C = 1;
K_AB = 1;
K_BC = 0.1;
K_AB_C = 1;
K_BC_A = 0.1;
""")

simulation = r.simulate(start=0, end=5, steps=400)
r.plot(simulation)
print(simulation[400,6])