import sys

ssplit = sys.stdin.readlines()

index = 0
max = len(ssplit) - 1

for x in range (0, max):
	if ssplit[index].strip() == '':
		index = index + 1
	else:
		print('#', ssplit[index].strip())
		sensplit = ssplit[index].split(' ')
		index = index + 1
		senindex = 0
		senmax = len(sensplit)
		for x in range (0, senmax):
			sensplit[senindex] = sensplit[senindex].strip()
			if sensplit[senindex].strip() == '':
				senindex = senindex + 1
			else:
				print(senindex + 1, '\t', sensplit[senindex], '\t_\t_\t_\t_\t_\t_\t_\t_\t_')
				senindex = senindex + 1
	print()