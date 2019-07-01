# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 23:17:40 2018

@author: frances
"""

#Need to find rate constants, initial values?

import tellurium as te

r = te.loada('''
  
# Reactions:
  #lambda cl
  Y1: R + Gy -> gy; (k1*R*Gy);     #Gy off 
  Y2: gy -> R + Gy; (k_1*gy);      #gy on
  Y3: Gy -> ry + Gy; (k2*Gy);      #ry transcription
  Y4: ry -> ; (k3*ry);             #rna degradation
  Y5: ry -> y + ry; (k4*ry);       #y translation
  Y6: y -> ; (k5*y);               #protein degradation
  
  #LacI
  L1: y + GL -> gL; (k6*y*GL);     #GL off
  L2: gL -> y + GL; (k_6*gL);      #gL on
  L3: GL -> rL + GL; (k7*GL);      #rL transcription
  L4: rL -> ; (k8*rL);             #rna degradation
  L5: rL -> L + rL; (k9*rL);       #L translation
  L6: L -> ; (k10*L);              #protein degradation
  
  #TetR
  R1: L + GR -> gR; (k16*L*GR);    #GR off
  R2: gR -> L + GR; (k_16*gR);     #gR on
  R3: GR -> rR + GR; (k17*GR);     #rR transcription
  R4: rR -> ; (k18*rR);            #rna degradation
  R5: rR -> R + rR; (k19*rR);      #R translation
  R6: R -> ; (k20*R);              #protein degradation
  
  #GFP
  F1: R + GF -> gF; (k16*R*GF);    #GF off
  F2: gF -> R + GL; (k_16*gF);     #gF on
  F3: GF -> rF + GF; (k17*GF);     #rF transcription
  F4: rF -> ; (k18*rF);            #rna degradation
  F5: rF -> F + rF; (k19*rF);      #F translation
  F6: F -> ; (k20*F);              #protein degradation
  
  
# Rate Constants:
  k1 = 0.1; k_1 = 1;              #Gy off; gy on
  k2 = 5; k3 = 0.01;               #ry transcription; ry degradation
  k4 = 1; k5 = 0.01;               #y translation; y degradation
  
  k6 = 0.1; k_6 = 1;              #GL off; gL on 
  k7 = 2; k8 = 0.01;               #rL transcription; rL degradation
  k9 = 1; k10 = 0.01;              #L translation; L degradation
  
  k11 = 0.1; k_11 = 1;            #GR off; gR on
  k12 = 3; k13 = 0.01;             #rR transcription; rR degradation
  k14 = 1; k15 = 0.01;             #R translation; R degradation
  
  k16 = 0.1; k_16 = 1;           #GF off; gF on
  k17 = 4; k18 = 0.01;             #rF transcription; rF degradation
  k19 = 1; k20 = 0.01;             #F translation; F degradation
  
# Initial Values
  gy = 0; Gy = 1; ry = 0; y = 0;   #lambdacl initial values
  gL = 0; GL = 1; rL = 0; L = 0;   #LacI initial values
  gR = 0; GR = 1; rR = 0; R = 0;   #TetR initial values
  gF = 0; GF = 1; rF = 0; F = 0;   #GFP initial values
   
''')

r.reset() 

result = r.simulate(0,5000,1000) 
r.plot(result)
