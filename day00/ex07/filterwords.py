import sys

i = 0
for arg in sys.argv:
	i = i + 1
if (i != 3 or sys.argv[1].isdigit() == True or sys.argv[2] == False):
	print("ERROR")
	sys.exit()
i = 0
slen = 0
t = [""]
str = sys.argv[1]
nb = int(sys.argv[2])
for char in str:
	if (char != ' '):
		t[i] = t[i] + char
	else:
		if (len(t[i])):
			t.append("")
			slen += 1
		i += 1

i = 0
while (i <= slen):
	print(len(t[i]))
	if (len(t[i]) > int(sys.argv[2])):
		del (t[i])
		slen -= 1
	else:
		i += 1
print(t)
	