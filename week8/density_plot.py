#!/usr/bin/env python3

"""
script.py that_janky_file_we_made.txt
"""

import sys
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math
from collections import Counter

f = pd.read_csv(sys.argv[1], delim_whitespace=True, header=None)
f_df = pd.DataFrame(f)
f_df1 = f_df.iloc[:,2]
list_start = f_df1.values.tolist()
#print(list_start)


f_df2 = f_df.iloc[:,0]
list_range = f_df2.values.tolist()
sequence_range = []
for i in range(len(list_range)):
	x = list_range[i].split(":")
	y = x[1].split('-')
	z = int(y[1])-int(y[0])
	sequence_range.append(str(z))


a = np.array(list_start, dtype=np.float)
b = np.array(sequence_range, dtype=np.float)
c = np.divide(a,b)
d = []
for i in range(len(c)):
	d.append(round(c[i],2))

#print(Counter(d))

fig, ax = plt.subplots()

ax.hist(d)
plt.yticks(range(0,21, 2))
#plt.xticks(range(0, float(1.01), float(0.05)))
plt.xlabel('Relative start position')
plt.ylabel('Frequency')


plt.title('Density plot for relative motif start site')


fig.savefig('test')
plt.close(fig)


