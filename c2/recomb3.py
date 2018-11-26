#!/usr/bin/env python3
""" """

import os
import sys
from itertools import product, chain

args = sys.argv[1:]

if len(args) != 1:
	print('Usage: {} NUM_GENES'.format(os.path.basename(sys.argv[0])))
	sys.exit(1)

if not args[0].isdigit():
	print('"{}" does not look like an integer'.format(args[0]))
	sys.exit(1)

num_genes = int(args[0])
if not 2 <= num_genes <= 10:
	print('NUM_GENES must be greater than 1, less than 10')
	sys.exit(1)

def gen(prefix):
	return [prefix + str(n + 1) for n in range(0, num_genes)]

promotors = gen('P')
coding = gen('C')
terminators = gen('T')

print('N = "{}"'.format(num_genes))
for i, combo in enumerate(product(promotors, coding, terminators)):
	print('{:3}: {}'.format(i + 1, combo))
