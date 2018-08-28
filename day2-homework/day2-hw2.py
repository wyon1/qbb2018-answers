#!/usr/bin/env python3



import sys
import numpy as np

ID = {}

#adds entries into the dictionary that have the FB ID as the key and UniProt as the value 
def read_fly(fname): 
	for line in open(fname):
		if "DROME" in line and "FBgn" in line:
			fields = line.rstrip("\r\n").split()
			ID[fields[3]] = fields[2]


#checks to see if the FB ID is in the line of the file and prints out the Uniprot ID followed by the gene's line
def mapping(fname):
	for line in open(fname):
		if "FBgn" in line:
			fields = line.rstrip("\r\n").split()
			if fields[8] in ID.keys():
				print(ID[fields[8]], "\t", line)



test_output1 = read_fly(sys.argv[1])
test_output2 = mapping(sys.argv[2])
