from discord import Embed

from classes.hero import *
from classes.pet import *

from utils.miscUtils import get_discord_color
from utils.findUtils import *
from utils.strUtils import str_compact, str_arg_to_readable


def get_class(args, heroes, pets, bot_commands):
	"""Commande /class"""

	hero_description = format_class_results(find_match_class(args, heroes, pets, 'heroes'),'Héros')
	pets_description = format_class_results(find_match_class(args, heroes, pets, 'pets'),'Pets')

	if hero_description == None:
		#pas de classe trouvée -> message d'erreur
		to_return = discord.Embed(title=bot_commands['error']['title'],
			description='La classe ' + str_arg_to_readable(args) + ' n\'a pas été trouvée dans la base des classes recensées.\n' +
				'Merci de vérifier et de réitérer la commande :cry:',
			color=get_discord_color(bot_commands['error']['color']))
	else:
		description = '# ' + str_arg_to_readable(args) + ' #\n'
		description += '### Liste des héros de la classe spécifiée : ###\n' + hero_description
		if pets_description != None:
			description += '### Liste des pets de classe : ###\n' + pets_description

		to_return = discord.Embed(title='', description=description, color=get_discord_color('default'))

	return to_return



def format_class_results(found_objects, whichone):
	to_return = ''
	some_match = False
	print(found_objects)

	if found_objects != None:
		for star_iter in range(0,len(found_objects)):
			print(star_iter)
			if len(found_objects[star_iter]) > 0:
				some_match = True
				to_return += '### ' + stars(star_iter) + ' ###\n'
				for obj in found_objects[star_iter]:
					to_return += obj['name'] + ' (' + obj['color'] + ')'
					match whichone:
						case 'Héros':
							if obj['att_rank'] == 1:
								add_att_char = 'er'
							else:
								add_att_char = 'ème'

							if obj['def_rank'] == 1:
								add_def_char = 'er'
							else:
								add_def_char = 'ème'
							to_return += ' : Att max : ' + str(obj['att_max']) + ' (' + str(obj['att_rank']) + add_att_char + ') | Def max : ' + str(obj['def_max']) + ' (' + str(obj['def_rank']) + add_def_char + ')\n'

						case 'Pets':
							to_return += '\n'
				print(to_return)

	if some_match:
		return to_return
	else:
		return None

	