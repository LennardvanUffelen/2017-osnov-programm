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

#############################
####JUST PRINTING & TESTING#######
print(word)
word = ''.join(word)
print(word)