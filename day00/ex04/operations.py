import sys

i = 0
for arg in sys.argv:
	i = i + 1
if (i != 3):
	print("ERROR, (wrong number of arguments)")
	sys.exit()
print(sys.argv[1].isdigit(), sys.argv[1].isdigit())
if ((sys.argv[1].isdigit() == False) or (sys.argv[2] == False)):
	print("Error, (only numbers)")
	sys.exit()

def calc(nb, mod):
	print("Sum:\t\t\t",nb + mod)
	print("Difference\t\t", nb - mod)
	print("Product\t\t\t", nb * mod)
	if (nb == 0 or mod == 0):
		print("ERROR, (div by zero)")
		print("ERROR, (modulo by zero)")
		sys.exit()
	else:
		print("Quotient\t\t", nb / mod)
		print("Reminder\t\t", nb % mod)
	return(nb + mod, nb - mod, nb * mod, nb / mod, nb % mod)

calc(int(sys.argv[1]), int(sys.argv[2]))