#!/usr/bin/env python3

import sys
import matplotlib.pyplot as plt

f = open(sys.argv[1])
AF = []

for line in f:
	if line.startswith('#'):
		continue
	fields = line.split()
	x = fields[7].split('=')
	AF.append(float(x[1].split(',')[0]))



fig, ax = plt.subplots()

plt.hist(AF, bins = 100)

plt.xlabel("Allele Frequency")
plt.ylabel("Count")

fig.savefig("Allele_Freq.png")
plt.close(fig)