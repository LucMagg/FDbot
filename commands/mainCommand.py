import discord
from time import time

from utils.miscUtils import get_discord_color, nick
from .command_hero import get_hero_stats
from .command_item import get_items
from .command_talent import get_talents
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
	if "dhjk" in str.lower(args):
		command = "dhjk"

	match command:
		case 'bothelp':
			return_msg = discord.Embed(title=bot_commands['help']['title']['generic'],
				description=bot_commands['help']['description']['generic'],
				color=get_discord_color(bot_commands['help']['color']))

		case 'hero':
			if args == 'help':
				return_msg = discord.Embed(title=bot_commands['help']['title']['command'] + '/hero',
					description=bot_commands['help']['description']['hero'],
					color=get_discord_color(bot_commands['help']['color']))
			else:
				return_msg = get_hero_stats(args, heroes, pets, talents, qualities, bot_commands)

		case 'item':
			if args == 'help':
				return_msg = discord.Embed(title=bot_commands['help']['title']['command'] + '/item',
					description=bot_commands['help']['description']['item'],
					color=get_discord_color(bot_commands['help']['color']))
			else:
				return_msg = get_items(args, heroes, qualities, dusts, bot_commands)

		case 'talent':
			if args == 'help':
				return_msg = discord.Embed(title=bot_commands['help']['title']['command'] + '/talent',
					description=bot_commands['help']['description']['talent'],
					color=get_discord_color(bot_commands['help']['color']))
			else:
				return_msg = get_talents(args, heroes, pets, talents, bot_commands)

		case 'dhjk':
			return_msg = dhjk(bot_commands)
			


	return_msg.set_footer(text=bot_commands['footer'] + str(round(time()-begin_time,3))+ 's*')

	return [wait_msg, return_msg]