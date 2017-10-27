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

#############################
####JUST PRINTING & TESTING#######
print(word)
word = ''.join(word)
print(word)