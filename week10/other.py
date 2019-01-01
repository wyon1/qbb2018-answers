#!/usr/bin/env python3

"""
./clustering.py <hema_data.txt>
"""

import sys
from matplotlib import pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
import pandas as pd
from sklearn import datasets
from scipy.stats import ttest_ind

file = open(sys.argv[1])

header = file.readline()
genes = []


for line in file:
   fields = line.split()
   genes.append(fields[0])

"""
f = pd.read_csv(sys.argv[1], delim_whitespace=True, index_col="gene")
f_df = pd.DataFrame(f)

#print(f_df)

k_means = KMeans(n_clusters = 4)
k_means.fit(f_df)
y_k_means = k_means.predict(f_df)

#print(y_k_means)

fig = plt.figure()
plt.title("K-means")
plt.scatter(f_df["CFU"], f_df["poly"], c = y_k_means, s = 1)

plt.xlabel("CFU")
plt.ylabel("Poly")
plt.savefig("k_means.png")
plt.close(fig)
"""

f = pd.read_csv(sys.argv[1], delim_whitespace=True, header=0, index_col="gene").loc[:, ("CFU", "mys", "poly", "unk")].dropna()
f_df = pd.DataFrame(f)

early = ["CFU", "mys"]
late = ["poly", "unk"]

t_stat, p_val = ttest_ind(f_df[early], f_df[late], axis = 1)
f_df["p_value"] = p_val

f_df = f_df.mask(f_df["p_value"] > 0.05).dropna(how = "any").sort_values ("p_value")
#print(f_df.ix[:,4].to_csv(sep="\t"))
print(f_df.index)
