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

antimonyString = ('''
model feedback()
  // Reactions:
  J0: Nan1 + Mol -> Nan1Mol; (K1*Nan1*Mol);
  J1: Nan1Mol -> Nan1 + Mol; (K_1*Nan1Mol); 
  J2: Nan1Mol + Nan2 -> Nan1MolNan2; (K2*Nan1Mol*Nan2)
  J3: Nan1MolNan2 + GeneOff -> GeneOn; (K3*Nan1MolNan2*GeneOff);
  //J4: GeneOn -> Nan1MolNan2 + GeneOff; (K_3*GeneOn);

  // Species initializations:
  Nan1 = 0.0001692; Mol = 0.0001692/2; Nan2 = 0.0001692; Nan1Mol = 0;
  Nan1MolNan2 = 0; GeneOff = 5*10^-5; GeneOn = 0;

  // Variable initialization:
  K1 = 6.1*10^5; K_1 = 8*10^-5; K2 = 3.3*10^5; K3 = 1*10^5; K_3 = 0;
end''')
