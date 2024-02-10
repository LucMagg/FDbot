import random

from discord import Embed
from utils.miscUtils import get_discord_color, stars


def dhjk(messages):
	""" Commande dhjk xD"""

	my_random = random.randint(0,4)

	to_return = Embed(title=stars(10), description=messages['dhjk'][str(my_random)]['text'], color=get_discord_color("blue")).set_image(url=messages['dhjk'][str(my_random)]['gif'])
	
	return to_return