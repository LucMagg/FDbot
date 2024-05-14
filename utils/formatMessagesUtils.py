from classes.hero import *
from classes.pet import *
from utils.miscUtils import stars
from utils.findUtils import *
from utils.strUtils import *



def format_hero(hero, heroes, pets, qualities):
	#***calculs***
	att_moyenne = get_average_stat(hero, heroes, pets, 'att')
	if att_moyenne[0] == 1:
		added_att_char = 'er'
	else:
		added_att_char = 'ème'

	def_moyenne = get_average_stat(hero, heroes, pets, 'def')
	if def_moyenne[0] == 1:
		added_def_char = 'er'
	else:
		added_def_char = 'ème'

	b_talents = ['','','','','','','']
	a_talents = ['','','','']
	m_talents = ['','','','']
	for t in hero.talents:
		if t.name != None:
			position = t.position.split(' ')
			if position[0] == 'base':
				b_talents[int(position[1])] = t.name
			elif position[0] == 'ascend':
				a_talents[int(position[1])] = t.name
			elif t.position[0] == 'merge':
				m_talents[int(position[1])] = t.name
	base_talents = ' | '.join([s for s in b_talents if s])
	asc_talents = ' | '.join([s for s in a_talents if s])
	merge_talents = ' __**ou**__ '.join([s for s in m_talents if s])
	
	unique_talents = find_unique_talents(hero, heroes)

	base_gear = find_gear(hero, qualities, 'A0')
	first_gear = find_gear(hero, qualities, 'A1')
	second_gear = find_gear(hero, qualities, 'A2')
	third_gear = find_gear(hero, qualities, 'A3')

	if hero.pet != None:
		my_pet = find_match_names(hero.pet, pets)
		if my_pet != None:
			for t in my_pet.talents:
				if t.position == 'gold':
					gold_pet_talent = t.name
				if t.position == 'full':
					full_pet_talent = t.name

	#***mise en forme***
	description = '# ' + hero.name + '   ' + stars(hero.stars) + '#\n' 
	description += hero.color + ' ' + hero.species + ' ' + hero.heroclass + '\n'

	description += '### Attributs max (A' + str(hero.ascend()) + ' - lvl ' + str(hero.lvl_max()) + ') : ###' + '\n'
	description += '__**Attaque**__ : ' + '\n'
	description += '**Total : ' + str(hero.att_max(pets)) + '**\n'  
	description += '(base : ' + str(hero.attack()) + ' + équipements : ' + str(hero.att_gear()) + ' + merge : ' + str(hero.att_merge())
	if hero.att_pet_boost(pets) != 0:
		description += ' + pet bonus : ' + str(hero.att_pet_boost(pets))
	description +=  ')\n'
	description += str(att_moyenne[0]) + added_att_char + ' sur ' + str(att_moyenne[1]) + ' ' + str_compact(hero.heroclass) + 's (moyenne de la classe : ' + str(att_moyenne[2]) + ')\n\n'
	description += '__**Défense**__ : ' + '\n'
	description += '**Total : ' + str(hero.def_max(pets)) + '**\n'
	description += '(base : ' + str(hero.defense()) + ' + équipements : ' + str(hero.def_gear_merge()) + ' + merge : ' + str(hero.def_gear_merge())
	if hero.def_pet_boost(pets) != 0:
		description += ' + pet bonus : ' + str(hero.def_pet_boost(pets))
	description +=  ')\n'
	description += str(def_moyenne[0]) + added_def_char + ' sur ' + str(def_moyenne[1]) + ' ' + str_compact(hero.heroclass) + 's (moyenne de la classe : ' + str(def_moyenne[2]) + ')\n\n'
	description += '**Orientation offensive :** ' + str(round(hero.att_max(pets)/hero.def_max(pets)*100)) + '%\n'

	description += '### Bonus de lead : ###' + '\n'
	description += hero.lead_bonus_color + '\n'
	if hero.lead_bonus_species != None:
		description += hero.lead_bonus_species +'\n'

	description += '### Talents : ###' + '\n'
	description += '__**Base :**__\n' + base_talents + '\n'
	description += '__**Ascension :**__\n' + asc_talents + '\n'
	if merge_talents != '':
		description += '__**Merge :**__\n' + merge_talents + '\n'
	if unique_talents[0] != None:
		description += '\n__Talent' + unique_talents[1] + ' unique' + unique_talents[1] + ' pour un ' + str_compact(hero.heroclass) + ' :__\n'
		description += unique_talents[0] + '\n'

	description += '### Équipements : ###' + '\n'
	if base_gear[1] > 0:
		description += '__**Base :**__ (coût : ' + str(base_gear[1]) + ' :gem:)\n'
		description += base_gear[0] + '\n'
	if first_gear[1] > 0:
		description += '__**1ère ascension :**__ (coût : ' + str(first_gear[1]) + ' :gem:)\n'
		description += first_gear[0] + '\n'
	if second_gear[1] > 0:
		description += '__**2ème ascension :**__ (coût : ' + str(second_gear[1]) + ' :gem:)\n'
		description += second_gear[0] + '\n'
	if third_gear[1] > 0:
		description += '__**3ème ascension :**__ (coût : ' + str(third_gear[1]) + ' :gem:)\n'
		description += third_gear[0] + '\n'
	if base_gear[1] + first_gear[1] + second_gear[1] + third_gear[1] == 0:
		description += 'Aucun équipement recensé pour ce héros :shrug:' + '\n'

	if hero.pet != None:
		description += '### Pet signature : ' + my_pet.name + ' ###' + '\n'
		description += 'Bonus max d\'attaque/défense : ' + str(my_pet.attack) + '%\n'
		description += 'Talent pour tous les ' + str_compact(hero.heroclass) + 's : ' + full_pet_talent + '\n'
		description += 'Talent gold seulement pour ' + hero.name + ' : ' + gold_pet_talent + '\n'

	description += '### Commentaires : ###' + '\n'

	return description



