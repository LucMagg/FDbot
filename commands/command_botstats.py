from discord import Embed

from classes.hero import *
from classes.pet import *
from classes.talent import *

from utils.miscUtils import get_discord_color, stars
from utils.findUtils import *
from utils.strUtils import str_compact, str_arg_to_readable


def get_bot_stats(args, heroes, pets, talents, bot_commands):
	"""Commande /botstats"""

	colors = unique_objects(heroes, 'color')
	species = unique_objects(heroes, 'species')
	classes = unique_objects(heroes, 'heroclass')

	description = '# Stats du bot #\n'
	description += '### ' + str(len(heroes)) + ' héros recensés : #\n'

	description += '* '
	for star in range(1,6):
		count_items = find_specific_objects(star ,heroes, 'stars')
		description += str(len(count_items)) + stars(star) + ', '
	description = description[:-2]
	description += '\n'
	
	description += '* ' + str(len(colors)) + ' couleurs ('
	for color in colors:
		count_items = find_specific_objects(color, heroes, 'color')
		description += str(len(count_items)) + ' ' + color + ', '
	description = description[:-2]
	description += ')\n'

	description += '* ' + str(len(species)) + ' espèces ('
	for specie in species:
		count_items = find_specific_objects(specie, heroes, 'species')
		description += str(len(count_items)) + ' ' + specie + ', '
	description = description[:-2]
	description += ')\n'

	description += '* ' + str(len(classes)) + ' classes ('
	for heroclass in classes:
		count_items = find_specific_objects(heroclass, heroes, 'heroclass')
		description += str(len(count_items)) + ' ' + heroclass + ', '
	description = description[:-2]
	description += ')\n'

	colors = unique_objects(pets, 'color')
	classes = unique_objects(pets, 'petclass')

	description += '### ' + str(len(pets)) + ' pets recensés : #\n'

	description += '* '
	for star in range(1,6):
		count_items = find_specific_objects(star ,pets, 'stars')
		description += str(len(count_items)) + stars(star) + ', '
	description = description[:-2]
	description += '\n'
	
	description += '* ' + str(len(colors)) + ' couleurs ('
	for color in colors:
		count_items = find_specific_objects(color, pets, 'color')
		description += str(len(count_items)) + ' ' + color + ', '
	description = description[:-2]
	description += ')\n'

	description += '* ' + str(len(classes)) + ' classes ('
	for petclass in classes:
		count_items = find_specific_objects(petclass, pets, 'petclass')
		description += str(len(count_items)) + ' ' + petclass + ', '
	description = description[:-2]
	description += ')\n'

	description += '### ' + str(len(talents)) + ' talents recensés #\n'

	to_return = discord.Embed(title='', description=description, color=get_discord_color('default'))

	return to_return