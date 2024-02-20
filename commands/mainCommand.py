import discord
from time import time

from utils.miscUtils import get_discord_color, nick
from utils.strUtils import str_compact
from utils.findUtils import unique_objects, format_uniques
from .command_stats import get_stats
from .command_item import get_items
from .command_talent import get_talents_heroes_and_pets
from .command_class import get_class
from .command_petlist import get_pet_list
from .command_botstats import get_bot_stats
from .command_dhjk import dhjk


async def main_command(msg, command, args, heroes, pets, talents, dusts, qualities, bot_commands):
	"""fonction principale de commande : vérifie si la commande existe"""

	begin_time = time()
	author = nick(msg)

	#envoie le message de prise en compte de la commande avant traitement
	wait_msg = await msg.channel.send(embed=discord.Embed(title=bot_commands['wait']['title'],
			description=bot_commands['wait']['description'],
			color=get_discord_color(bot_commands['wait']['color'])))

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
				return_msg = get_stats(args, command, heroes, pets, talents, qualities, bot_commands)

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


		case 'dhjk':
			return_msg = dhjk(bot_commands)

		case other:
			return_msg = discord.Embed(title=bot_commands['none']['title'],
					description=bot_commands['none']['description'],
					color=get_discord_color(bot_commands['help']['color']))
			
	#garde-fou contre les messages trop longs
	footer_txt = bot_commands['footer'] + str(round(time()-begin_time,3))+ 's*'

	if len(return_msg.description) + len(footer_txt) > 4096:
		error_msg = "\n**[...]**\n\n:warning: la fin est tronquée pour cause de dépassement de la taille maximum d\'un message sur discord :shrug:\nSi possible, merci d'affiner votre recherche pour avoir le résultat complet :wink:"
		taille_max = 4096 - len(footer_txt) - len(error_msg)
		return_msg.description = return_msg.description[0:taille_max] + error_msg

	return_msg.set_footer(text=footer_txt)

	return [wait_msg, return_msg]