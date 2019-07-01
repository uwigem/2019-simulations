#!/bin/bash

~/Downloads/rosetta_src_2018.33.60351_bundle/main/source/bin/rosetta_scripts.default.linuxgccrelease \
	-database ~/Downloads/rosetta_src_2018.33.60351_bundle/main/database \
	-s ~/Downloads/NewDockProtocol/ConcatenatedPDBs/S_MOL_0X.pdb \
	-in:file:extra_res_fa ~/Downloads/NewDockProtocol/CBD.params \
	-parser:protocol dock.xml \
	-beta_cart \
	-overwrite \
	-in::file::load_PDB_components false \
	-nstruct 10
