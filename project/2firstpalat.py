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

#####################################
##### pierwsza palatalizacja Długosz 9.3.2.1

pal1 = ["i", "ę", "ĕ", "r˚'", "l˚'", "ь"]

for g in word:
	if "g" in word:
		pal11 = word.index("g")
		pal12 = pal11 + 1
		pal13 = pal11 - 1
		if word[pal12] in pal1:
			pal14 = word[pal12]
			lenpal = len(word)
			if pal14 is "i":
				pal14 = "y"
			word.pop(pal11)
			word.pop(pal11)
			word.insert(pal11, pal14)
			word.insert(pal11, "ž")

for x in word:
	if "x" in word:
		pal11 = word.index("x")
		pal12 = pal11 + 1
		pal13 = pal11 - 1
		if word[pal12] in pal1:
			pal14 = word[pal12]
			lenpal = len(word)
			if pal14 is "i":
				pal14 = "y"
			word.pop(pal11)
			word.pop(pal11)
			word.insert(pal11, pal14)
			word.insert(pal11, "š")

for k in word:
	if "k" in word:
		pal11 = word.index("k")
		pal12 = pal11 + 1
		pal13 = pal11 - 1
		if word[pal12] in pal1:
			pal14 = word[pal12]
			lenpal = len(word)
			if pal14 is "i":
				pal14 = "y"
			word.pop(pal11)
			word.pop(pal11)
			word.insert(pal11, pal14)
			word.insert(pal11, "č")

#############################
####JUST PRINTING & TESTING#######
print(word)
word = ''.join(word)
print(word)