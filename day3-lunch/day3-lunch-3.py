#!/usr/bin/env python3

import sys

def num_pcg(fname, j, k):
	count = 0
	for line in open(fname):
		fields = line.rstrip("\r\n").split()
		if line.startswith("#!"):
			continue
		if "gene" in fields[2] and "biotype" in line:
			for i, word in enumerate(fields):
				if word == "gene_id":
					name.append(fields[i+1])
					start.append(fields[3])
					end.append(fields[4])
					chromosome.append(fields[0])
					for x, boo in enumerate(fields):
						if "biotype" in boo:
							kind.append(fields[x+1])


	for i in range(len(start)):
		if chromosome[i] == roi:
			a = poi - int(start[i])
			b = poi - int(end[i])
			if abs(a) <= abs(b):
				distance.append(a)
			else:
				distance.append(b)

	for i in range(len(distance)):
		if kind[i] == "protein_coding":
			continue
		if abs(distance[i]) <= abs(j):
			j = (distance[i])
			k = i
#	print ("Closest non-protein coding gene is " + name[i])
	print (j)

	for i in range(len(distance)):
		if kind[i] != "protein_coding":
			continue
		if abs(distance[i]) <= abs(j):
			j = (distance[i])
			k = i
#	print ("Closest protein coding gene is " + name[i])
	print (j)
#	print(kind)










#	print (distance)
#	print (name)
#	print(start)
#	print(end)
#	print(chromosome)
#	print(kind)



	





name = []
start = []
end = []
kind = []
chromosome = []
roi = "3R"
poi = int(21378950)
distance = []
j = 99999999999999999
k = 0
test_output = num_pcg(sys.argv[1], j, k)






