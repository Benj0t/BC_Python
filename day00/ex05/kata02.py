import sys

t = (3,30,2019,9,25)
tab = ["", "", "", "", ""]
i = 0
for val in t:
	if (val < 10):
		tab[i] = "0" + str(val)
	else:
		tab[i] = str(val)
	i +=1
print(tab[3], end = "")
print("/", end ="")
print(tab[4], end ="")
print("/", end ="")
print(tab[2], end ="")
print(" ", end ="")
print(tab[0], end ="")
print(":", end ="")
print(tab[1], end ="")
