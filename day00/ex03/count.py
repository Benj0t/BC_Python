import sys

i = 0
for arg in sys.argv:
	i = i + 1
if (i != 2):
	print("ERROR")
	sys.exit()

def text_analyzer(str):
	low = 0
	upp = 0
	car = 0
	ponct = 0
	spac = 0
	for char in str:
		car += 1
		if (char == char.upper() and char.isalpha() == True):
			upp += 1
		elif (char == char.lower() and char.isalpha() == True):
			low += 1
		elif (char == ' ' and char.isdigit() != True):
			spac += 1
		elif (char.isdigit() != True):
			ponct += 1
	print("Le texte contient ", car, " caracteres")
	print("- ", upp, " upper letters")
	print("- ", low, " lower letters")
	print("- ", ponct, " ponctuation marks")
	print("- ", spac, " spaces")
text_analyzer(sys.argv[1])