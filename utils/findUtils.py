from classes.dust import *
from classes.hero import *
from classes.item import *
from classes.pet import *
from classes.quality import *
from classes.talent import *

from .miscUtils import *
from .strUtils import *



def find_match_names(arg, any_object_list):
	to_return = []
	
	for an_object in any_object_list:
		if an_object.name != None:
			if str_compact(an_object.name) == str_compact(arg):
				to_return.append(an_object)
	
	if len(to_return) == 1:
		return to_return[0]
	elif len(to_return) > 1:
		return to_return
	else:
		return None



def find_match_class(arg, heroes, pets, whichone):
	found_objects = [[],[],[],[],[],[]]
	some_match = False

	match whichone:
		case 'heroes':
			object_list = heroes
		case 'pets':
			object_list = pets

	raw_list = []
	for obj in object_list:
		to_append = ''
		match whichone:
			case 'heroes':
				if str_compact(obj.heroclass) == str_compact(arg):
					to_append = {'name': obj.name,
							'color': obj.color,
							'stars': obj.stars,
							'att_max': obj.att_max(pets),
							'att_rank': 0,
							'def_max': obj.def_max(pets),
							'def_rank': 0}

			case 'pets':
				if str_compact(obj.petclass) == str_compact(arg):
					to_append = {'name': obj.name,
							'color': obj.color,
							'stars': obj.stars}

		if to_append != '':
			raw_list.append(to_append)

	if whichone == 'heroes':
		for my_key in [['att_max','att_rank'],['def_max','def_rank']]:
			raw_list = sort_list(raw_list, my_key)

	if len(raw_list) > 0:
		for item in raw_list:
			found_objects[item['stars']].append(item)
		return found_objects
	else:
		return None



def sort_list(my_list, keys):
	sorted_list = sorted(my_list, key=lambda cle:cle[keys[0]], reverse = True)
	
	for item in sorted_list:
		item[keys[1]] = sorted_list.index(item) + 1

	#calcul des ex-aequo
	for i in range(0, len(sorted_list)-1):
		if sorted_list[i][keys[0]] == sorted_list[i+1][keys[0]]:
			sorted_list[i+1][keys[1]] = sorted_list[i][keys[1]]

	#renvoie des clés triées avec le rank dans la liste de base
	for item in my_list:
		for sorted_item in sorted_list:
			if item[keys[0]] == sorted_item[keys[0]]:
				item[keys[1]] == sorted_item[keys[1]]
				break

	return my_list



def remove_doublons(found_objects):
	for iter in range(0,len(found_objects)):
		if len(found_objects[iter]) > 0:
			doublon_count = 0
			while doublon_count < len(found_objects[iter])-1:
				if found_objects[iter][doublon_count]['name'] == found_objects[iter][doublon_count+1]['name']: #doublon spotted!
					if found_objects[iter][doublon_count]['quality'] != '': #spechol case du doublon mais avec qualité d'item non spécifiée
						found_objects[iter][doublon_count]['quality'] += ',' + found_objects[iter][doublon_count+1]['quality']
					found_objects[iter][doublon_count]['count'] += 1
					found_objects[iter][doublon_count]['pos'] += ',' + found_objects[iter][doublon_count+1]['pos']
					del(found_objects[iter][doublon_count+1])
				else:
					doublon_count += 1

	return found_objects



