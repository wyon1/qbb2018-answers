#!/usr/bin/env python3


import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.sandbox.regression.predstd import wls_prediction_std


H3K4me1 = pd.read_csv(sys.argv[1], sep = "\t", header=None).iloc[:,5]
H3K4me3 = pd.read_csv(sys.argv[2], sep = "\t", header=None).iloc[:,5]
H3K9ac = pd.read_csv(sys.argv[3], sep = "\t", header=None).iloc[:,5]
H3K27ac = pd.read_csv(sys.argv[4], sep = "\t", header=None).iloc[:,5]
H3K27me3 = pd.read_csv(sys.argv[5], sep = "\t", header=None).iloc[:,5]
fpkm = pd.read_csv(sys.argv[6], sep = "\t", header=None)
combined_avg = pd.concat([H3K4me1, H3K27me3, H3K9ac, H3K27ac, H3K27me3, fpkm], axis=1)

#combined_avg.columns = sys.argv[1:6]


model = smf.ols(formula='fpkm ~ H3K4me1 + H3K4me3 + H3K4me3 + H3K27ac + H3K27me3', data=combined_avg)
results = model.fit()
print (results.summary())


fig, ax = plt.subplots()
ax.hist(results.resid)
ax.set_title("Residuals plot")
ax.set_xlabel("Residual points")
ax.set_xlim(left=-50, right=1000)


ax.set_ylabel("")
fig.savefig("residuals.png")
plt.close(fig)
