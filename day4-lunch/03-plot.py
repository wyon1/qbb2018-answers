#!/usr/bin/env python3

"""
Usage: ./03-plot.py <ctab_file>

"""

import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

tx_fpkms1 = []
tx_fpkms2 = []


fpkms1 = pd.read_csv(sys.argv[1], sep = "\t", index_col = "t_name").loc[:,"FPKM"]
fpkms2 = pd.read_csv(sys.argv[2], sep = "\t", index_col = "t_name").loc[:,"FPKM"]


fig, ax = plt.subplots()

x = fpkms1
y = fpkms2
t=np.random.rand(100)
dotcolors=[(0.2, 0.4, 0.6,a) for a in t]
ax.scatter(x, y,alpha=0.2)
ax.set_yscale('log')
ax.set_xscale('log')
plt.xlabel(sys.argv[1])
plt.ylabel(sys.argv[2])
plt.ylim(1, 10**5)
plt.xlim(1, 10**5)



z = np.polyfit(x, y, 1)
f = np.poly1d(z)
x1 = np.linspace(0,fpkms1.max())
plt.plot(x1, f(x1))

fig.savefig("scatter.png")
plt.close(fig)
#ax.set_title("Descriptive Title Here")

