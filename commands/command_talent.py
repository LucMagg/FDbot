from discord import Embed

from classes.hero import *
from classes.pet import *
from classes.talent import *
from utils.miscUtils import get_discord_color
from utils.findUtils import *
from utils.strUtils import str_compact, str_arg_to_readable


def get_talents_heroes_and_pets(args, heroes, pets, talents, bot_commands):
	"""Commande /talent"""

	talent = find_match_names(str_arg_to_readable(args), talents)

	if talent != None:
		description = '# ' + talent.name + ' #\n'
		if talent.description != None and talent.description != '':
			description += talent.description +'\n'
		description += format_talent(talent, heroes, 'Héros') + '\n'
		description += format_talent(talent, pets, 'Pets') + '\n'
		description = description[:-2]

		return discord.Embed(title='', description=description, color=get_discord_color('default'))

	else:
		return discord.Embed(title=bot_commands['error']['title'],
			description='Le talent ' + args + ' n\'a pas été trouvé dans la base des talents recensés.\n' +
			'Merci de vérifier et de réitérer la commande :cry:',
			color=get_discord_color(bot_commands['error']['color']))



def format_talent(talent, object_list, whichone):
	match whichone:
		case 'Héros':
			match_talent = find_objects(talent, object_list, 'heroTalent')
		case 'Pets':
			match_talent = find_objects(talent, object_list, 'petTalent')

	if match_talent != None:
		match_talent = '### ' + whichone + ' ayant ' + talent.name + ' :###\n' + format_results(match_talent)
	else:
		match_talent = ''

	return match_talent




