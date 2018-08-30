#!/usr/bin/env python3

"""
Usage: ./02-merge.py <sample list.csv> <~/data/results/stringtie> 

Create csv file with FPKMs from n samples, but only for ones above your set threshold
"""

import sys
import os
import pandas as pd
import matplotlib.pyplot as plt

d = {	

}

df = pd.read_csv(sys.argv[1])

for index, sample, sex, stage in df.itertuples():
	filename = os.path.join(sys.argv[2], sample, "t_data.ctab")
	ctab_df = pd.read_table(filename, index_col = "t_name")
	fpkm = ctab_df.loc[:, "FPKM"]
	header = "{0}_{1}".format(sex, stage)
	d[header] = fpkm

fpkm_df = pd.DataFrame(d)
fpkm_df.to_csv(sys.stdout, sep="\t")
"""
for i,file in enumerate(sys.argv[1:]):
	if i==0:
		total_fpkms = pd.read_csv(file, sep = "\t", index_col = "t_name").loc[:,"FPKM"]
	else:
		total_fpkms += pd.read_csv(file, sep = "\t", index_col = "t_name").loc[:,"FPKM"]

roi = total_fpkms
print(total_fpkms.loc[roi])
"""
"""

d = {
	'first': ctab1,
	'second': ctab2
}

df = pd.DataFrame(d)
df.to_csv(sys.stdout)
"""
