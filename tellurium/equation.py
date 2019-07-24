# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 16:01:54 2019

@author: Joshua IP
"""

import tellurium as te
import roadrunner
import math
import numpy as np
import matplotlib as plt

def complex(mol_total, anchor_total, dimerization_total, Kab, Kbc):
    phiab = (anchor_total + mol_total + Kab - math.sqrt((anchor_total + mol_total + Kab)**2 - 4 * anchor_total * mol_total)) / 2 
    phibc = (dimerization_total + mol_total + Kbc - math.sqrt((dimerization_total  + mol_total + Kbc)**2 - 4 * dimerization_total  * mol_total)) / 2 
    result = phiab * phibc / mol_total
    return result

print(complex(3, 1, 1, 1, 1))