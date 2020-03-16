"""
Step 2

Processing all moves so we can
use raw data with chessboars.js
"""



collect = open("moves.tsv", "w")

file = open("all.tsv", "r")

for l in file.readlines():

	row = l.split("\t")

	print(row[3])