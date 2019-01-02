#!/usr/bin/env python3

import sys
import fasta
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import math

aa_reader = fasta.FASTAReader(open(sys.argv[1]))
dna_reader = fasta.FASTAReader(open(sys.argv[2]))

dic = {}
Z_test = []
diff = []

sig = []
sig_pos = []

non_sig = []
non_sig_pos = []

rel = 0


for (dna_ident, dna), (aa_ident, aa) in zip(dna_reader, aa_reader):
   j = 0
   gaps = []
   AA = []
   for i in range(len(aa)):
       AA.append(aa[i])

       if aa[i] == "-":
           gaps.append("-")
           gaps.append("-")
           gaps.append("-")
       else:
           gaps += dna[j:j+3]
           j = j + 3

   if rel == 1:
       dic[aa] = "".join(gaps)
   elif rel == 0:
       aa_seq = AA
       dna_seq = gaps

       count1=[0]*len(aa_seq)
       count2=[0]*len(aa_seq)
       rel = 1

for aa in dic:
   for i in range(len(aa)):
       if aa[i] =="-":
           continue
       elif aa[i] != aa_seq[i]:
           count1[i] = count1[i]+1
       elif dic[aa][3*i] != dna_seq[3*i] or dic[aa][3*i+1] != dna_seq[3*i+1] or dic[aa][3*i+2] != dna_seq[3*i+2]:
           count2[i] = count2[i]+1



for i in range(len(aa_seq)):
   diff.append(count1[i]-count2[i])
   x = len(aa_seq)

   Z_test.append((diff[i]-0)/((np.std(diff))/(math.sqrt(x))))



for i in range(len(aa_seq)):
   dN = count1[i]

   if count2[i] == 0:
       dS = 1
   else:
       dS = count2[i]

   if Z_test[i] > 2.58:
       sig.append(np.log2(dN/dS))
       sig_pos.append(i+1)
   else:
       non_sig.append(np.log2(dN/dS))
       non_sig_pos.append(i+1)



fig, ax = plt.subplots()

ax.scatter(sig_pos, sig, s=2, color="orange")
ax.scatter(non_sig_pos, non_sig, s=2, color="blue")

ax.set_xlabel("Condon position")
ax.set_ylabel("Z-test result")
ax.set_title("dN/dS per codon position")


fig.savefig("dS_to_dN.png")

plt.close(fig)
