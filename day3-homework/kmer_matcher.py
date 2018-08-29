#!/usr/bin/env python3

import sys
import fasta


reader1 = fasta.FASTAreader(open(sys.argv[2]))
reader2 = fasta.FASTAreader(open(sys.argv[1]))
kmers = {}
target_position = []
k = int(sys.argv[3])


for ident, sequence in reader1:
	for i in range(0,len(sequence)-k):
		kmer = sequence[i:i+k]
		if kmer not in kmers:
			kmers[kmer] = [i]
		else:
			kmers[kmer].append(i)


for ident, sequence in reader2:
	count = 0
	for i in range(0,len(sequence)-k):
		kmer = sequence[i:i+k]
		if kmer not in kmers:
			continue
		else:
			if count < 1000:
				print(ident, str(i), kmer, kmers.get(kmer))



#for key in kmers:
#	print(key, kmers[key])

