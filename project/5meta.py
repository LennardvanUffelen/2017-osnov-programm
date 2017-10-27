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

######################################
####metateza prasłowiańska Długosz 2.3.2.5 Genis 1.5

wordbase = word

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
				word.insert(met11, "ó")
				word.insert(met11, "r")
			elif word[met12] is "l":
				word.pop(met11)
				word.pop(met11)
				word.insert(met11, "ó")
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

#############################
####JUST PRINTING & TESTING#######
word = ''.join(word)
print(word)