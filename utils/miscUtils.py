import discord

from time import strftime, localtime

def str_now():
	"""renvoie la date et l'heure sous forme de chaîne"""

	return strftime("%Y-%m-%d %H:%M:%S", localtime())




def nick(message):
	"""renvoie l'auteur du message (objet discord)"""

	nickname = message.author.nick
	if nickname == None:
		nickname = message.author.global_name
	else:
		nickname = str(nickname).split('[')[0]

	return nickname



def get_discord_color(color):
	"""renvoie la couleur Discord en fonction de color"""
	match color:
		case 'default':
			return discord.Color.default()
		case 'red':
			return discord.Color.red()
		case 'green':
			return discord.Color.green()
		case 'blue':
			return discord.Color.blue()
		case 'light':
			return discord.Color.gold()
		case 'dark':
			return discord.Color.magenta()



def stars(how_many):
	stars = ''
	for iter in range(0,how_many):
		stars += ':star:'
	return stars



def date_format_fr():
	return strftime("%d/%m/%Y", localtime())



def check_message_length(description, bot_commands):
	footer_txt = bot_commands['footer']['ok'] + 's*'
	if len(description) + len(footer_txt) > 4094:
		return False
	else:
		return True