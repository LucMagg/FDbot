from discord import Embed

from classes.hero import *
from utils.miscUtils import get_discord_color, stars
from utils.findUtils import *


def get_hero_stats(args, heroes, pets, talents, qualities, bot_commands):
	"""Commande /hero"""

	hero = find_match_name(args, heroes)

	if hero == None:
		#pas de héros trouvé -> message d'erreur
		to_return = discord.Embed(title=bot_commands['error']['title'],
			description='Le héros ' + args + ' n\'a pas été trouvé dans la base des héros recensés.\n' +
				'Merci de vérifier et de réitérer la commande :cry:',
			color=get_discord_color(bot_commands['error']['color']))
	else:
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

		base_talents = ''
		asc_talents = ''
		merge_talents = ''
		for t in hero.talents:
			if t.name != None:
				if t.position[:4] == 'base':
					base_talents += t.name + ' │ '
				elif t.position[:6] == 'ascend':
					asc_talents += t.name + ' │ '
				elif t.position[:5] == 'merge':
					merge_talents += t.name + ' __**ou**__ '
		base_talents = base_talents[:-3]
		asc_talents = asc_talents[:-3]
		if merge_talents != '':
			merge_talents = merge_talents[:-12]
		
		unique_talents = find_unique_talents(hero, heroes)

		base_gear = find_gear(hero, qualities, 'A0')
		first_gear = find_gear(hero, qualities, 'A1')
		second_gear = find_gear(hero, qualities, 'A2')
		third_gear = find_gear(hero, qualities, 'A3')

		if hero.pet != None:
			my_pet = find_match_name(hero.pet, pets)
			if my_pet != None:
				for t in my_pet.talents:
					if t.position == 'gold':
						gold_pet_talent = t.name
					if t.position == 'full':
						full_pet_talent = t.name



		#***mise en forme***
		title = ''
		color = get_discord_color(str_compact(hero.color))

		description = '# ' + hero.name + '   ' + stars(hero.stars) + '#\n' 
		description += hero.color + ' ' + hero.species + ' ' + hero.heroclass + '\n'
		#description += stars(hero.stars) + '\n'

		description += '### Attributs max (A' + str(hero.ascend()) + ' - lvl ' + str(hero.lvl_max()) + ') : ###' + '\n'
		description += '__**Attaque**__ : ' + '\n'
		description += '**Total : ' + str(hero.att_max(pets)) + '**\n'  
		description += '(base : ' + str(hero.attack) + ' + équipements : ' + str(hero.att_gear()) + ' + merge : ' + str(hero.att_merge())
		if hero.att_pet_boost(pets) != 0:
			description += ' + pet bonus : ' + str(hero.att_pet_boost(pets))
		description +=  ')\n'
		description += str(att_moyenne[0]) + added_att_char + ' sur ' + str(att_moyenne[1]) + ' ' + str_compact(hero.heroclass) + 's (moyenne de la classe : ' + str(att_moyenne[2]) + ')\n\n'
		description += '__**Défense**__ : ' + '\n'
		description += '**Total : ' + str(hero.def_max(pets)) + '**\n'
		description += '(base : ' + str(hero.defense) + ' + équipements : ' + str(hero.def_gear_merge()) + ' + merge : ' + str(hero.def_gear_merge())
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
		description += find_comments(hero)


		to_return = discord.Embed(title=title, description=description, color=color)

		if hero.image_url != None:
			to_return.set_thumbnail(url=hero.image_url)

	return to_return