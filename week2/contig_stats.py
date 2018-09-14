#!/usr/bin/env python3

import sys
import fasta
import numpy as np

reader1 = fasta.FASTAreader(open(sys.argv[1]))
idents = []
lengths = []
avg = []

for ident, sequence in reader1:
	idents.append(ident)

num_of_contigs = (idents[-1].split("_"))[1]
print("Number of contigs is " + num_of_contigs)


for i in range(len(idents)):
	shit = (idents[i].split("_"))
	lengths.append(int(shit[3]))
lengths = sorted(lengths)

print("Shortest contig is " + str(np.min(lengths)))
print("Longest contig is " + str(np.max(lengths)))
print("Average contig length is " + str(np.mean(lengths)))

full_length_50 = np.sum(lengths)/2


a = 0
for j in range(len(lengths)):
#	print(lengths[j])
	if a < full_length_50:
		a = a + lengths[j]
	else:
		print("N50 is " + str(lengths[j+1]))
		break
		
