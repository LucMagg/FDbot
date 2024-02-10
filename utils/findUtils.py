from classes.dust import *
from classes.hero import *
from classes.item import *
from classes.pet import *
from classes.quality import *
from classes.talent import *

from .miscUtils import *
from .strFunctions import *


def find_match_name(arg, any_object_list):
	for an_object in any_object_list:
		if an_object.name != None:
			if str_compact(an_object.name) == str_compact(arg):
				return an_object
	return None


def get_average_stat(my_hero, heroes, pets, whichone):
	found_list = []
	count = 0
	for hero in heroes:
		if my_hero.heroclass == hero.heroclass:
			if whichone == 'att':
				found_list.append(hero.att_max(pets))
			elif whichone == 'def':
				found_list.append(hero.def_max(pets))
			count += 1
	found_list.sort(reverse=True)

	total = 0
	for f in found_list:
		total += f

	if whichone == 'att':
		my_index = found_list.index(my_hero.att_max(pets)) + 1
	elif whichone == 'def':
		my_index = found_list.index(my_hero.def_max(pets)) + 1

	return [my_index, count, round(total/count)]


def find_unique_talents(my_hero, heroes):
	my_talents = []
	for talent in my_hero.talents:
		if talent.name not in my_talents:
			my_talents.append(talent.name)

	out_of_talents = False
	for hero in heroes:
		if hero.name != my_hero.name and hero.heroclass == my_hero.heroclass:
			for htalent in hero.talents:
				while htalent.name in my_talents:
					my_talents.remove(htalent.name)
					if len(my_talents) == 0:
						out_of_talents = True
						break
				if out_of_talents:
					break
			if out_of_talents:
				break
		if out_of_talents:
			break
			

	if out_of_talents:
		return [None,None]
	else:
		my_talents.sort()
		to_return = ''
		for f in my_talents:
			to_return += f + ', '
		if len(my_talents) > 1:
			addchar = 's'
		else:
			addchar = ''
		return [to_return[:-2], addchar]


def find_gear(hero, qualities, whichone):
	to_return = ''
	price = 0
	for gear in hero.gear:
		if gear.ascend == whichone:
			for quality in qualities:
				if gear.quality == quality.name:
					to_return += quality.icon + ' ' + quality.name + ' ' + gear.name + '\n'
					price += quality.price

	return [to_return, price]


def find_comments(hero):
	to_return = ''
	for comment in hero.comments:
		if comment.author != None:
			to_return += '__' + comment.author + ' le ' + comment.date + '__\n'
			to_return += comment.commentaire + '\n'
	if to_return == '':
		to_return += 'Pas de commentaire pour l\'instant :shrug:\n'
		to_return += 'N\'hésitez pas à ajouter le vôtre via la commande /addcomment (/addcomment help pour plus d\'info) \n Sauf si c\'est kiki évidemment... :joy:'
	return to_return


def parse_args_to_item(args, qualities):
	parsed_arg = args.split(' ')

	for quality in qualities:
		if str_compact(quality.name) == str_compact(parsed_arg[0]):
			item_name = ' '.join(parsed_arg[1:])
			return Item(name=item_name, quality=quality.name)

	return Item(name=args, quality=None)


def find_items(item, heroes):
	found_heroes = [[],[],[],[],[],[]]
	some_match = False

	for hero in heroes:
		for gear in hero.gear:
			to_append = ''
			if gear.name != None:
				if str_compact(item.name) == str_compact(gear.name):
					some_match = True
					if item.quality == None:
						to_append = hero.name + ' (' + hero.color + ' ' + hero.heroclass + ') : ' + gear.ascend + ' (' + gear.quality + ')'
					else:
						if str_compact(item.quality) == str_compact(gear.quality):
							to_append = hero.name + ' (' + hero.color + ' ' + hero.heroclass + ') : ' + gear.ascend
					
				if to_append != '':	
					found_heroes[hero.stars].append(to_append)

	for iter in range(0,len(found_heroes)):
		if len(found_heroes[iter]) > 0:
			doublon_iter = 0
			while doublon_iter < len(found_heroes[iter])-1:
				if found_heroes[iter][doublon_iter].split(' ')[0] == found_heroes[iter][doublon_iter+1].split(' ')[0]:
					#doublon spotted!
					found_heroes[iter][doublon_iter] = found_heroes[iter][doublon_iter] + ',' + ' '.join(found_heroes[iter][doublon_iter+1].split(':')[1:])
					del(found_heroes[iter][doublon_iter+1])
					doublon_iter -= 1
				doublon_iter += 1

	to_return = '### Héros pouvant équiper cet objet : ###\n'
	for iter in range(0,len(found_heroes)):
		if len(found_heroes[iter]) > 0:
			to_return += '### ' + stars(iter) + ' ###\n'
			for nb_match in found_heroes[iter]:
				count_nb = len(nb_match.split(','))
				if count_nb > 1:
					to_insert = 'x' + str(count_nb) + ' :'
					nb_match = to_insert.join(nb_match.split(':'))
				to_return += nb_match + '\n'
	if some_match:
		return to_return
	else:
		return None



def recycle_item(item, qualities, dusts):
	to_return = ''
	for quality in qualities:
		if str_compact(item.quality) == str_compact(quality.name):
			my_dust = find_match_name(quality.recycling.dust.name, dusts)

			to_return = '### Achat en boutique : ###\n'
			to_return += str(quality.price) + ':gem:  (' + str(quality.discount_price) + ' :gem: en promo)\n'
			to_return += '### Recyclage : ###\n'
			to_return += '* :moneybag: ' + str(quality.recycling.gold) + '\n'
			to_return += '* ' + my_dust.icon + ' ' + str(quality.recycling.dust.quantity) + ' ' + str(quality.recycling.dust.name) + ' dusts'

	return to_return
