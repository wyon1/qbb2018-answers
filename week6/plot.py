#!/usr/bin/env python3

import sys
import matplotlib.pyplot as plt
import numpy as np

differences = 0
promoter_range =[]
exon_range = []
intron_range = []

promoter = 0
exon = 0
intron = 0


for line in open(sys.argv[1]):
	fields=line.rstrip("\n").split("\t")
	if fields[3] == "promoter":
		for x in range(int(fields[1]),int(fields[2])):
			promoter_range.append(x)
	elif fields[3] == "exon":
		for x in range(int(fields[1]),int(fields[2])):
			exon_range.append(x)
	else:
		for x in range(int(fields[1]),int(fields[2])):
			intron_range.append(x)



for line in open(sys.argv[2]):
	fields=line.rstrip("\n").split("\t")
	if fields[6] != fields[5]:
		differences+=1
print(differences)
for line in open(sys.argv[2]):
	fields=line.rstrip("\n").split("\t")
	if int(fields[1])+1 in promoter_range:
		promoter+=1
	elif int(fields[1])+1 in exon_range:
		exon+=1
	else:
		intron+=1

fig, (ax1, ax2) = plt.subplots(ncols=2)

ax1.set_title("# of changed sites in each type of region")
pie_labels = ["Promoter", "Exon", "Intron"]
pie = ax1.pie([promoter, exon, intron], labels=pie_labels)
fig.savefig("clean_pie.png")                 # Save the figure 
plt.close(fig)                               # Close the canvas

ax2.set_title("# of sites lost/gained")
ax2.bar(0,1466)

fig.savefig("clean_pie.png")                 # Save the figure 
plt.close(fig)                               # Close the canvas