import tellurium as te
import roadrunner
from CIDmodelBasic import *
import matplotlib.pyplot as plt

CID_reaction = antimonyString #imported from CIDmodelBasic


or_gate = ('''

model *full_pathway()
    // A and B have their own separate nanobodies which interact with their specific
    // molecule of interest (Molecule_1 or Molecule_2)
    A: feedback()
    B: feedback()
    
    A.Mol is "Molecule_1"
    B.Mol is "Molecule_2"
    
    // complex will be our measure of activity
    // (i.e. it goes on to activate GFP)
    A.GeneOn -> A.GeneOn + Mol3;  trans_A * A.GeneOn
    B.GeneOn -> B.GeneOn + Mol4; trans_B * B.GeneOn
    Mol3 + Mol4 -> complex;  K * Mol3 * Mol4

    // species initialization
    Mol3 = 0;
    Mol4 = 0;
    complex = 0;
    
    // for testing OR gate behavior (A.Mol and B.Mol start at nonzero values within feedback())
    // A.Mol = 0
    // B.Mol = 0


    // parameter intialization
    K = 1;
    trans_A = 1;
    trans_B = 1;
end

''')


full_reaction = CID_reaction + or_gate

r = te.loada(full_reaction)
r.simulate(0,50,100, selections = ['time', 'complex'])
r.plot()
plt.show()

