#!/bin/bash

# Edit the docked ligand and anchor binder pdb so that the ligand and the protein are on a single chain.
# This is necessary, otherwise the 
sed "s/CBD X/CBD A/g" S_MOL_DOCKED.pdb > S_COMPLEX_SINGLE_CHAIN.pdb \

# Edit the dimerization binder such that it is on a different chain than the ligand and the anchor binder
# Rosetta will try to dock proteins of different chains, but it doesn't matter what particular unique letter we use for each chain
sed "s/ A / B /g" S_DIM_BINDER.pdb > S_DIM_BINDER_UNIQUE_CHAIN.pdb \

# Concatenate both chains into one file so that we can pack it
cat S_DIM_BINDER_UNIQUE_CHAIN.pdb S_COMPLEX_SINGLE_CHAIN.pdb > S_DOCKING_UNPACKED.pdb \


sed "/ATOM\|HETATM\|CONECT/!d" S_DOCKING_UNPACKED.pdb > S_DOCKING_EXTRA_LINES_REMOVED.pdb \

# 
#~/Documents/iGEM/labjournal/rosetta/models/molx/S_MOL_SINGLE_CHAIN.pdb \

#~/Downloads/rosetta_src_2018.33.60351_bundle/main/source/bin/relax.default.linuxgccrelease \
#	-s S_DOCKING_EXTRA_LINES_REMOVED.pdb \
#	-out 
#	-in:file:extra_res_fa CBD.params \
#	-beta_cart \
#
mv score.sc score_packing.sc
mv S_DOCKING_EXTRA_LINES_REMOVED_0001.pdb S_DOCKING_PACKED.pdb
sed "/ATOM\|HETATM\|CONECT/!d" S_DOCKING_PACKED.pdb > S_DOCKING_PACKED_EXTRA_LINES_REMOVED.pdb \

~/Downloads/rosetta_src_2018.33.60351_bundle/main/source/bin/docking_protocol.default.linuxgccrelease \
	-s S_DOCKING_PACKED_EXTRA_LINES_REMOVED.pdb \
	-in:file:extra_res_fa CBD.params \
	-database ~/Downloads/rosetta_src_2018.33.60351_bundle/main/database \
	-nstruct 10000 \
	-beta_cart \
	-ex1 \
	-ex2aro \
	-randomize2 \

mv score.sc score_docking_01.sc

