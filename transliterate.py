import sys

word =  sys.stdin.read()

#######################
####CLEANING IT UP#########

word = word.replace(" ב", "b")
word = word.replace("בּ", "b")
word = word.replace("בֿ", "v")
word = word.replace("וי", "oy")
word = word.replace("׳׳", "Q")
word = word.replace("יי", "Q")
word = word.replace("ײַ", "ay")

word = word.replace("ג", "g")
word = word.replace("ד", "d")
word = word.replace("ה", "h")
word = word.replace("וו", "v")
word = word.replace("ו", "u")
word = word.replace("אָ", "o")

word = word.replace(" אַ", "a")
word = word.replace("וּ", "u")
word = word.replace("וֹ", "oj")
word = word.replace("װ", "v")
word = word.replace("ז", "z")
word = word.replace("זש", "zh")
word = word.replace("ח", "kh")
word = word.replace("ט", "t")

word = word.replace("טש", "tsh")
word = word.replace("י", "y")
word = word.replace("יִ", "i")

word = word.replace("כּ", "k")
word = word.replace("כ", "kh")
word = word.replace("ך", "kh")
word = word.replace("ל", "l")
word = word.replace("מ", "m")
word = word.replace("ם", "m")
word = word.replace("ו", "u")

word = word.replace("נ", "n")
word = word.replace("ס", "s")
word = word.replace("ע", "e")
word = word.replace("פּ", "p")
word = word.replace("פֿ", "f")
word = word.replace("פ", "f")
word = word.replace("ף", "f")
word = word.replace("צ", "ts")
word = word.replace("ץ", "ts")
word = word.replace("ק", "k")
word = word.replace("ר", "r")
word = word.replace("ש", "sh")

word = word.replace("שׂ", "s")
word = word.replace("תּ", "t")
word = word.replace("ת", "s")

word = word.replace("אַ", "a")

word = word.replace("ן", "n")
word = word.replace("yy", "yi")
word = word.replace("ב", "b")

word = list(word)

cons = ["q", "w", "r", "t", "p", "s", "d","f", "g","h","j","k", "l","z","x","c","v","b","n","m", " "]

while "Q" in word:
	pal11 = word.index("Q")
	pal13 = pal11 - 1
	if word[pal13] is " ":
		word.pop(pal11)
		word.insert(pal11, "yi")
	else:
		word.pop(pal11)
		word.insert(pal11, "ey")

while "א" in word:
	pal11 = word.index("א")
	pal13 = pal11 - 1
	if word[pal13] is " ":
		word.pop(pal11)
	else:
		word.pop(pal11)
		word.insert(pal11, "e")

while "y" in word:
	pal11 = word.index("y")
	word.pop(pal11)
	word.insert(pal11, "QWER")

while "QWER" in word:
	pal11 = word.index("QWER")
	pal12 = pal11 + 1
	pal13 = pal11 - 1
	if word[pal12] in cons:
		if word[pal13] in cons:
			word.pop(pal11)
			word.insert(pal11, "i")
		else:
			word.pop(pal11)
			word.insert(pal11, "y")
	else:
		word.pop(pal11)
		word.insert(pal11, "y")

word = ''.join(word)
print(word)