#!/usr/bin/env python3



import sys
import numpy as np

ID = {}

#IMPORTANT
# IF YOU WANT TO PRINT EMPTY SPACES FOR  UNKNOWN GENES, TYPE 'a' AS FOURTH ARGUMENT
# IF YOU WANT TO SKIP UNKNOWN GENES, TYPE 'b' AS FOURTH ARGUMENT



#adds entries into the dictionary that have the FB ID as the key and UniProt as the value 
def read_fly(fname): 
	for line in open(fname):
		if "DROME" in line and "FBgn" in line:
			fields = line.rstrip("\r\n").split()
			ID[fields[3]] = fields[2]


#checks to see if the FB ID is in the line of the file and prints out the Uniprot ID followed by the gene's line
def mapping(fname):
	for line in open(fname):
		count = 0
		if "FBgn" in line:
			fields = line.rstrip("\r\n").split()
			if fields[8] in ID.keys():
 				if count < 100:
 				 	if sys.argv[3] == "a":
 				 		print("unknown", "\t", line)
 				 		count = count + 1
 				 	if sys.argv[3] == "b":
 				 		print(ID[fields[8]], "\t", line)
 				 		count = count + 1






test_output1 = read_fly(sys.argv[1])
test_output2 = mapping(sys.argv[2])
