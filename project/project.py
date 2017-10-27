################### insert a word in late common slavic (western variant)
################### this script contain most major sound laws in the transation from LCS to old polish
################### among others: 2nd & 3th palalization, slavic metathesis, western slavic umlaut, polish umlaut
################### this script cannot predict irregularities
################### problems will definitely arise because of the lack of a written standard for LCS
################### the standard used is that of Polish handbooks in historical linguistics such as Długosz (2006)
################### but still, that guy is pretty inconsistent as wel...
################### moreover, some changes took place simultanously resulting in more massive irregularities
################### another way to solve this is is piping the sound laws in separate scripts
#####EXAMPLE####### echo "berg" | python3 project.py

import sys

word =  sys.stdin.read()

#######################
####CLEANING IT UP#########

word = word.strip("\n")
word = word.strip(" ")
word = word.replace("r̥", "r˚", 10)
word = word.replace("l̥", "l˚", 10)
word = word.replace("ĕ", "'ĕ", 10)
#word = word.replace("ь", "'", 10)
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

#####################################
#### druga palatalizacja Genis 1.4 Długosz 9.3.2.2

for k in word:
	if "k" in word:
		pal11 = word.index("k")
		pal12 = pal11 + 1
		pal13 = pal11 - 1
		lenpal = len(word)
		if dej12 is not lenpal:			
			if word[pal12] == "ě":
				word.pop(pal11)
				word.pop(pal11)
				word.insert(pal11, "ĕ")
				word.insert(pal11, "c")
			elif word[pal12] == "i":
				word.pop(pal11)
				word.pop(pal11)
				word.insert(pal11, "y")
				word.insert(pal11, "c")

for g in word:
	if "g" in word:
		pal11 = word.index("g")
		pal12 = pal11 + 1
		pal13 = pal11 - 1
		lenpal = len(word)
		if pal12 is not lenpal:	
			if word[pal12] == "ě":
				word.pop(pal11)
				word.pop(pal11)
				word.insert(pal11, "ĕ")
				word.insert(pal11, "dz")
			elif word[pal12] == "i":
				word.pop(pal11)
				word.pop(pal11)
				word.insert(pal11, "y")
				word.insert(pal11, "dz")

for x in word:
	if "x" in word:
		pal11 = word.index("x")
		pal12 = pal11 + 1
		pal13 = pal11 - 1
		lenpal = len(word)
		if pal12 is not lenpal:	
			if word[pal12] == "ě":
				word.pop(pal11)
				word.pop(pal11)
				word.insert(pal11, "ĕ")
				word.insert(pal11, "š")
			elif word[pal12] == "i":
				word.pop(pal11)
				word.pop(pal11)
				word.insert(pal11, "y")
				word.insert(pal11, "š")

###################################
#### trzecia palatalizacja Genis 1.4

for ь in word:
	if "ь" in word:
		pal11 = word.index("ь")
		pal12 = pal11 + 1
		pal13 = pal11 - 1
		lenpal = len(word)
		if pal12 is not lenpal:	
			if word[pal12] is "ě":
				word.pop(pal11)
				word.pop(pal11)
				word.insert(pal11, "ĕ")
				word.insert(pal11, "š")
			elif word[pal12] is "i":
				word.pop(pal11)
				word.pop(pal11)
				word.insert(pal11, "i")
				word.insert(pal11, "š")


######################################
####metateza prasłowiańska Długosz 2.3.2.5 Genis 1.5

for o in word:
	if "o" in word:
		met11 = word.index("o")
		met12 = met11 + 1
		met13 = met11 - 1
		lenmet = len(word)
		if met12 is not lenmet:
			if word[met12] is "r":
				word.pop(met11)
				word.pop(met11)
				word.insert(met11, "o")
				word.insert(met11, "r")
			elif word[met12] is "l":
				word.pop(met11)
				word.pop(met11)
				word.insert(met11, "o")
				word.insert(met11, "l")

for e in word:
	if "e" in word:
		met11 = word.index("e")
		met12 = met11 + 1
		met13 = met11 - 1
		lenmet = len(word)
		if met12 is not lenmet:
			if word[met12] is "r":
				word.pop(met11)
				word.pop(met11)
				word.insert(met11, "e")
				word.insert(met11, "r'")
			elif word[met12] is "l":
				word.pop(met11)
				word.pop(met11)
				word.insert(met11, "e")
				word.insert(met11, "l'")

######################
# przegłos lechicki Długosz 2.1.1

for ĕ in word:
	if "ĕ" in word:
		przeg11 = word.index("ĕ")
		przeg12 = przeg11 + 1
		przeg13 = przeg11 - 1
		lenprzeg = len(word)
		if przeg12 is not lenprzeg:
			if word[przeg12] in samtwar:
					word.pop(przeg11)
					word.insert(przeg11, "a")
					if word[przeg13] in samtwar:
						word[przeg13] = word[przeg13] + "'"

for e in word:
	if "e" in word:
		przeg11 = word.index("e")
		przeg12 = przeg11 + 1
		przeg13 = przeg11 - 1
		lenprzeg = len(word)
		if przeg12 is not lenprzeg:
			if word[przeg12] in samtwar:
				word.pop(przeg11)
				word.insert(przeg11, "o")
				if word[przeg13] in samtwar:
					word[przeg13] = word[przeg13] + "'"

for ę in word:	
	if "ę" in word:
		przeg11 = word.index("ę")
		przeg12 = przeg11 + 1
		przeg13 = przeg11 - 1
		lenprzeg = len(word)
		if przeg12 is not lenprzeg:
			if word[przeg12] in samtwar:
				word.pop(przeg11)
				word.insert(przeg11, "ǫ")
				if word[przeg13] in samtwar:
					word[przeg13] = word[przeg13] + "'"

if "r˚" in word:
	przeg11 = word.index("r˚")
	przeg12 = przeg11 + 1
	przeg13 = przeg11 - 1
	lenprzeg = len(word)
	if przeg12 is not lenprzeg:
		if word[przeg12] in samtwar:
			word.pop(przeg11)
			word.insert(przeg11, "r")
			word.insert(przeg11, "a")

if "l˚" in word:
	przeg11 = word.index("l˚")
	przeg12 = przeg11 + 1
	przeg13 = przeg11 - 1
	lenprzeg = len(word)
	if przeg12 is not lenprzeg:
		if word[przeg12] in samtwar:
			word.pop(przeg11)
			word.insert(przeg11, "l")
			word.insert(przeg11, "e")

################## r' > rz

if "r'" in word:
	przeg11 = word.index("r'")
	word.pop(przeg11)
	word.insert(przeg11, "rz")

#############################
####JUST PRINTING & TESTING#######
print(word)
word = ''.join(word)
print(word)