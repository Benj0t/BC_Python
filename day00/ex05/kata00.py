import sys
t = (19,42,21)

j = len(t)
print("The ", j, "numbers are: ", end = "")
i = 0
while (i < j - 1):
	print(t[i], end = ", ")
	i += 1
print(t[i])