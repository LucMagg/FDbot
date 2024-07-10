from .pathUtils import *
from .jsonUtils import *

from classes.hero import *
from classes.dust import *
from classes.quality import *
from classes.talent import *
from classes.pet import *



def get_heroes():
	"""charge le JSON des heros et renvoie une liste d'objets Hero"""

	my_json = 'hero.json'
	my_path = add_rep_to_parent('JSON')

	heroes = importFromJson(my_json,my_path)

	to_return = []
	for hero in heroes:
		gears = []
		for g in hero['gear']:
			gears.append(Item(name=g['name'], quality=g['quality'], ascend=g['ascend']))

		talents = []
		for t in hero['talents']:
			talents.append(Talent(name=t['name'], position=t['position']))

		comments = []
		for c in hero['comments']:
			comments.append(Comment(author=c['author'], date=c['date'], commentaire=c['commentaire']))

		to_append = Hero(name=hero['name'],
			stars=int(hero['stars']),
			ascend_max=int(hero['ascend_max']),
			heroclass=hero['heroclass'],
			species=hero['species'],
			color=hero['color'],
			attack75=int(hero['attack75']),
			defense75=int(hero['defense75']),
			attack85=int(hero['attack85']),
			defense85=int(hero['defense85']),
			attack95=int(hero['attack95']),
			defense95=int(hero['defense95']),
			attack100=int(hero['attack100']),
			defense100=int(hero['defense100']),
			talents=talents,
			gear=gears,
			comments=comments,
			lead_bonus_color=hero['lead_bonus_color'],
			lead_bonus_species=hero['lead_bonus_species'],
			base_IA=hero['base_IA'],
			image_url=hero['image_url'],
			pet=hero['pet']
			)

		to_return.append(to_append)

	return to_return




def get_dusts():
	"""charge le JSON des dust et renvoie une liste d'objets Dust"""

	my_json = 'dust.json'
	my_path = add_rep_to_parent('JSON')

	dusts = importFromJson(my_json,my_path)

	to_return = []
	for dust in dusts:
		to_append = Dust(name=dust['name'],
			icon=dust['icon'],
			conversion=Conversion(p_input=Dust_conv(name=dust['conversion']['input']['name'], quantity=dust['conversion']['input']['quantity']),
				p_output=Dust_conv(name=dust['conversion']['output']['name'], quantity=dust['conversion']['output']['quantity'])),
			price_in_gems=Price(price=dust['price_in_gems']['price'], quantity=dust['price_in_gems']['quantity'])
			)
		to_return.append(to_append)

	return to_return




def get_qualities():
	"""charge le JSON des qualités d'objets et renvoie une liste d'objets Quality"""

	my_json = 'quality.json'
	my_path = add_rep_to_parent('JSON')

	qualities = importFromJson(my_json,my_path)

	to_return = []
	for quality in qualities:
		to_append = Quality(name=quality['name'],
			icon=quality['icon'],
			price=int(quality['price']),
			discount_price=quality['discount_price'],
			recycling=Recycling(dust=Dust_conv(name=quality['recycling']['dust']['name'],quantity=quality['recycling']['dust']['quantity']),
				gold=quality['recycling']['gold']
				)
			)
		to_return.append(to_append)

	return to_return




def get_messages():
	my_json = 'messages.json'
	my_path = add_rep_to_parent('JSON')

	messages = importFromJson(my_json,my_path)

	return messages




def get_talents():
	my_json = 'talent.json'
	my_path = add_rep_to_parent('JSON')

	talents = importFromJson(my_json,my_path)

	to_return = []
	for talent in talents:
		to_append = Talent(name=talent['name'],
			position=talent['position'],
			description=talent['description'],
			bonus_count=talent['bonus_count'],
			bonus_type=talent['bonus_type']
			)
		to_return.append(to_append)

	return to_return




def get_pets():
	my_json = 'pet.json'
	my_path = add_rep_to_parent('JSON')

	pets = importFromJson(my_json,my_path)

	to_return = []
	for pet in pets:
		talents = []
		for t in pet['talents']:
			talents.append(Talent(name=t['name'], position=t['position']))

		comments = []
		for c in pet['comments']:
			comments.append(Comment(author=c['author'], date=c['date'], commentaire=c['commentaire']))

		to_append = Pet(name=pet['name'],
			stars=int(pet['stars']),
			petclass=pet['petclass'],
			color=pet['color'],
			signature=pet['signature'],
			signature_bis=pet['signature_bis'],
			attack=int(pet['attack']),
			defense=int(pet['defense']),
			manacost=int(pet['manacost']),
			talents=talents,
			comments=comments,
			image_url=pet['image_url']
			)
		to_return.append(to_append)

	return to_return

def get_spire_scores():
	my_json = 'spire.json'
	my_path = add_rep_to_parent('JSON')

	spires = importFromJson(my_json,my_path)

	return spires