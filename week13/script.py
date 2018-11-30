#!/usr/bin/env python2

import hifive
import numpy as np
import pandas as pd
import sys

hic = hifive.HiC('./normalized/normalizing.hcp')

data = hic.cis_heatmap(chrom='chr17', start=15000000, 
	stop=17500000, binsize=10000, datatype='fend', arraytype='full')



data[:, :, 1] *= np.sum(data[:, :, 0]) / np.sum(data[:, :, 1])
where = np.where(data[:, :, 1] > 0)
data[where[0], where[1], 0] /= data[where[0], where[1], 1]
data = data[:, :, 0]

#print(data)

f = pd.read_csv(sys.argv[1], sep='\t')
f_df = pd.DataFrame(f)

start = f_df.iloc[:,1]
end = f_df.iloc[:,2]
mid = np.add(end,start)
mid = np.divide (mid, 2)
mid = np.subtract (mid, 15000000)
mid = np.divide (mid, 10000)
mid_uniq = np.unique(mid)


x = np.triu_indices


for i in range(len(mid_uniq)):
   count = 0
   for j in range((i+1),len(mid_uniq)):
       row = mid_uniq[i]
       column = mid_uniq[j]
       enrichment = data[row,column]
       if enrichment >= 1:
           print("bin coordinate= " + str([i,j]) + "   " + "enrichment= " + str(enrichment))
       count = count + 1
       if count >= len(mid_uniq):
           break
