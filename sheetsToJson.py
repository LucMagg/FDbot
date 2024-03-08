from to_be_deleted.sheetsImport import *
from to_be_deleted.items_talents import *

from classes.hero import *
from classes.talent import *
from classes.item import *
from classes.comment import *
from classes.pet import *

from utils.jsonUtils import *
from utils.pathUtils import *
from utils.strUtils import *



def herosheet_to_json():
	googlesheet = "prep-bot-dev"
	sheet_name = "HeroSheet"
	sheet_range = "A:BQ"

	print('connexion à Sheets')
	raw_bdd = getValues(googlesheet,sheet_name,sheet_range)

	print('création des objets Hero')
	heroes = []
	i = 0
	for row in raw_bdd:
		i+=1
		if i>2:
			gear = []
			for i in range(20,44):
				if row[i] != 'X':
					quality = fullname_from_shortcut(row[i].split(',')[0])
					name = row[i].split(',')[1]
				else:
					quality = None
					name = None
				gear.append(Item(name = name, quality = quality, ascend = 'A' + str((i-20) // 6)).toJSON())

			talent = []
			for i in range(8,20):
				if row[i] != 'X':
					talent.append(str_readable(row[i]))
				else:
					talent.append(None)

			comments = []
			for i in range(45,51,2):
				if row[i] != '':
					comments.append(Comment(author = comment_split(row[i],'author'), date = comment_split(row[i],'date'), commentaire = comment_split(row[i+1],'comment')).toJSON())

			if row[52] == 'None':
				lead_bonus_species = None
			else:
				lead_bonus_species = row[52]

			if row[66] == 'None':
				image_url = None
			else:
				image_url = row[66]

			if row[67] == 'None':
				pet = None
			else:
				pet = row[67]


			newhero = Hero(name = row[44],
				stars = int(row[1]),
				ascend_max = int(row[2]),
				heroclass = row[3],
				species = row[4],
				color = row[5],
				attack = int(row[6]),
				defense = int(row[7]),
				talents = [Talent(name = talent[0], position = 'base 1').toJSON(),
					Talent(name = talent[1], position = 'base 2').toJSON(),
					Talent(name = talent[2], position = 'base 3').toJSON(),
					Talent(name = talent[3], position = 'base 4').toJSON(),
					Talent(name = talent[4], position = 'base 5').toJSON(),
					Talent(name = talent[5], position = 'base 6').toJSON(),
					Talent(name = talent[6], position = 'ascend 1').toJSON(),
					Talent(name = talent[7], position = 'ascend 2').toJSON(),
					Talent(name = talent[8], position = 'ascend 3').toJSON(),
					Talent(name = talent[9], position = 'merge 1').toJSON(),
					Talent(name = talent[10], position = 'merge 2').toJSON(),
					Talent(name = talent[11], position = 'merge 3').toJSON()
				],
				gear = gear,
				comments = comments,
				lead_bonus_color = row[51],
				lead_bonus_species = lead_bonus_species,
				base_IA = row[53],
				image_url = image_url,
				pet = pet
				)
			heroes.append(newhero.toJSON())	
	return heroes



def petsheet_to_json():
	googlesheet = "prep-bot-dev"
	sheet_name = "PetSheet"
	sheet_range = "A:AF"

	print('connexion à Sheets')
	raw_bdd = getValues(googlesheet,sheet_name,sheet_range)

	print('création des objets Pet')
	pets = []
	i = 0
	for row in raw_bdd:
		i+=1
		if i>2:
			talent = []
			j = 9
			while j < 24:
				if j == 12:
					pass
				elif row[j] != 'X':
					talent.append(str_readable(row[j]))
				else:
					talent.append(None)
				j += 1
			
			comments = []
			for i in range(25,31,2):
				if row[i] != '':
					comments.append(Comment(author = comment_split(row[i],'author'), date = comment_split(row[i],'date'), commentaire = comment_split(row[i+1],'comment')).toJSON())

			if row[5] == 'X':
				signature_bis = None
			else:
				signature_bis = row[5]

			if row[31] == 'None':
				image_url = None
			else:
				image_url = row[31]

			pet = Pet(name = row[24],		
				stars = int(row[1]),
				petclass = row[2],
				color = row[3],
				signature = row[4],
				signature_bis = signature_bis,
				attack = int(row[6]),
				defense = int(row[7]),
				manacost = int(row[8]),
				talents = [Talent(name = talent[0], position = 'base').toJSON(),
					Talent(name = talent[1], position = 'silver').toJSON(),
					Talent(name = talent[2], position = 'gold').toJSON(),
					Talent(name = talent[3], position = 'full').toJSON(),
					Talent(name = talent[4], position = 'merge 1').toJSON(),
					Talent(name = talent[5], position = 'merge 2').toJSON(),
					Talent(name = talent[6], position = 'merge 3').toJSON(),
					Talent(name = talent[7], position = 'merge 4').toJSON(),
					Talent(name = talent[8], position = 'merge 5').toJSON(),
					Talent(name = talent[9], position = 'merge 6').toJSON(),
					Talent(name = talent[10], position = 'merge 7').toJSON(),
					Talent(name = talent[11], position = 'merge 8').toJSON(),
					Talent(name = talent[12], position = 'merge 9').toJSON(),
					Talent(name = talent[13], position = 'merge 10').toJSON()
				],
				comments = comments,
				image_url = image_url
			)

			pets.append(pet.toJSON())
	return pets




def talentsheet_to_json():
	googlesheet = "prep-bot-dev"
	sheet_name = "ListTalents"
	sheet_range = "A:A"

	print('connexion à Sheets')
	raw_bdd = getValues(googlesheet,sheet_name,sheet_range)

	print('création des objets Talent')
	talents = []
	i = 0
	for row in raw_bdd:
		i+=1
		if i>2:
			talent = Talent(name = str_readable(row[0]))

			talents.append(talent.toJSON())
	return talents




def comment_split(arg,whichone):
	if arg != '':
		match whichone:	
			case 'date':
				date_comment = arg.split(' /// ')[1].split('/')
				for i in range(0,3):
					date_comment[i] = date_comment[i].rjust(2, '0')
				date_comment = '/'.join(date_comment)
				return date_comment
			case 'author':
				return arg.split(' /// ')[0]
			case 'comment':
				return arg
	else:
		return None





print('Export des héros...')
heroes = herosheet_to_json()
exportInJson(heroes,'hero.json',add_rep_to_parent('JSON'))
print('OK')

print('Export des pets...')
pets = petsheet_to_json()
exportInJson(pets,'pet.json',add_rep_to_parent('JSON'))
print('OK')

print('Export des talents...')
talents = talentsheet_to_json()
exportInJson(talents,'talent.json',add_rep_to_parent('JSON'))
print('OK')