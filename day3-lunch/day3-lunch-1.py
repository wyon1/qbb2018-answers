#!/usr/bin/env python3

import sys

def num_pcg(fname):
	count = 0
	for line in open(fname):
		fields = line.rstrip("\r\n").split()
		if line.startswith("#!"):
			continue
		if "gene" in line and "protein_coding" in line:
			count = count + 1
#			print('check')
	print(count)

test_output = num_pcg(sys.argv[1])