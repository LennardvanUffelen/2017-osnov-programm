import sys

loc = input('Please enter file domain: ')
locout = input('Please enter output domain:')

fout = open(locout, 'w')

with open('output.txt', 'w') as f:
	sys.stdout = fout

f = open(loc, 'r')
sin = f.read()
f.close()

sin = sin.replace('\n', ' ')

ssplit = sin.split('. ')

index = 0
max = len(ssplit) - 1

for x in range (0, max):
	print('\n', index + 1, ssplit[index], '\n')
	print('Index\tSurface form\t\tLemma\tUPOS\tXPOS\tMorph. features\tHead\tRelation\tSecondary dependencies\tMiscellaneous')
	sensplit = ssplit[index].split(' ')
	index = index + 1
	senindex = 0
	senmax = len(sensplit)
	for x in range (0, senmax):
		print(senindex + 1, '\t', sensplit[senindex], '\t\t\t-\t-\t-\t-\t\t-\t-\t\t-\t\t\t-')
		senindex = senindex + 1