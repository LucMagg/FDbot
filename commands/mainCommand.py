import discord
from time import time

from utils.miscUtils import get_discord_color, nick, check_message_length
from utils.strUtils import str_compact
from utils.findUtils import unique_objects, format_uniques
from .command_stats import get_stats
from .command_item import get_items
from .command_talent import get_talents_heroes_and_pets
from .command_class import get_class
from .command_petlist import get_pet_list
from .command_botstats import get_bot_stats
from .command_addcomment import set_comment
from .command_dhjk import dhjk
from .command_update import get_update


def main_command(msg, command, args, heroes, pets, talents, dusts, qualities, bot_commands):
	"""fonction principale de commande : vérifie si la commande existe"""

	author = nick(msg)

	#check la commande
	if ('dhjk' in str.lower(args)) or (str_compact(author) == 'dhjk' and str_compact(command) == 'moi') or (command == 'dieu') or (command == 'god'):
		command = "dhjk"

	match command:
		case 'bothelp':
			return_msg = discord.Embed(title=bot_commands['help']['title']['generic'],
				description=bot_commands['help']['description']['generic'],
				color=get_discord_color(bot_commands['help']['color']))

		case 'hero'|'pet':
			if args == 'help':
				return_msg = discord.Embed(title=bot_commands['help']['title']['command'] + command,
					description=bot_commands['help']['description'][command],
					color=get_discord_color(bot_commands['help']['color']))
			else:
				return_msg = get_stats(args, command, heroes, pets, qualities, bot_commands)

		case 'item':
			if args == 'help':
				return_msg = discord.Embed(title=bot_commands['help']['title']['command'] + command,
					description=bot_commands['help']['description']['item'],
					color=get_discord_color(bot_commands['help']['color']))
			else:
				return_msg = get_items(args, heroes, qualities, dusts, bot_commands)

		case 'talent':
			if args == 'help':
				return_msg = discord.Embed(title=bot_commands['help']['title']['command'] + command,
					description=bot_commands['help']['description']['talent'],
					color=get_discord_color(bot_commands['help']['color']))
			else:
				return_msg = get_talents_heroes_and_pets(args, heroes, pets, talents, bot_commands)

		case 'class':
			if args == 'help':
				return_msg = discord.Embed(title=bot_commands['help']['title']['command'] + command,
					description=bot_commands['help']['description']['class'] + format_uniques(unique_objects(heroes, 'heroclass')),
					color=get_discord_color(bot_commands['help']['color']))
			else:
				return_msg = get_class(args, heroes, pets, bot_commands)

		case 'petlist':
			if args == 'help':
				return_msg = discord.Embed(title=bot_commands['help']['title']['command'] + command,
					description=bot_commands['help']['description']['petlist'],
					color=get_discord_color(bot_commands['help']['color']))
			else:
				return_msg = get_pet_list(args, heroes, pets, bot_commands)

		case 'botstats':
			if args == 'help':
				return_msg = discord.Embed(title=bot_commands['help']['title']['command'] + command,
					description=bot_commands['help']['description']['petlist'],
					color=get_discord_color(bot_commands['help']['color']))
			else:
				return_msg = get_bot_stats(args, heroes, pets, talents, bot_commands)

		case 'addcomment':
			if args == 'help':
				return_msg = discord.Embed(title=bot_commands['help']['title']['command'] + command,
					description=bot_commands['help']['description']['addcomment'],
					color=get_discord_color(bot_commands['help']['color']))
			else:
				return_msg = set_comment(args, author, heroes, pets, qualities, bot_commands)

		case 'update':
			if args == 'help':
				return_msg = discord.Embed(title=bot_commands['help']['title']['command'] + command,
					description=bot_commands['help']['description']['update'],
					color=get_discord_color(bot_commands['help']['color']))
			else:
				return_msg = get_update(args, author, heroes, pets, bot_commands)


		case 'dhjk':
			return_msg = dhjk(bot_commands)

		case _:
			return_msg = discord.Embed(title=bot_commands['none']['title'],
					description=bot_commands['none']['description'],
					color=get_discord_color(bot_commands['help']['color']))
			
	#garde-fou contre les messages trop longs
	footer_txt = bot_commands['footer']['ok']

	if not check_message_length(return_msg.description, bot_commands):
		taille_max = 4096 - len(footer_txt) - len(bot_commands['footer']['too_long'])
		return_msg.description = return_msg.description[0:taille_max] + bot_commands['footer']['too_long']
	
	return_msg.set_footer(text=footer_txt)

	return return_msg