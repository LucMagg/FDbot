from discord import Embed
from time import sleep

from utils.miscUtils import get_discord_color
from utils.findUtils import *
from utils.strFunctions import str_arg_to_readable



def get_items(args, heroes, qualities, dusts, bot_commands):
	"""Commande /item"""
	my_item = parse_args_to_item(args, qualities)

	printable_list = find_items(my_item, heroes)
	if my_item.quality != None:
		add_to_list = recycle_item(my_item, qualities, dusts)
	else:
		add_to_list = ''


	if printable_list == None:
		#pas d'item trouvé -> message d'erreur
		to_return = discord.Embed(title=bot_commands['error']['title'],
			description='L\'objet ' + args + ' n\'a pas été trouvé dans la base des objets recensés.\n' +
				'Merci de vérifier et de réitérer la commande :cry:',
			color=get_discord_color(bot_commands['error']['color']))
	else:
		title = ''
		description = '# ' + str_arg_to_readable(args) + ' #\n' + printable_list + add_to_list
		color=get_discord_color(bot_commands['class']['color'])

		to_return = discord.Embed(title=title, description=description, color=color)		

	return to_return