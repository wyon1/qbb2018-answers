#!/usr/bin/env python3

import sys
import pandas as pd
import matplotlib.pyplot as plt


f = open(sys.argv[1])
f1 = open(sys.argv[2])

read_depth = []
genotype_quality = []
allele_frequency = []

for i, line in enumerate(f):
	#one way to skip header
	if line.startswith("#"):
#		print(line)
		continue
	fields = line.rstrip("\r\n").split("\t")
	genotype_quality.append(float(fields[5]))
	shit = fields[7].split(";")
	for j in shit:
		if "DP=" in j:
			read_depth.append((j.split("=")[1]))
	for k in shit:
		if "AF=" in k:
			if "SAF=" in k:
				continue
			else:	
				allele_frequency.append((k.split("=")[1]))


#print(read_depth)
#print(genotype_quality)
#print(allele_frequency)


df = pd.read_csv(f1, sep = "\t")
col = df.columns[df.columns.str.contains('variants_effect_')]
col = col.values
coi = df.loc[:,col]



fig, (ax1, ax2, ax3, ax4) = plt.subplots(4)
ax1.hist(coi)
ax1.set_xticklabels(coi, rotation = 90)
plt.xlabel('Predicted effect')
plt.ylabel('Frequency')


ax2.hist(read_depth)

ax3.hist(genotype_quality)

ax4.hist(allele_frequency)

plt.title('')


#box = ax.get_position()
#ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])

# Put a legend to the right of the current axis
#ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), frameon = False)





fig.savefig('choices')
plt.close(fig)











