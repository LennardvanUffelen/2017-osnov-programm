import sys

word =  sys.stdin.read()

#######################
####CLEANING IT UP#########

word = word.strip("\n")
word = word.strip(" ")
word = word.replace("r̥", "r˚", 10)
word = word.replace("l̥", "l˚", 10)
word = word.replace("ĕ", "'ĕ", 10)
word = list(word)

while "˚" in word:
	fpos = word.index("˚")
	fpos2 = fpos - 1
	fpos3 = word[fpos2] + word[fpos]
	word.pop(fpos)
	word.pop(fpos2)
	word.insert(fpos2, fpos3)

while "'" in word:
	fpos = word.index("'")
	fpos2 = fpos - 1
	fpos3 = word[fpos2] + word[fpos]
	word.pop(fpos)
	word.pop(fpos2)
	word.insert(fpos2, fpos3)

##########################
####DEFINING SOME STUFF########

samtwar = ["t", "d", "s", "z", "n", "r", "l"]
sammię = ["l'", "d'", "s'", "z'", "n'", "r'", "l'"]
samhis = ["c", "dz"]

###################################
####DIE AUSNAHMLOESE LAUTGESETZEN######

#####################################
### palatalizacja przez sł. j Długosz II 9.2.3

for p in word:
	if "p" in word:
		dej11 = word.index("p")
		dej12 = dej11 + 1
		dej13 = dej11 - 1
		lendej = len(word)
		if dej12 is not lendej:
			if word[dej12] is "j":
				word.pop(dej11)
				word.pop(dej11)
				word.insert(dej11, "p'")

for b in word:
	if "b" in word:
		dej11 = word.index("b")
		dej12 = dej11 + 1
		dej13 = dej11 - 1
		lendej = len(word)
		if dej12 is not lendej:
			if word[dej12] is "j":
				word.pop(dej11)
				word.pop(dej11)
				word.insert(dej11, "b'")

for m in word:
	if "m" in word:
		dej11 = word.index("m")
		dej12 = dej11 + 1
		dej13 = dej11 - 1
		lendej = len(word)
		if dej12 is not lendej:
			if word[dej12] is "j":
				word.pop(dej11)
				word.pop(dej11)
				word.insert(dej11, "m'")

for v in word:
	if "v" in word:
		dej11 = word.index("v")
		dej12 = dej11 + 1
		dej13 = dej11 - 1
		lendej = len(word)
		if dej12 is not lendej:
			if word[dej12] is "j":
				word.pop(dej11)
				word.pop(dej11)
				word.insert(dej11, "v'")

#####9.3.1.2
for n in word:
	if "n" in word:
		dej11 = word.index("n")
		dej12 = dej11 + 1
		dej13 = dej11 - 1
		lendej = len(word)
		if dej12 is not lendej:
			if word[dej12] is "j":
				word.pop(dej11)
				word.pop(dej11)
				word.insert(dej11, "n'")

for r in word:
	if "r" in word:
		dej11 = word.index("r")
		dej12 = dej11 + 1
		dej13 = dej11 - 1
		lendej = len(word)
		if dej12 is not lendej:
			if word[dej12] is "j":
				word.pop(dej11)
				word.pop(dej11)
				word.insert(dej11, "r'")

for l in word:
	if "l" in word:
		dej11 = word.index("l")
		dej12 = dej11 + 1
		dej13 = dej11 - 1
		lendej = len(word)
		if dej12 is not lendej:
			if word[dej12] is "j":
				if word[dej13] is "s":
					word.pop(dej13)
					word.pop(dej13)
					word.pop(dej13)
					word.insert(dej13, "l'")
					word.insert(dej13, "s'")
				else:
					word.pop(dej11)
					word.pop(dej11)
					word.insert(dej11, "l'")

#######9.3.1.3
for t in word:
	if "t" in word:
		dej11 = word.index("t")
		dej12 = dej11 + 1
		dej13 = dej11 - 1
		lendej = len(word)
		if dej12 is not lendej:
			if word[dej12] is "j":
				if word[dej13] is "s":
					word.pop(dej13)
					word.pop(dej13)
					word.pop(dej13)
					word.insert(dej13, "č")
					word.insert(dej13, "š")
				else:
					word.pop(dej11)
					word.pop(dej11)
					word.insert(dej11, "c")

for d in word:
	if "d" in word:
		dej11 = word.index("d")
		dej12 = dej11 + 1
		dej13 = dej11 - 1
		lendej = len(word)
		if dej12 is not lendej:
			if word[dej12] is "j":
				word.pop(dej11)
				word.pop(dej11)
				word.insert(dej11, "dz")

##############9.3.1.4
for s in word:
	if "s" in word:
		dej11 = word.index("s")
		dej12 = dej11 + 1
		dej13 = dej11 - 1
		lendej = len(word)
		if dej12 is not lendej:
			if word[dej12] is "j":
				word.pop(dej11)
				word.pop(dej11)
				word.insert(dej11, "š")

for z in word:
	if "z" in word:
		dej11 = word.index("z")
		dej12 = dej11 + 1
		dej13 = dej11 - 1
		lendej = len(word)
		if dej12 is not lendej:
			if word[dej12] is "j":
				word.pop(dej11)
				word.pop(dej11)
				word.insert(dej11, "ž")

#################################
#### kt > c Genis 1.1

for k in word:
	if "k" in word:
		dej11 = word.index("k")
		dej12 = dej11 + 1
		dej13 = dej11 - 1
		lendej = len(word)
		if dej12 is not lendej:
			if word[dej12] is "t":
				word.pop(dej11)
				word.pop(dej11)
				word.insert(dej11, "c")
			elif word[dej13] is "s":
					word.pop(dej13)
					word.pop(dej13)
					word.pop(dej13)
					word.insert(dej13, "č")
					word.insert(dej13, "š")

#############################
####JUST PRINTING & TESTING#######
print(word)
word = ''.join(word)
print(word)