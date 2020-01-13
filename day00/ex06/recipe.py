import sys

def add_rcp(name, t, meal, time, rec):
	rec.update({name: {'ingredients': t, 'meal': meal, 'prep_time': time}})
	return rec

def get_rcp(rec):
	t = [0]
	name = 0
	nb = 0
	ing = 0
	meal = 0
	time = 0
	while (not name):
		name = input("Entrez le nom de la recette. \n>")
		if (not name):
			print("/!\ Veuillez entrer un nom valide /!\.\n")
	while ((not nb) or nb < 0):
		nb = int(input("Entrez le nombre d ingredients composant la recette \n>"))
		if ((not nb) or (nb < 0)):
			print("/!\ Veuillez entrer un nombre valide /!\.\n>")
	tmp = nb - 1
	while (tmp > 0):
		t.append(0)
		tmp -= 1
	while (tmp < nb):
		while (not ing or tmp < nb):
			ing = input("Entrez un ingredient qui compose la recette \n>")
			if (not ing):
				print("/!\ Veuillez entrer un nom valide /!\.\n")
			else:
				t[tmp] = ing
				tmp += 1
	while (not meal):
		meal = input("Entrez le type de plat de la recette (breakfeast, lunch, dessert) \n>")
		if (not meal):
			print("/!\ Veuillez entrer un nom valide /!\.\n")
	while (not (time) or (time < 0)):
		time  = int(input("Entrez le temps necessaire pour realiser la recette \n>"))
		if (not time):
			print("/!\ Veuillez entrer un nombre valide /!\.\n")
	return(add_rcp(name, t, meal, time, rec))

def	del_rcp():
	return 0

def	print_rcp(rec):
	key = 0
	ver = 0
	while (not key or ver == 0):
		key = input("Please enter the recipe's name to delete:\n>")
		if (not key):
			print("/!\ Veuillez entrer un nom /!\ \n")
		else:
			for check in rec:
				if (key == check):
					ver = 1
					break
	print("Recipe for ", key,":\n")
	print("Ingredients list:", rec[key]['ingredients'], "\n")
	print("To be eaten for:", rec[key]['meal'], "\n")
	print("Takes ", rec[key]['prep_time'], "minutes of cooking\n")

def	print_book(rec):
	for key in rec:
		print("==================================================================================")
		print("Recipe for ", key,":\n")
		print("Ingredients list:", rec[key]['ingredients'], "\n")
		print("To be eaten for:", rec[key]['meal'], "\n")
		print("Takes ", rec[key]['prep_time'], "minutes of cooking\n")
		print("==================================================================================")

def	del_rcp(rec):
	key = 0
	ver = 0
	while (not key or ver == 0):
		key = input("Please enter the recipe's name to delete:\n>")
		if (not key):
			print("/!\ Veuillez entrer un nom valide /!\ \n")
		else:
			for check in rec:
				if (key == check):
					del rec[key]
					ver = 1
					break
def lobby(rec):
	nb = 0
	while (not nb or (nb > 5) or (nb < 0)):
		nb = int(input(("Please select an option by typing the corresponding number:\n1: Add a recipe\n2: Delete a recipe\n3: Print a recipe\n4: Print the cookbook\n5: Quit\n\n>")))
		if (not nb or (nb > 5) or (nb < 0)):
			print("The option does not exist, please type the corresponding number.\nTo exit, enter 5\n")
	if (nb == 1):
		rec = get_rcp(rec)
	elif (nb == 2):
		del_rcp(rec)
	elif (nb == 3):
		print_rcp(rec)
	elif (nb == 4):
		print_book(rec)
	else:
		print("Cookbook closed")
		sys.exit()

rec = {'sandwich': {'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'], 'meal':'lunch', 'prep_time':'10'}, 'cake': {'ingredients': ['flour', 'sugar', 'eggs'], 'meal':'dessert', 'prep_time':'60'}, 'salad': {'ingredients': '', 'meal': ['avocado', 'arugula', 'tomatoes', 'spinach'], 'prep_time':'15'}}

while (1):
	lobby(rec)