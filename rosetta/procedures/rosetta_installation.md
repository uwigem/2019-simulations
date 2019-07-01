# Installing PyRosetta

1. Download PyRosetta from: https://els.comotion.uw.edu/express_license_technologies/pyrosetta
   - Under "Academic License" click the "License" button
   - Fill out the required information and click "Execute License"
   - Wait for email with download link and login information
   - From download link choose your OS and python version (python 3.5
     recommended), then the latest version of PyRosetta
2. Unpack downloaded file
3. `cd` into generated folder
4. `cd setup`
5. `python setup.py install`
6. To test to make sure PyRosetta installed corrected open python and type
   `import pyrosetta` and then `pyrosetta.init()`

# Installing Rosetta on Windows via Ubuntu VM

Installing linux + vmware:
1. VMWare: https://www.virtualbox.org/wiki/Downloads
1. Linux iso file: https://www.ubuntu.com/download/desktop
1. Install VMWare, click on the blue "New" button
1. Choose Linux and Ubuntu, if your computer is 64 bit and you don't have the option to select 64 bit, follow the next few steps
    - Make sure your computer's motherboard supports virtualization
    - Turn off your computer
    - Turn on your computer and enter BIOS (your computer should have something that pops up saying "Press F# for boot options")
    - Turn on Virtualization. This may be called "SVM" or so in some.
    - Laptops should have this automatically. Don't be scared of this step, it's not too hard to do and it does not mess your computer up.
    - There should be an option to reboot or "Save and reset". Select one of those
1. Choose the 64 bit version of ubuntu, then partition the recommended off Linux's website, or more if you know what you're doing
1. Let it set up, then run it
1. Select the iso file you downloaded from step 2. (Make sure it's somewhere where you want to keep it, because you cannot move or delete this file!)
1. Install stuff and you're good

Initial stuff for setting up rosetta
1. `sudo apt-get install g++`
1. `sudo apt-get install scons`
1. Install rosetta
  - Request academic license: https://els.comotion.uw.edu/licenses/86
  - Compile and install following instructions here: https://www.rosettacommons.org/demos/latest/tutorials/install_build/install_build

Build debug:

`cannot find -lz`
1. `sudo apt-get install build-essential`
1. `sudo apt-get install lib32z1-dev`

`cannot find libsqlite3.so`
1. `sudo apt-get install libsqlite3-dev`

Running rosetta with input_nanobody on google drive + AbinitioRelax
1. For reference, my file locations are as follows:
`~/Desktop/rosetta_src_2018.09.60072_bundle/main/source/bin/AbinitioRelax.linuxgccrelease`
`~/Desktop/input_nanobody/input_nanobody/options_nanobody` (yes, folder in folder named same)
    - You can see where the files I downloaded are placed according to these file paths.

1. input_nanobody downloaded from the google drive here: https://drive.google.com/drive/u/1/folders/1XzeTnlVV9BWhBCocvYo9fyQhFPLS4KwS

1. Modified the options_nanobody file to have the file locations reference the correct file in relation to where the AbinitioRelax is. (NOTE: TILDE (~) DOES NOT WORK!)

1. Went into the `~/Desktop/rosetta_src_2018.09.60072_bundle/main/source/bin/` directory and ran the following command:

1. `./AbinitioRelax.linuxgccrelease @ /home/william/Desktop/input_nanobody/input_nanobody/options_nanobody` (Note the space after @ is important and makes it run an error if it isn't there).

Run time: 8 minutes, 1 core at ~3.9 GHz (Ryzen 1700), 3 pdb files
