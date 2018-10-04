#!/usr/bin/env python3

import sys
import matplotlib.pyplot as plt

f = open(sys.argv[1])

PC1 = []
PC2 = []

for i,line in enumerate(f):
	fields = line.split()
	PC1.append(float(fields[2]))
	PC2.append(float(fields[3]))


PC1_min = min(PC1)
PC1_max = max(PC1)
PC2_min = min(PC2)
PC2_max = max(PC2)


fig, ax = plt.subplots()

plt.scatter(PC1, PC2, marker = ".")
#Move left y-axis and bottim x-axis to centre, passing through (0,0)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

# Eliminate upper and right axes
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# Show ticks in the left and lower axes only
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.xlim(PC1_min*1.1, PC1_max*1.1)
plt.ylim(PC2_min*1.1, PC2_max*1.1)

plt.xticks([PC1_min, PC1_max])
plt.yticks([PC2_min, PC2_max])

fig.savefig("scatter.png")
plt.close(fig)
ax.set_title("PC2 vs. PC1")
