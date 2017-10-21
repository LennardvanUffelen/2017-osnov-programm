import sys

word =  sys.stdin.read()

out = open('output.txt', 'w')

with open('output.txt', 'w') as f:
	sys.stdout = out

#######################
####CLEANING IT UP#########

word = word.strip("\n")
word = word.strip(" ")
word = word.replace("אַ", "a")
word = word.replace("אָ", "o")
word = list(word)

for א in word:
	if "א" in word:
		num = word.index("א")
		word.pop(num)

#######################
#######################
####CONVERTER##########

for  א in word:
	if "א-" in word:
		num = word.index("א-")
		word.pop(num)
		word.insert(num, "a")

for אָ in word:
	if "אָ" in word:
		num = word.index("אָ")
		word.pop(num)
		word.insert(num, "o")

for ב in word:
	if "ב" in word:
		num = word.index("ב")
		word.pop(num)
		word.insert(num, "b")

for בּ in word:
	if "בּ" in word:
		num = word.index("בּ")
		word.pop(num)
		word.insert(num, "b")

for בֿ in word:
	if "בֿ" in word:
		num = word.index("בֿ")
		word.pop(num)
		word.insert(num, "v")

for ג in word:
	if "ג" in word:
		num = word.index("ג")
		word.pop(num)
		word.insert(num, "g")


for ד in word:
	if "ד" in word:
		num = word.index("ד")
		word.pop(num)
		word.insert(num, "d")

for ה in word:
	if "ה" in word:
		num = word.index("ה")
		word.pop(num)
		word.insert(num, "h")

for ו in word:
	if "ו" in word:
		num = word.index("ו")
		num2 = num - 1
		if word[num2] is ו:
			word.pop(num)
			word.pop(num)
			word.insert(num, "v")
		else:
			word.pop(num)
			word.insert(num, "u")

for וּ in word:
	if "וּ" in word:
		num = word.index("וּ")
		word.pop(num)
		word.insert(num, "u")

for וֹ in word:
	if "וֹ" in word:
		num = word.index("וֹ")
		word.pop(num)
		word.insert(num, "oy")

for װ in word:
	if "װ" in word:
		num = word.index("װ")
		word.pop(num)
		word.insert(num, "v")

for וי in word:
	if "וי" in word:
		num = word.index("וי")
		word.pop(num)
		word.insert(num, "oy")

for ז in word:
	if "ז" in word:
		num = word.index("ז")
		word.pop(num)
		word.insert(num, "z")

for ח in word:
	if "ח" in word:
		num = word.index("ח")
		word.pop(num)
		word.insert(num, "kh")


for ט in word:
	if "ט" in word:
		num = word.index("ט")
		word.pop(num)
		word.insert(num, "t")

for י in word:
	if "י" in word:
		num = word.index("י")
		word.pop(num)
		word.insert(num, "y")
#Consonantal [j] when the first character in a syllable. Vocalic [i] otherwise.

for יִ in word:
	if "יִ" in word:
		num = word.index("יִ")
		word.pop(num)
		word.insert(num, "i")

for ב in word:
	if "ב" in word:
		num = word.index("ב")
		word.pop(num)
		word.insert(num, "b")

for ב in word:
	if "ב" in word:
		num = word.index("ב")
		word.pop(num)
		word.insert(num, "b")

for כּ in word:
	if "כּ" in word:
		num = word.index("כּ")
		word.pop(num)
		word.insert(num, "k")

for כ in word:
	if "כ" in word:
		num = word.index("כ")
		word.pop(num)
		word.insert(num, "kh")

for ך in word:
	if "ך" in word:
		num = word.index("ך")
		word.pop(num)
		word.insert(num, "kh")

for ל in word:
	if "ל" in word:
		num = word.index("ל")
		word.pop(num)
		word.insert(num, "l")

for מ in word:
	if "מ" in word:
		num = word.index("מ")
		word.pop(num)
		word.insert(num, "m")

for ם in word:
	if "ם" in word:
		num = word.index("ם")
		word.pop(num)
		word.insert(num, "m")

for נ in word:
	if "נ" in word:
		num = word.index("נ")
		word.pop(num)
		word.insert(num, "n")

for ן in word:
	if "ן" in word:
		num = word.index("ן")
		word.pop(num)
		word.insert(num, "n")

for ס in word:
	if "ס" in word:
		num = word.index("ס")
		word.pop(num)
		word.insert(num, "s")

for ע in word:
	if "ע" in word:
		num = word.index("ע")
		word.pop(num)
		word.insert(num, "e")

for פּ in word:
	if "פּ" in word:
		num = word.index("פּ")
		word.pop(num)
		word.insert(num, "p")

for פֿ in word:
	if "פֿ" in word:
		num = word.index("פֿ")
		word.pop(num)
		word.insert(num, "p")

for פ in word:
	if "פ" in word:
		num = word.index("פ")
		word.pop(num)
		word.insert(num, "f")

for ף in word:
	if "ף" in word:
		num = word.index("ף")
		word.pop(num)
		word.insert(num, "ף")

for ב in word:
	if "ב" in word:
		num = word.index("ב")
		word.pop(num)
		word.insert(num, "b")

for צ in word:
	if "צ" in word:
		num = word.index("צ")
		word.pop(num)
		word.insert(num, "ts")

for ץ in word:
	if "ץ" in word:
		num = word.index("ץ")
		word.pop(num)
		word.insert(num, "ts")

for ק in word:
	if "ק" in word:
		num = word.index("ק")
		word.pop(num)
		word.insert(num, "k")

for ר in word:
	if "ר" in word:
		num = word.index("ר")
		word.pop(num)
		word.insert(num, "r")

for ש in word:
	if "ש" in word:
		num = word.index("ש")
		word.pop(num)
		word.insert(num, "sh")

for שׂ in word:
	if "שׂ" in word:
		num = word.index("שׂ")
		word.pop(num)
		word.insert(num, "s")

for תּ in word:
	if "תּ" in word:
		num = word.index("תּ")
		word.pop(num)
		word.insert(num, "t")

for ת in word:
	if "ת" in word:
		num = word.index("ת")
		word.pop(num)
		word.insert(num, "s")

print(word)
word = ''.join(word)
word = word.replace("uu", "v")
print(word)