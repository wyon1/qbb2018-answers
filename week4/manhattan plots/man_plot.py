#!/usr/bin/env python3
"""

Usage: ./05-week4.py <plink.X.qassoc> <X_position_condition>

"""
import sys
import numpy as np
import matplotlib.pyplot as plt
        

chrom = []
p_value = []


for line in open(sys.argv[1]):
    if "SNP" in line or "NA" in line:
        continue
    else:
        fields = line.rstrip("\r\n").split()
        a = -np.log(float(fields[8]))
        b = fields[0]

        chrom.append(b)
        p_value.append(a)

        
fig, ax = plt.subplots()
ax.scatter(chrom, p_value, s = 1.5)
plt.axhline(y=-np.log(10e-5), linewidth = 2, color = "red")
ax.set_ylabel('P-value')
ax.set_xlabel('SNPs for chrom')
ax.set_title(sys.argv[2] + " condition")
fig.savefig(sys.argv[2] + '.png', dpi=600)
plt.close()