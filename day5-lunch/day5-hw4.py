#!/usr/bin/env python3


import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as sm
from statsmodels.sandbox.regression.predstd import wls_prediction_std

avg_H3K4me1 = pd.read_csv(sys.argv[1], sep = "\t").iloc[:,5]
avg_H3K4me3 = pd.read_csv(sys.argv[2], sep = "\t").iloc[:,5]
avg_H3K9ac = pd.read_csv(sys.argv[3], sep = "\t").iloc[:,5]
avg_H3K27ac = pd.read_csv(sys.argv[4], sep = "\t").iloc[:,5]
avg_H3K27me3 = pd.read_csv(sys.argv[5], sep = "\t").iloc[:,5]

combined_avg = pd.concat([avg_H3K4me1, avg_H3K27me3, avg_H3K9ac, avg_H3K27ac, avg_H3K27me3], axis=1)
#print(combined_avg)

model = sm.OLS(pd.read_csv(sys.argv[6]),combined_avg)
results = model.fit()
print(results.summary())