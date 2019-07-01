# -*- coding: utf-8 -*-
# Dallas Warren
# Washington iGEM - Simulations
# Model of chemically induced dimerization.
# Nanobody kinetic rates based on antibody kinetic rates.
# Nanobody concentrations based on a protein's average concentration in cell.
# Molecule concentration as an arbitrary number.
# Gene kinetic rates and concentrations fudged.
"""
Tellurium oscillation
"""
import tellurium as te
import roadrunner
import antimony

import CIDmodelBasic as model

r = te.loada (model.antimonyString)
result = r.simulate(0, .5, 1000)
r.plot(result)
