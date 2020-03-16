"""
Step 1

Putting all chess openings into one file
from A to E
"""

eco = ["a", "b", "c", "d", "e"]

collect = open("all.tsv", "w")

for letter in eco:
	file = open("eco\\" + letter + ".tsv", "r")

	first = True

	for l in file.readlines():

		if first:
			first = False
			continue

		collect.write(l)