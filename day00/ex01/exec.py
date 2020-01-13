import sys

for arg in sys.argv:
	str = arg[::-1]
	for char in str:
		if (str[::-1] == sys.argv[0]):
			break
		if(char != char.upper()):
			print (char.upper(), end = "")
		elif (char != char.lower()):
			print (char.lower(), end ="")