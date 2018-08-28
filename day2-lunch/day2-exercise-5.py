#!/usr/bin/env python3

import sys

if len(sys.argv) > 1:
	f = open(sys.argv[1])
else:
	f = sys.stdin

#for i in range(10):
 #   print(f.readline().rstrip)
count = 0
full = 0
for i, line in enumerate(f):
	#one way to skip header
		fields = line.rstrip("\r\n").split("\t")
		if fields[1].startswith("@"):
			continue
		if fields[1].startswith("*"):
			continue
		if len(fields) < 12:
			continue
		else:
			count += 1
			full = full + int(fields[4])
print(full/count)