def find_objects(item, obj_list, whichone):
	found_objects = [[],[],[],[],[],[]]
	some_match = False
	
	for to_parse in obj_list:
		match whichone:
			case 'item':
				object_list = to_parse.gear
			case 'heroTalent'|'petTalent':
				object_list = to_parse.talents

		for obj in object_list:
			to_append = ''
			if obj.name != None:
				if str_compact(item.name) == str_compact(obj.name):
					some_match = True
					match whichone:
						case 'item':
							if item.quality == None:
								to_append = {'name': to_parse.name,
									'color': to_parse.color,
									'class': to_parse.heroclass,
									'count': 1,
									'pos': obj.ascend,
									'quality': obj.quality}
							else:
								if str_compact(item.quality) == str_compact(obj.quality):
									to_append = {'name': to_parse.name,
									'color': to_parse.color,
									'class': to_parse.heroclass,
									'count': 1,
									'pos': obj.ascend,
									'quality': ''}
						
						case 'heroTalent':
							to_append = {'name': to_parse.name,
									'color': to_parse.color,
									'class': to_parse.heroclass,
									'count': 1,
									'pos': obj.position,
									'quality': ''}

						case 'petTalent':
							if obj.position == 'full' or obj.position == 'gold':
								talent_pos = obj.position + ' talent'
							else:
								talent_pos = obj.position
							to_append = {'name': to_parse.name,
									'color': to_parse.color,
									'class': to_parse.petclass,
									'count': 1,
									'pos' : talent_pos,
									'quality': ''}
			
				if to_append != '':	
					found_objects[to_parse.stars].append(to_append)

	found_objects = remove_doublons(found_objects)

	if some_match:
		return found_objects
	else:
		return None



def format_results(found_objects):
	to_return = ''
	some_match = False

	for star_iter in range(0,len(found_objects)):
		if len(found_objects[star_iter]) > 0:
			some_match = True
			to_return += '### ' + stars(star_iter) + ' ###\n'
			for obj in found_objects[star_iter]:
				to_append = obj['name'] + ' (' + obj['color'] + ' ' + obj['class'] + ') '
				if obj['count'] > 1:
					to_append += 'x' + str(obj['count']) + ' '
				to_append += ': '
				
				obj_ascends = obj['pos'].split(',')
				if obj['quality'] != '' :	#spechol case de la recherche d'item sans qualité précisée
					obj_qual = obj['quality'].split(',')
					different_qualities = True
				else:
					different_qualities = False

				obj_iter = 0
				while obj_iter < len(obj_ascends):
					to_append += obj_ascends[obj_iter]
					if different_qualities:
						to_append += ' (' + obj_qual[obj_iter] + ')'
					to_append += ', '
					obj_iter += 1
	
				to_return += to_append[:-2] + '\n'

	if some_match:
		return to_return
	else:
		return None



def unique_objects(object_list, whichone):
	to_return = []
	for obj in object_list:
		match whichone:
			case 'heroclass':
				if obj.heroclass not in to_return:
					to_return.append(obj.heroclass)
			case 'petclass':
				if obj.petclass not in to_return:
					to_return.append(obj.petclass)
			case 'color':
				if obj.color not in to_return:
					to_return.append(obj.color)
			case 'species':
				if obj.species not in to_return:
					to_return.append(obj.species)

	return sorted(to_return)



def find_specific_objects(arg, object_list, whichone):
	to_return = []
	for obj in object_list:
		match whichone:
			case 'heroclass':
				if obj.heroclass == arg:
					to_return.append(obj)
			case 'petclass':
				if obj.petclass == arg:
					to_return.append(obj)
			case 'color':
				if obj.color == arg:
					to_return.append(obj)
			case 'species':
				if obj.species == arg:
					to_return.append(obj)
			case 'stars':
				if obj.stars == arg:
					to_return.append(obj)
	return to_return



def format_uniques(object_list):
	to_return = ''
	for obj in object_list:
		to_return += '- ' + obj + '\n'

	return to_return



def find_pet_talents(pet):
	m_talents = ['','','','','','','','','','','']
	full_talent = {'name':'', 'description':''}
	gold_talent = {'name':'', 'description':''}

	for t in pet.talents:
		if t.name != None:
			position = t.position.split(' ')
			if position[0] == 'base':
				base_talents = str(t.name)
			elif position[0] == 'silver':
				silver_talents = str(t.name)
			elif position[0] == 'full':
				full_talent['name'] = t.name
				if t.description != '':
					full_talent['description'] = t.description
				else:
					full_talent['description'] = ''
			elif position[0] == 'gold':
				gold_talent['name'] = t.name
				if t.description != '':
					gold_talent['description'] = t.description
				else:
					gold_description = ''
			elif position[0] == 'merge':
				m_talents[int(position[1])] = t.name
	
	return [base_talents, silver_talents, full_talent, gold_talent, m_talents]