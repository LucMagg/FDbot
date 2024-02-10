def str_readable(arg):
	"""Renvoie la chaîne de caractères arg sous un format lisible par l'utilisateur"""

	if type(arg) == str:
		specialCases = ["of","to","&"]
		exceptions = ['-']

		i = 1
		while i < len(arg):
			if arg[i] in exceptions:
				i += 1
			elif arg[i] == str.upper(arg[i]) and arg[i-1] != " " and arg[i] not in specialCases:
				arg = arg[:i] + " " + arg[i:]
			i += 1

			

		for specialCase in specialCases:
			if specialCase in arg:
				nextChar = arg[arg.find(specialCase) + len(specialCase)]
				if nextChar == " ":
					arg = arg.replace(specialCase," " + specialCase)

		while arg[-1] == " ":
			arg = arg[:-1]

		return arg
	else:
		print(f"L'argument fourni ({arg}) à la fonction str_readable n'est pas une chaîne de caractères")
		return None




def str_compact(arg):
	"""renvoie la chaîne de caractères arg sous un format comparable"""

	split_cars = [' ','-','&']

	if type(arg) == str:
		for split_car in split_cars:
			arg = arg.replace(split_car,'')
		arg = str.lower(arg)
		return arg

	else:
		print(f"L'argument fourni ({arg}) à la fonction str_compact n'est pas une chaîne de caractères")
		return None



def str_arg_to_readable(arg):
	specialCases = ["of","to"]
	split_cars = [' ','-','&']

	if type(arg) == str:
		some_match = False
		for split_car in split_cars:
			if split_car in arg:
				some_match = True
				args = arg.split(split_car)
				for a in args:
					if a not in specialCases:
						args[args.index(a)] = str.upper(a[0]) + str.lower(a[1:])
				arg = split_car.join(args)

		if not some_match:
			arg = str.upper(arg[0]) + str.lower(arg[1:])
			
		return arg

	else:
		print(f"L'argument fourni ({arg}) à la fonction str_compact n'est pas une chaîne de caractères")
		return None
