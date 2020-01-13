from random import *
import sys
#nb = randint(1, 99)
nb = 42
print("This is an interactive guessing game!\nYou have to enter a number between 1 and 99 to find out the secret number.\nType 'exit' to end the game.\nGood luck!\n\n")
tries = 0
while (1):
	tries += 1
	guess = int(input("What's your guess between 1 and 99 ?\n>>"))
	if (guess > nb):
		print("Too high!\n")
	elif (guess < nb):
		print("Too low!\n")
	else:
		if (nb == 42):
			print("La vie... ne me parlez pas de la vie. \nMarvin -H2g2: Le Guide du Voyageur Galactique")
		elif (tries == 1):
			print("Du premier coup, bien joue!\n")
		elif (tries == 2):
			print("Presque un Oneshot, dommage!")
		elif (tries <= 7):
			print("Ca commencait a etre long")
		elif (tries <= 15):
			print("Nan mais faut reflechir a un moment")
		sys.exit()
		