from discord import Embed
from time import sleep

from utils.miscUtils import get_discord_color
from utils.findUtils import *
from utils.strUtils import str_arg_to_readable



def get_items(args, heroes, qualities, dusts, bot_commands):
	"""Commande /item"""
	my_item = parse_args_to_item(args, qualities)

	match_list = find_objects(my_item, heroes, 'item')
	if match_list != None:
		printable_list = '### Héros pouvant équiper '
		if my_item.quality != None:
			printable_list += my_item.quality + ' ' 
		printable_list += my_item.name + ' :###\n' + format_results(match_list)
	else:
		printable_list = ''


	if my_item.quality != None:
		add_to_list = recycle_item(my_item, qualities, dusts)
	else:
		add_to_list = ''


	if printable_list == '':
		#pas d'item trouvé -> message d'erreur
		to_return = discord.Embed(title=bot_commands['error']['title'],
			description='L\'objet ' + args + ' n\'a pas été trouvé dans la base des objets recensés.\n' +
				'Merci de vérifier et de réitérer la commande :cry:',
			color=get_discord_color(bot_commands['error']['color']))
	else:
		title = ''
		description = '# ' + str_arg_to_readable(args) + ' #\n' + printable_list + add_to_list
		color = get_discord_color(bot_commands['class']['color'])

		to_return = discord.Embed(title=title, description=description, color=color)		

	return to_return



def parse_args_to_item(args, qualities):
	parsed_arg = args.split(' ')

	for quality in qualities:
		if str_compact(quality.name) == str_compact(parsed_arg[0]):
			item_name = ' '.join(parsed_arg[1:])
			return Item(name=str_arg_to_readable(item_name), quality=str_arg_to_readable(quality.name))

	return Item(name=str_arg_to_readable(args), quality=None)

	

def recycle_item(item, qualities, dusts):
	to_return = ''
	for quality in qualities:
		if str_compact(item.quality) == str_compact(quality.name):
			my_dust = find_match_names(quality.recycling.dust.name, dusts)

			to_return = '### Achat en boutique : ###\n'
			to_return += str(quality.price) + ':gem:  (' + str(quality.discount_price) + ' :gem: en promo)\n'
			to_return += '### Recyclage : ###\n'
			to_return += '* :moneybag: ' + str(quality.recycling.gold) + '\n'
			to_return += '* ' + my_dust.icon + ' ' + str(quality.recycling.dust.quantity) + ' ' + str(quality.recycling.dust.name) + ' dusts'

	return to_return