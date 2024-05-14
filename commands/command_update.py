from discord import Embed


from utils.updateUtils import update_bdd
from classes.hero import *
from classes.pet import *
from utils.miscUtils import get_discord_color
from utils.findUtils import *
from utils.strUtils import *
from utils.formatMessagesUtils import format_hero, format_pet, format_comments

urls = {'heroes': ['Hero_Gear','Hero_Talents','Hero_Stats'],
        'pets': ['Pet_Stats','Pet_Talents']}

def get_update(args, author, heroes, pets, bot_commands):
	#Commande /update
    if args == '' or args == 'all':
        toParse = urls['heroes'] + urls['pets']
    else:
        toParse = urls[args]
    update_bdd(toParse, heroes, pets)

    return_msg = discord.Embed(title=bot_commands['update']['title'],
					description=bot_commands['update']['description']['all'] + bot_commands['update']['description']['thxmsg'],
					color=get_discord_color(bot_commands['update']['color']))

    return return_msg