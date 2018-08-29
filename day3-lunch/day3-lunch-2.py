#!/usr/bin/env python3

import sys

gene_types = {}

def num_pcg(fname):
	count = 0
	for line in open(fname):
		fields = line.rstrip("\r\n").split()
		if line.startswith("#!"):
			continue
		for i, word in enumerate(fields):
			if word == "gene_biotype":
				if fields[i+1] in gene_types:
					gene_types[fields[i+1]] = gene_types[fields[i+1]] +1
				else:
					gene_types[fields[i+1]] = 1

#		if "gene_biotype" in line:

#		if fields[17] in gene_types:
#			gene_types[fields[17]] = gene_types[fields[17]] + 1
#			count = count + 1
#		else:
#			gene_types[fields[17]] = 1

	print (gene_types)

test_output = num_pcg(sys.argv[1])