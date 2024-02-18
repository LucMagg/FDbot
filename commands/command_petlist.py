from discord import Embed

from classes.hero import *
from classes.pet import *
from utils.miscUtils import get_discord_color, stars
from utils.findUtils import *
from utils.strUtils import *


def get_pet_list(args, heroes, pets,bot_commands):
	#Commande /petlist

	my_hero = find_match_names(args, heroes)
	search_match = find_pets(my_hero, pets)

	if my_hero == None:
		#pas de pet trouvé -> message d'erreur
		to_return = discord.Embed(title=bot_commands['error']['title'],
			description='Le héros ' + str_arg_to_readable(args) + ' n\'a pas été trouvé dans la base des héros recensés.\n' +
				'Merci de vérifier et de réitérer la commande :cry:',
			color=get_discord_color(bot_commands['error']['color']))
	elif search_match == None:
		to_return = discord.Embed(title=bot_commands['error']['title'],
			description='Aucun pet trouvé pour le héros ' + my_hero.name + ' dans la base des pets recensés :cry:\n',
			color=get_discord_color(bot_commands['error']['color']))
	else:
		description = '# Liste des pets équipables par ' + my_hero.name + ' #\n'
		description += format_petlist(search_match)

		color = get_discord_color(my_hero.color)
		to_return = discord.Embed(title='', description=description, color=color)

		if my_hero.image_url != None:
			to_return.set_thumbnail(url=my_hero.image_url)		

	return to_return



def find_pets(hero, pets):
	found_pets = [[],[],[],[],[],[]]
	some_match = False
	for pet in pets:
		if (hero.name == pet.signature) or (hero.name == pet.signature_bis):
			found_pets[pet.stars].append([pet, 'signature'])
			some_match = True
		elif (hero.color == pet.color):
			some_match = True
			if (hero.heroclass == pet.petclass):
				found_pets[pet.stars].append([pet, 'full'])
			else:
				found_pets[pet.stars].append([pet, 'color'])

	if some_match:
		return found_pets
	else:
		return None



def format_petlist(found_objects):
	to_return = ''
	some_match = False

	for star_iter in range(0,len(found_objects)):
		if len(found_objects[star_iter]) > 0:
			some_match = True
			to_return += '### ' + stars(star_iter) + ' ###\n'
			for obj in found_objects[star_iter]:
				pet_talents = find_pet_talents(obj[0])
				to_append = obj[0].name + ' : '

				full_talent_to_append = False
				if obj[1] == 'signature':
					to_append += pet_talents[3]['name'] + ' (manacost : ' + str(obj[0].manacost) + ') | '
					full_talent_to_append = True
				if full_talent_to_append or obj[1] == 'full':
					to_append += pet_talents[2]['name'] + ' | '
				to_append += '+' + str(obj[0].attack) + '% att/def\n'
	
				to_return += to_append

	if some_match:
		return to_return
	else:
		return None