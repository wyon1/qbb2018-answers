#!/usr/bin/env python3

"""
Usage: ./02-merge.py <FPKM threshold> <sample1/t_data.ctab> <sample2/t_data.ctab> ... <sample_n/t_data.ctab> 

Create csv file with FPKMs from n samples, but only for ones above your set threshold
"""

import sys
import os
import pandas as pd
import matplotlib.pyplot as plt




for i,file in enumerate(sys.argv[2:]):
	print ("loading "+file)
	if i==0:
		print ("loading "+file)
		total_fpkms = pd.read_csv(file, sep = "\t", index_col = "t_name").loc[:,"FPKM"]
	else:
		total_fpkms += pd.read_csv(file, sep = "\t", index_col = "t_name").loc[:,"FPKM"]

roi = total_fpkms > float(sys.argv[1])
print(total_fpkms.loc[roi])



"""

while i < sys.argv[1]
fpkms1 = pd.read_csv(sys.argv[2], sep = "\t", index_col = "t_name").loc[:,"FPKM"]
fpkms2 = pd.read_csv(sys.argv[2], sep = "\t", index_col = "t_name").loc[:,"FPKM"]

total_fpkms = fpkms1 + fpkms2 
roi = total_fpkms > float(sys.argv[3])
print(total_fpkms.loc[roi].index)
"""

"""
fig, ax = plt.subplots()
ax.scatter(total_fpkms)


fig.savefig("scatter.png")
plt.close(fig)
#ax.set_title("Descriptive Title Here")

"""