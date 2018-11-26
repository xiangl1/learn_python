#!/usr/bin/env python3


import os
import sys

args = sys.argv[1:]

if len(args) != 1:
	print('Usage: {} DNA'.format(os.path.basename(sys.argv[0])))
	sys.exit(1)

dna = args[0]

count = {}

for base in dna.lower():
	if not base in count:
		count[base] = 0

	count[base] += 1

counts = []
for base in "acgt":
	num = count.get(base, 0)
	counts.append(str(num))

print(' '.join(counts))
