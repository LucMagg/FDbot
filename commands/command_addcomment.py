from discord import Embed
from datetime import datetime

from classes.hero import *
from classes.pet import *
from utils.miscUtils import get_discord_color, date_format_fr
from utils.findUtils import *
from utils.strUtils import *
from utils.formatMessagesUtils import format_hero, format_pet, format_comments



def set_comment(args, author, heroes, pets, qualities, bot_commands):
	"""Commande /addcomment pour les héros et les pets"""
	matched = False
	i = 0

	#cherche avec les héros en un seul ou deux mots
	while not matched:
		split_args = args.split(' ')
		if i == 0 and len(split_args) > 0:
			to_find = split_args[0]
			comment = ' '.join(split_args[1:])
		elif i == 1 and len(split_args) > 1:
			to_find = split_args[0] + split_args[1]
			comment = ' '.join(split_args[2:])
		else:
			matched = True
		if not matched:
			search_match = find_match_names(to_find, heroes)
			whichone = 'hero'
			if search_match == None:
				search_match = find_match_names(to_find, pets)
				whichone = 'pet'
			if search_match != None:
				matched = True
			else:
				i += 1
			if i > 1:
				matched = True
	

	if search_match == None:
		#pas de héros ou de pet trouvé -> message d'erreur
		to_return = discord.Embed(title=bot_commands['error']['title'],
			description='Le héros ou le pet ' + str_arg_to_readable(args) + ' n\'a pas été trouvé dans la base de données.\n' +
				'Merci de vérifier et de réitérer la commande :cry:',
			color=get_discord_color(bot_commands['error']['color']))
	elif comment == "":
		to_return = discord.Embed(title=bot_commands['error']['title'],
			description='Le commentaire est vide :grin:\n' +
				'Merci de vérifier et de réitérer la commande :cry:',
			color=get_discord_color(bot_commands['error']['color']))
	else:
		append_comment(search_match, author, date_format_fr(), comment)
		if whichone == 'hero':
			description = format_hero(search_match, heroes, pets, qualities) + format_comments(search_match, bot_commands)
		else:
			description = format_pet(search_match, heroes) + format_comments(search_match, bot_commands)
		
		while not check_message_length(description, bot_commands):
			remove_oldest_comment(search_match)
			if whichone == 'hero':
				description = format_hero(search_match, heroes, pets, qualities) + format_comments(search_match, bot_commands)
			else:
				description = format_pet(search_match, heroes) + format_comments(search_match, bot_commands)
		
		color = get_discord_color(str_compact(search_match.color))
		to_return = discord.Embed(title='', description=description, color=color)

	return to_return



def append_comment(who, author, date, commentaire):
	matched = False
	for comment in who.comments:
		if comment.author == author:
			matched = True
			comment.commentaire = commentaire
			comment.date = date
	if not matched:
		who.comments.append(Comment(author=author, date=date, commentaire=commentaire))



def remove_oldest_comment(who):
	comment_dates = []
	for comment in who.comments:
		date_split = comment.date.split('/')
		comment_dates.append(datetime(int(date_split[2]),int(date_split[1]),int(date_split[0])))
	oldest_comment_index = comment_dates.index(min(comment_dates))
	who.comments.pop(oldest_comment_index)