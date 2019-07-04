# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 15:04:56 2019
@author: LEGION-JCWP
"""

import tellurium as te
import roadrunner
""" This model assumes that K_AB > A_total and that """


r = te.loada("""
J0: A + B -> AB ; K_AB * A * B - 1/K_AB * AB
J1: B + C -> BC ; K_BC * B * C - 1/K_BC * BC
J4: AB + C -> ABC ; K_AB_C * AB * C - 1/K_AB_C * ABC
J5: BC + A -> ABC ; K_BC_A * BC * A - 1/K_BC_A * ABC
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

simulation = r.simulate(start=0, end=100, steps=100)
r.plot(simulation)
print(simulation[100,6])
print(simulation)

concentrations =  [0, 0.01, 0.05, 0.1, 0.25, 0.5, 1, 2.5, 5, 10]

for i in concentrations:
    r.resetToOrigin()
    r.B = i
    m = r.simulate(0, 5, 100, ['time', 'ABC'])
    print(m)
    te.plotArray (m, show=False, labels = ['Concentration=' + str(i)], resetColorCycle = False)