from discord import Embed

from classes.hero import *
from classes.pet import *
from utils.miscUtils import get_discord_color
from utils.findUtils import *
from utils.strUtils import *
from utils.formatMessagesUtils import format_hero, format_pet, format_comments



def get_stats(args, command, heroes, pets, qualities, bot_commands):
	"""Commandes /hero et /pet"""

	if command == 'hero':
		search_match = find_match_names(args, heroes)
		readable = 'héros'
		addchar = ''
	else:
		search_match = find_match_names(args, pets)
		readable = 'pet'
		addchar = 's'

	if search_match == None:
		#pas de héros ou de pet trouvé -> message d'erreur
		to_return = discord.Embed(title=bot_commands['error']['title'],
			description='Le ' + readable + ' ' + str_arg_to_readable(args) + ' n\'a pas été trouvé dans la base des ' + readable + addchar + ' recensés.\n' +
				'Merci de vérifier et de réitérer la commande :cry:',
			color=get_discord_color(bot_commands['error']['color']))
	else:
		if command == 'hero':
			description = format_hero(search_match, heroes, pets, qualities) + format_comments(search_match, bot_commands)
		else:
			description = format_pet(search_match, heroes) + format_comments(search_match, bot_commands)

		color = get_discord_color(str_compact(search_match.color))
		to_return = discord.Embed(title='', description=description, color=color)

		if search_match.image_url != None:
			to_return.set_thumbnail(url=search_match.image_url)		

	return to_return