def format_pet(pet, heroes):
	#***calculs***
	other_heroes = []
	count_heroes = 0
	for hero in heroes:
		if (hero.heroclass == pet.petclass) and (hero.color == pet.color) and (hero.name != pet.signature):
			other_heroes.append(hero.name)
			count_heroes += 1
	other_heroes = ', '.join(other_heroes)
	if count_heroes > 1:
		added_s = 's'
	else:
		added_s = ''

	pet_talents = find_pet_talents(pet)

	merge_talents = ' | '.join([s for s in pet_talents[4] if s])

	manacost_merge = str(pet_talents[4].count('Mana Efficiency'))
	manacost_with_gold = str(pet.manacost + int(manacost_merge))

	#***mise en forme***
	description = '# ' + pet.name + '   ' + stars(pet.stars) + '#\n' 
	description += pet.color + ' pet pour ' + pet.petclass + '\n'

	description += '### Attributs max : ###\n'
	description += '+ ' + str(pet.attack) + '% attaque/défense\n'

	description += '### Héros signature : ###\n'
	description += pet.signature
	if pet.signature_bis != None:
		description += ' | ' + pet.signature_bis + '\n'
	else:
		description += '\n'
	if count_heroes > 0:
		description += '### Autre' + added_s + ' héros pouvant bénéficier du full talent :###\n'
		description += other_heroes + '\n'

	description += '### Talents : ###' + '\n'
	description += '__**Base :**__\n' + pet_talents[0] + ' (+1% att/def)\n'
	description += '__**Silver :**__\n' + pet_talents[1] + ' (+2% att/def)\n'
	description += '__**Full :**__\n' + pet_talents[2]['name'] + ' seulement pour ' + pet.petclass
	if pet_talents[2]['description'] != '':
		description += ' (' + pet_talents[2]['description'] + ')\n'
	else:
		description += '\n'
	description += '__**Merge :**__\n' + merge_talents + '\n'
	description += '__**Gold :**__\n' + pet_talents[3]['name']
	if pet_talents[3]['description'] != '':
		description += ' (' + pet_talents[3]['description'] + ')\n'
	else:
		description += '\n'
	description += '__**Mana Cost :**__\n' + str(pet.manacost) + ' (base : 25 - gold : ' + manacost_with_gold + ' - merge : ' + manacost_merge + ')\n'

	description += '### Commentaires : ###' + '\n'

	return description


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
		if talent.name not in my_talents and talent.name != None:
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

	if len(my_talents) == 0:
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



def format_comments(hero_or_pet, bot_commands):
	to_return = ''
	for comment in hero_or_pet.comments:
		if comment.author != None:
			to_return += '__' + comment.author + ' le ' + comment.date + '__\n'
			to_return += comment.commentaire + '\n'
	if to_return == '':
		to_return = bot_commands['nocomment']['description']
	return to_return