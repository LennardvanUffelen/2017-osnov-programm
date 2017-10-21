import sys

freq = []

fd = open('freq.txt', 'r')
for line in fd.readlines():
	line = line.strip()
	(f, w) = line.split('\t')
	freq.append((int(f), w))