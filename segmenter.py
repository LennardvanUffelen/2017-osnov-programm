import sys

sin = sys.stdin.read()

sin = sin.replace('\n', ' ')

ssplit = sin.split(r'[\. \? \! ]')

for s in ssplit:
	print(s)