import sys

i = 0
for arg in sys.argv:
	i = i + 1
if (i > 2):
	print("ERROR")
	sys.exit()
str = sys.argv[1]
if (str.isdigit() == True):
	nb = int(str)
	if (nb % 2 == 0):
		print("I'm Even.")
	elif (nb == 0):
		print("I'm Zero.")
	else:
		print("I'm Odd.")
else:
	print("Error")