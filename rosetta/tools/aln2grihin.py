#!/usr/bin/env python
"""
Convert clustal alignment files to grishin for use in rosetta

Author: Ed van Bruggen <edvb@uw.edu>
"""

import sys
import argparse
from argparse import RawTextHelpFormatter

parser = argparse.ArgumentParser(description=__doc__, formatter_class=RawTextHelpFormatter)
parser.add_argument('--file', type=str, required=True,
                    help='input clustal alignment file')
parser.add_argument('--target', metavar='POS', type=int, default=1,
                    help='position of target protein (default: 1)')
args = parser.parse_args()

aln = open(args.file)
proteins = []

for i, line in enumerate(aln):
    if i == 0 or line == '\n' or line[0] == ' ':
        continue
    words = line.split()
    skip = 0
    for protein in proteins:
        if protein[0] == words[0]:
            protein[1] += words[1]
            skip = 1
            continue
    if not skip:
        proteins.append([words[0], words[1]])

target = proteins[args.target - 1]

for protein in proteins:
    if protein == target:
        continue
    grishin = open(target[0] + "_" + protein[0] + ".grishin", "w")
    grishin.write("## %s %s_thread\n#\nscores from program: 0\n0 %s\n0 %s\n" %
                  (target[0], protein[0], target[1], protein[1]))
