#!/usr/bin/env python3

"""dictionary lookup"""

import os
import sys

args = sys.argv[1:]

if len(args) != 1:
	print('Usage: {} LETTER'.format(os.path.basename(sys.argv[0])))
	sys.exit(1)

letter = args[0].upper()

text = """
A is for Amy who fell down the stairs.
B is for Basil assaulted by bears.
C is for Clara who wasted away.
D is for Desmond thrown out of a sleigh.
E is for Ernest who choked on a peach.
F is for Fanny sucked dry by a leech.
G is for George smothered under a rug.
H is for Hector done in by a thug.
I is for Ida who drowned in a lake.
J is for James who took lye by mistake.
K is for Kate who was struck with an axe.
L is for Leo who choked on some tacks.
M is for Maud who was swept out to sea.
N is for Neville who died of ennui.
O is for Olive run through with an awl.
P is for Prue trampled flat in a brawl.
Q is for Quentin who sank on a mire.
R is for Rhoda consumed by a fire.
S is for Susan who perished of fits.
T is for Titus who flew into bits.
U is for Una who slipped down a drain.
V is for Victor squashed under a train.
W is for Winnie embedded in ice.
X is for Xerxes devoured by mice.
Y is for Yorick whose head was bashed in.
Z is for Zillah who drank too much gin.
"""

lookup = {}
for line in text.splitlines():
	if line:
		lookup[line[0]] = line
if letter in lookup:
	print(lookup[letter])
else:
	print('I do not know "{}"'.format(letter))
