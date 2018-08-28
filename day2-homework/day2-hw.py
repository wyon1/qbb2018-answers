#!/usr/bin/env python3

#Print the unique gene names from a t_data.ctab file

import sys
import numpy as np

#adds entries into the dictionary that have the FB ID as the key and UniProt as the value 
def read_fly(fname):
	IDs = {}
	for line in open(fname):
		if "DROME" in line and "FBgn" in line:
			fields = line.rstrip("\r\n").split()
			print(fields[3], "\t", fields[2])



test_output = read_fly(sys.argv[1])
