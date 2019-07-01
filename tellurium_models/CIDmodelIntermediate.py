# -*- coding: utf-8 -*-
"""
Created on Wed May 30 16:39:36 2018

@author: Joshua Ip - Work
"""

antimonyString = ("""    
    J0: $AncDNA -> AncRNANuc ; a_rna * AncDNA
    J1: $DimDNA -> DimRNANuc ; a_rna * DimDNA
    # transcription
    # units of (mRNA copies)/(sec)

    J3: AncRNANuc -> AncRNACyt ; diffusion_rna * AncRNANuc - diffusion_rna * AncRNACyt   
    J2: DimRNANuc -> DimRNACyt ; diffusion_rna * DimRNANuc - diffusion_rna * DimRNACyt
    # mRNA transport out of the nucleus into the cytoplasm
    # units of (mRNA copies)/(sec)
    
    J4: AncRNACyt -> ; d_rna * AncRNACyt
    J5: DimRNACyt -> ; d_rna * DimRNACyt
    J6: AncRNANuc -> ; d_rna * AncRNANuc
    J7: DimRNANuc -> ; d_rna * DimRNANuc
    # mRNA decay
    # units of 1/(sec) * (mRNA copies) = (mRNA copies)/(sec)

    J8: -> AncBinder ; a_nb * AncRNACyt
    J9: -> DimBinder ; a_nb * DimRNACyt
    # translation
    # units of (protein copies)/(sec * mRNA copies) * (mRNA copies) = (protein copies / sec)

        
    J10: AncBinder -> ; d_nb * AncBinder
    J11: DimBinder -> ; d_nb * DimBinder
    J12: DimerCyt -> ; d_nb * DimerCyt
    J13: DimerNuc -> ; d_nb * DimerNuc
    # protein decay
    # units of (1 / sec) * (protein copies) = (protein copies / sec)
    
    J14: Mol + AncBinder -> Complex ;  k_on_anchor_binder * Mol * AncBinder -  k_off_anchor_binder * Complex
    # the anchor binder binds to molecule of interest to form a complex.
    # nanobody complexes may dissociate over time
    # units for forward reaction: (1 / (mols / liter) * sec) / (copies / mol)  / liters * copies * copies = copies / sec
    # units for backwards reaction: (1 / sec) * copies = copies / sec

    J15: Complex + DimBinder -> DimerCyt ; k_on_dimerization_binder * DimBinder * Complex - k_off_dimerization_binder * DimerCyt
    # dimerization binder binds to complex to form dimers       
    # dimers may dissociate, but much less often than complexes
    # units for forward reaction: (1 / (mols / liter) * sec) / (copies / mol)  / liters * copies * copies = copies / sec
    # units for backwards reaction: (1 / sec) * copies = copies / sec
    
    J16: DimerCyt -> DimerNuc; diffusion_nb * DimerCyt 
    J17: DimerNuc -> DimerCyt; diffusion_nb * DimerNuc
    # dimer must be transported into the cell to act as a transcription factor
    
    J18: DimerNuc + GeneOff -> GeneOn; k_on_transcription_factor * DimerNuc * GeneOff - k_off_transcription_factor * GeneOn
    # dimer acts as transcription factor for a gene
    # units: (copies) / (copies)
    
    J19: -> RepRNANuc ; a_rna * GeneOn
    J20: RepRNANuc -> RepRNACyt ; diffusion_rna * RepRNANuc - diffusion_rna * RepRNACyt
    J22: RepRNANuc -> ; d_rna * RepRNANuc
    J23: RepRNACyt -> ; d_rna * RepRNACyt
    J24: -> Rep ; a_nb * RepRNACyt
    J25: Rep -> ; d_nb * Rep
    # the activated gene transcribes a reporter
    
    # *****************************************************************************************************************************
    # Parameters
    
    AvoNum = 6.02 * 10^23;
    
    TotalCellVol = 30.3 * 10^(-6);
    NucleusVol = 4.3 * 10^(-6);
    CytoplasmVol = TotalCellVol - NucleusVol;
    # all volumes given in units of L, 
    # volumes from http://bionumbers.hms.harvard.edu/bionumber.aspx?id=106557&ver=1&trm=yeast%20cytoplasm%20volume&org=
    
    scalingFactor = 60 * 60;
    # since all our rates/rate constants are in seconds, we can scale time by multiplying each time-dependent parameter by a scaling factor
    # this particular value scales the parameters for time units of hours
    
    a_rna = (0.002) * scalingFactor;
    # median transcription rate = 0.12 mRNA molecules/min = 0.002 mRNA molecules/sec
    # median transcription rate from http://bionumbers.hms.harvard.edu/bionumber.aspx?id=106766&ver=3&trm=transcription%20rate%20yeast&org=
    # KEY ASSUMPTION: the rate of transcription of our nanobody gene is constant. 
    # in reality, it may not be safe to assume that our molecule is transcribed by the median transcription rate
    
    d_rna = 5.6 * 10^(-4) * scalingFactor;        
    # 5.6 * 10 ^ -4 = mRNA decay rate constant in units of sec^-1
    # mRNA decay constant found from http://bionumbers.hms.harvard.edu/bionumber.aspx?id=105510&ver=5&trm=mrna%20s.%20cerevisiae&org=
    
    a_nb = (0.0185) * scalingFactor;
    # yeast has no rough ER, so translation occurs in the cytoplasm
    # median time for translation initiation = 4.0 * 10^2 s * mRNA / protein
    # median elongation rate = 9.5 aa/s
    # nanobody average amino acids = 130 aa
    # time for elongation = (130 aa / protein)/(9.5 aa/s) = 14 sec / protein
    # total time for 1 mRNA transcript = 14 sec / protein + 40 sec = 54 sec
    # rate at which mRNA is transcribed = 1 protein/(54 sec * 1 mRNA) / ~ 0.0185 protein/(sec mRNA)
    # it is notable that translation initiation rate can vary between mRNA by orders of magnitude
    # all data from https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3694300/

    d_nb = 2.6 * 10^(-4) * scalingFactor;
    # which shows that the median half-life of a protein in a budding yeast cell is 43 minutes
    # median rate constant of degradation of proteins in a yeast cell = 2.6e-4 1/sec
    # data from http://www.pnas.org/content/103/35/13004 (doi: https://doi.org/10.1073/pnas.0605420103) https://www.nature.com/articles/nature10098,
    
    k_on_anchor_binder = 4.0 * 10^5 * scalingFactor;
    k_off_anchor_binder = 80 * 10^(-1) *scalingFactor;
    # k_on of antibody-binding to cytochrome C = (4.0 +- 0.3) * 10^5 1/(M * sec)
    # From gu's data, K_d of anchor binder binding = 20 * 10^-6, units of M
    # K_d = k_off / k_on, therefore k_off = K_d * k_on
    # 4.0 * 10^5 1/(M * sec) * (20 * 10^-6 M) = 80 * 10^-1 (sec^-1)
    # this is one of the binding affinities that we will do a parameter sweep to learn more about
    
    k_on_dimerization_binder = 4.0 * 10^5 * scalingFactor;
    k_off_dimerization_binder = 400 * 10^(-1) * scalingFactor;
    # k_on of antibody-binding to cytochrome C = (4.0 +- 0.3) * 10^5, units of 1/(M * sec)
    # from Gu's data, K_d of dimerization binder binding = 100 * 10^-9, units of M
    # K_d = k_off / k_on, therefore k_off = K_d * k_on
    # 4.0 * 10^5 1/(M * sec) * (100 * 10^-6 M) = 400 * 10^-1 (sec^-1)
    # this is one of the binding affinities that we will do a parameter sweep to learn more about
        
    k_on_transcription_factor = 1.0 * 10^9 * scalingFactor;
    k_off_transcription_factor = 1.11 * 10^(-3) * scalingFactor;
    # k_on of Egr1 DNA binding domain =  1.0 * 10^9, units of 1/(sec * M)
    # k_off of EGr1 DNA binding domain = 1.11 * 10^-3, units of 1/sec
    # data from http://bionumbers.hms.harvard.edu/bionumber.aspx?s=n&v=5&id=104597

    
    diffusion_rna = 1;
    diffusion_nb = 3;
    # Where do we get this?
    
    # *****************************************************************************************************************************************
    # Initial values
    # These are all in copies
    AncDNA = 1; 
    DimDNA = 1;
    Mol = 0;
    GeneOff = 1;
    Setting = 50;
    
    
    at time>=4: Mol=Setting;
    

    
""");