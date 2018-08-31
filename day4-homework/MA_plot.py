#!/usr/bin/env python3

"""
Usage: ./03-plot.py <ctab_file1> <ctab_file2>

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

y = fpkms1/fpkms2
x = 1/2*(fpkms1 + fpkms2)
t=np.random.rand(100)
dotcolors=[(0.2, 0.4, 0.6,a) for a in t]
ax.scatter(x, y,alpha=0.2)
plt.xlabel('average')
plt.ylabel('ratio of fpkms1 to fpkms2')
plt.title(sys.argv[1])
plt.tight_layout()

box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])

# Put a legend to the right of the current axis
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), frameon = False)


#z = np.polyfit(x, y, 1)
#f = np.poly1d(z)
#x1 = np.linspace(0,fpkms1.max())
#plt.plot(x1, f(x1))
fig.savefig("scatter.png")
plt.close(fig)
#ax.set_title("Descriptive Title Here")

