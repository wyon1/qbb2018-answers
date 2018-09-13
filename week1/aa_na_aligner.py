#!/usr/bin/env python3

import sys
import fasta
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt



dna_reader = fasta.FASTAreader(open(sys.argv[1]))
aa_reader = fasta.FASTAreader(open(sys.argv[2]))
new_seq = []


for (dna_ident, dna) , (aa_ident, aa) in zip(dna_reader, aa_reader):
	j = 0
	gaps = []
	for i in range(len(aa)):
		a = aa[i]
		if a == "-":
			gaps.append("---")
		else:
			gaps.append(dna[j:j+3])
			j += 3
	new_seq.append(gaps)

#every codon permutation
all_codons = ['---','ATT', 'ATC', 'ATA','CTT', 'CTC', 'CTA', 'CTG', 'TTA', 'TTG','GTT', 'GTC', 'GTA', 'GTG','TTT', 'TTC','ATG','TGT', 'TGC','GCT', 'GCC', 'GCA', 'GCG','GGT', 'GGC', 'GGA', 'GGG','CCT', 'CCC', 'CCA', 'CCG','ACT', 'ACC', 'ACA', 'ACG','TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC','TAT', 'TAC','TGG','CAA', 'CAG','AAT', 'AAC','CAT', 'CAC','GAA', 'GAG','GAT', 'GAC','AAA', 'AAG','CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG','TAA', 'TAG', 'TGA']

# this dictionary shows which codons encode the same AA 
SynonymousCodons = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    '---':'-', 'GA':'','GG':'','GC':'', 'G':'','A':'','C':'','T':'','GT':'','AG':'','AC':'', 'AT':'', 'AA':'', 'CT':'', 'CG':'', 'CA':'', 'CC':'', 'TT':'', 'TC':'', 'TG':'', 'TA':''}


num_of_dS = []

num_of_dN = []


for j in range(0,4850):
#	print(SynonymousCodons[new_seq[0][j]])
	for i in range(1, len(new_seq)):
		dS = 0
		dN = 0
		if new_seq[0][j] not in str(all_codons) or new_seq[i][j] not in str(all_codons):
			continue
		if new_seq[0][j] == new_seq[i][j]:
			continue
		elif SynonymousCodons[new_seq[0][j]] != SynonymousCodons[new_seq[i][j]]:
			dN += 1
		else:
			dS += 1
		num_of_dS.append(dS)
		num_of_dN.append(dN)
	else:
		continue
Dc = np.subtract(num_of_dN, num_of_dS)
mean_Dc = np.mean(Dc)
standev = np.std(Dc)
SEM = stats.sem(Dc)

z_values = []
significant = []

for i in np.nditer(Dc):
	x = abs(mean_Dc - i) / SEM
	z_values.append(x)
print (z_values)

for i in np.nditer(Dc):
	if abs(np.subtract(mean_Dc, Dc[i])) > standev:
		significant.append('1')
	else:
		significant.append('0')


"""
fig, ax = plt.subplots()

x = num_of_dS
y = num_of_dN


ax.scatter(x,y)

plt.xlabel('num_of_dS')
plt.ylabel('num_of_dN')
#plt.ylim(1, 10**5)
#plt.xlim(1, 10**5)


fig.savefig("dS_to_dN.jpg")
plt.close(fig)
#ax.set_title("Descriptive Title Here")




"""













