def generate_quality_list():
	"""
	Cette fonction génère une liste de dictionnaires sous la forme {shortcut,fullname,icon}

	Parameters:
	none :)

	Returns:
	liste: la liste en question
	"""
	shortcuts_base = 'MA','EP','MY','LE','EX','DI','RA','BR','CO','IN'
	fullnames_base = 'Magic','Epic','Mythic','Legendary','Exalted','Divine','Radiant','Brilliant','Coruscating','Incandescent'
	icon_base = ':blue_circle:',':purple_circle:',':yellow_circle:',':red_circle:',':green_circle:',':orange_circle:',':purple_circle:',':yellow_circle:',':red_circle:',':orange_circle:'
	price_base = 20,200,750,1500,2500,5000,200,1000,1800,2500
	iter = 0
	quality_list = []
	while iter < len(shortcuts_base):
		quality = {
			'shortcut': shortcuts_base[iter],
			'fullname': fullnames_base[iter],
			'icon'    : icon_base[iter],
			'price'   : price_base[iter]
		}
		quality_list.append(quality)
		iter+=1
	return quality_list
	


def parse_stuff(items):
	"""
	Cette fonction renvoie un dict à partir d'une liste d'items de la forme shortcut,item

	Parameters:
	items(listes de string): les items en question
	base_list(liste de dictionnaires): la liste des dictionnaires sous la forme {shortcut,fullname}

	Returns:
	dict : correspondant à la liste des items passés en paramètres sous la forme {price,value}
	"""
	value = ''
	price = 0
	base_list = generate_quality_list()
	
	for item in items:
		if item != 'X':
			parsed_item = str(item).split(',')
			
			for qual in base_list:
				if qual['shortcut'] == parsed_item[0]:
					value += qual['icon'] + ' ' + qual['fullname'] + ' ' + parsed_item[1] + '\n'
					price += qual['price']
					break
		
		#else:
		#	value += ':x: Non défini\n'

	if price > 0:
		return {'price': str(price) + ' :gem:',
				'value': value} 
	else:
		return {'price': '',
				'value': ':x: Non défini'}


def talent_values(talents):
	"""
	Cette fonction renvoie une chaine contenant les talents à partir d'une liste de talents

	Parameters:
	liste de string): les talents en question
	
	Returns:
	string : correspondant à la liste des talents passés en paramètre
	"""
	to_return = ''
	nb_talents = 0
	for talent in talents:
		if talent != 'X':
			to_return += talent + ' │ '
			nb_talents += 1
		else:
			to_return += ':x: │ '

	if nb_talents > 0:
		done = False
		while not done:
			if len(to_return) == 0:
				to_return == ':x: Non défini'
				done = True
			elif to_return[-6:] == ':x: │ ':
				to_return = to_return[:-6]
			else:
				done = True

		return to_return[:-3]
	else:
		return ':x: Non défini'



def parse_quality_itemname(item,base_list):
	"""
	Cette fonction parse un item passé en paramètre et renvoie un dictionnaire sous la forme {shortcut,item}

	Parameters:
	item(string): l'item en question
	base_list(liste de dictionnaires): la liste des dictionnaires sous la forme {shortcut,fullname}

	Returns:
	dict: sous la forme {shortcut,item} (renvoie {'',''} si item est vide)
	"""
	if item !='':
		split_item = item.split(' ',1)
		for qual in base_list:
			if qual['fullname'] == split_item[0]:
				my_quality = qual['shortcut']
				break
		quality_item = my_quality + ',' + split_item[1]

		return(quality_item)
	else:
		return 'X'



def fullname_from_shortcut(arg):
	base_list = generate_quality_list()
	for blist in base_list:
		if arg == blist['shortcut']:
			return blist['fullname']

	return 'error'




def shortcut_from_fullname(arg):
	base_list = generate_quality_list()
	for blist in base_list:
		if arg == blist['fullname']:
			return blist['shortcut']

	return 'error'