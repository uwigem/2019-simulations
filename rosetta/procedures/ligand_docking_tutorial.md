# Ligand Docking in Rosetta

Ligand docking is a simulation in Rosetta that allows you to take a protein along with a ligand (some small molecule) and simulate the ligand docking to the protein. For iGEM, the purposes of using this protocal is to dock our ligand ``molx`` with the anchor nanobody.

As a reference, [this](https://www.rosettacommons.org/demos/latest/tutorials/ligand_docking/ligand_docking_tutorial) is the official Rosetta guide for ligand docking. Our guide will be similar, but geared towards the molecules we are working with.

---

## Prepping Files

In order to run ligand docking, you will need the files listed below.

    - pdb of the anchor nanobody
    - pdb of molx
    - pdb of molx in anchor nanobody binding spot
    - conformer file for molx
    - params file of molx
    - dock.xml
    - options file for rosetta script

#### Get pdb files

In order to get pdb of molx and the anchor nanobody, we used homology modeling. Please refer to our RosettaCM guide. 

For the pdb of molx inside the anchor nanobody, the following steps were taken:

1. Use ``cat anchor.pdb molx.pdb > anchor-molx.pdb`` in order to concatenate the two pdb files together.
2. Open ``pymol anchor-molx.pdb`` 
3. Inside pymol, manually move the molx molecule to be somewhere near the predicted docking site. 
4. Save changes to the pdb.

#### Conformer file

The ``anchor-molx.pdb`` only has one conformation of molx. Therefore, in order to get a more accurate simulate, a conformer file is needed to provide Rosetta with various other conformations of molx.

The conformer file can be generated with a program called [OpenBable](http://openbabel.org/wiki/Main_Page). Use command:

`obabel molx.pdb  -O molx_confs.pdb --confab --conf 1000 —writeconformer`

to generate a conformation file for molx named ``molx_confs.pdb``.

### Params File

The params files contains necessary information that Rosetta needs in order to process the ligand. To generate this file, follow the instructions below:

1. Download a pdb file of the ligand. One place to search is the [RCSB](http://www.rcsb.org/pdb/ligand/chemAdvSearch.do) database.
2. Convert pdb to a mol2 file with hydrogen:
    a. Use [phenix.reduce](https://www.phenix-online.org/documentation/reference/hydrogens.html) to add hydrogens to the pdb file.
    b. Use OpenBabal to convert the pdb to mol2 file type.
3. Convert the mol2 to Rosetta format. Use a rosetta script to do this (location may vary on your device):

``python ~/Rosetta/main/source/scrips/python/apps/public/molfile_to_params.py --keep-names molx.mol2 -p molx -n molx --conformers-in-one-file molx_confs.pdb``

### Dock XML

The dock.xml file tells the Rosetta Script what movers it needs to use. We used the following file:

```xml
<ROSETTASCRIPTS>

        <SCOREFXNS>
                <ScoreFunction name="ligand_soft_rep" weights="ligand_soft_rep">
                </ScoreFunction>
                <ScoreFunction name="hard_rep" weights="ligand">
                </ScoreFunction>
        </SCOREFXNS>

        <LIGAND_AREAS>
                <LigandArea name="inhibitor_dock_sc" chain="X" cutoff="6.0" add_nbr_radius="true" all_atom_mode="false"/>
                <LigandArea name="inhibitor_final_sc" chain="X" cutoff="6.0" add_nbr_radius="true" all_atom_mode="false"/>
                <LigandArea name="inhibitor_final_bb" chain="X" cutoff="7.0" add_nbr_radius="false" all_atom_mode="true" Calpha_restraints="0.3"/>
        </LIGAND_AREAS>

        <INTERFACE_BUILDERS>
                <InterfaceBuilder name="side_chain_for_docking" ligand_areas="inhibitor_dock_sc"/>
                <InterfaceBuilder name="side_chain_for_final" ligand_areas="inhibitor_final_sc"/>
                <InterfaceBuilder name="backbone" ligand_areas="inhibitor_final_bb" extension_window="3"/>
        </INTERFACE_BUILDERS>

        <MOVEMAP_BUILDERS>
                <MoveMapBuilder name="docking" sc_interface="side_chain_for_docking" minimize_water="false"/>
                <MoveMapBuilder name="final" sc_interface="side_chain_for_final" bb_interface="backbone" minimize_water="false"/>
        </MOVEMAP_BUILDERS>

        <SCORINGGRIDS ligand_chain="X" width="18">
                <ClassicGrid grid_name="classic" weight="1.0"/>
        </SCORINGGRIDS>

        <MOVERS>
                <Transform name="transform" chain="X" box_size="7.0" move_distance="0.2" angle="20" cycles="500" repeats="1" temperature="5"/>
                <HighResDocker name="high_res_docker" cycles="6" repack_every_Nth="3" scorefxn="ligand_soft_rep" movemap_builder="docking"/>
                <FinalMinimizer name="final" scorefxn="hard_rep" movemap_builder="final"/>
                <InterfaceScoreCalculator name="add_scores" chains="X" scorefxn="hard_rep" />
        </MOVERS>

        <PROTOCOLS>
                <Add mover_name="transform"/>
                <Add mover_name="high_res_docker"/>
                <Add mover_name="final"/>
                <Add mover_name="add_scores"/>
        </PROTOCOLS>

</ROSETTASCRIPTS>
```

### Options File

The options file gives command line options the the rosetta script that runs the simulations. These are our specifications:

```bash
-in:file:s anchor-molx.pdb

-in:file:extra_res_fa molx.params

-packing
        -ex1
        -ex2
        -no_optH false
        -flip_HNQ true
        -ignore_ligand_chi true

-parser
        -protocol dock.xml

-mistakes
        -restore_pre_talaris_2013_behavior true
-nstruct 1
```

Note that the ``-in:file:`` options should be edited to match the correct filename. Use ``-nstruct`` to specify how many structures Rosetta should generate. 

## Run the simulation

To run the simulation, use ``rosetta_scripts`` protocol located in the bin file and pass in the options file:

``Rosetta/main/source/bin/rosetta_scripts.linuxgccrelease @options``

## Analyze results

Rosetta will generate pdb files of the docked ligand. It will also generate a score file which contains the energies of all the generated models. The lower the energy, the better fit the model is. You can use:

``cat score.sc | sort -nk2 > scores_sorted.txt``

This will create a new txt file called ``scores_sorted.txt`` which contains all the entries shorted (lowest on top).

