import requests
from bs4 import BeautifulSoup
from .pathUtils import *
from .jsonUtils import *
from .loadBDD import *
from .miscUtils import str_now

from classes.hero import *
from classes.pet import *
from classes.talent import *
from classes.item import *


base_url = 'https://friends-and-dragons.fandom.com/wiki/'
raw_data = ''

my_json = 'wikiSchemas.json'
my_path = add_rep_to_parent('JSON')
wiki_schemas = importFromJson(my_json,my_path)

def update_bdd(urls, heroes, pets):
    heroes_updated = False
    pets_updated = False
    for url in urls:
        urlToParse = base_url + url
        match url:
            case 'Hero_Gear':
                get_hero_gear(urlToParse, url, heroes)
                print(f'done {url}')
                heroes_updated = True
            case 'Hero_Talents':
                get_hero_talents(urlToParse, url, heroes)
                print(f'done {url}')
                heroes_updated = True
            case 'Hero_Stats':
                get_hero_stats(urlToParse, url, heroes)
                print(f'done {url}')
                heroes_updated = True
            case 'Pet_Stats':
                get_pet_stats(urlToParse, url, pets)
                print(f'done {url}')
                pets_updated = True
            case 'Pet_Talents':
                get_pet_talents(urlToParse, url, pets)
                print(f'done {url}')
                pets_updated = True

    if heroes_updated:
        updated = []
        for hero in heroes:
            to_append = {}
            to_append = hero.toJSON()

            h_talents = []
            for t in hero.talents:
                h_talents.append(t.toJSON())
            to_append['talents'] = h_talents
                                                     
            h_gear = []
            for g in hero.gear:
                h_gear.append(g.toJSON())
            to_append['gear'] = h_gear
            
            h_comments = []
            for comment in hero.comments:
                h_comments.append(comment.toJSON())
            to_append['comments'] = h_comments
                                        
            updated.append(to_append)

        exportInJson(updated, 'hero.json', my_path)
        heroes = get_heroes()
        print(f'[{str_now()}] --- Héros OK')

    if pets_updated:
        updated = []
        for pet in pets:
            to_append = {}
            to_append = pet.toJSON()

            p_talents = []
            for t in pet.talents:
                p_talents.append(t.toJSON())
            to_append['talents'] = p_talents
            
            p_comments = []
            for comment in pet.comments:
                p_comments.append(comment.toJSON())
            to_append['comments'] = p_comments
                                        
            updated.append(to_append)

        exportInJson(updated, 'pet.json', my_path)
        pets = get_pets()
        print(f'[{str_now()}] --- Pets OK')
    

def get_parsed_data(url):
    page = requests.get(f'{url}')
    return BeautifulSoup(page.content, 'html.parser').find_all('tr')[1:]


def get_hero_gear(url, whichone, heroes):
    updated_heroes = get_updated_objects(get_parsed_data(url), whichone)
    heroes = update_heroes(updated_heroes, heroes)


def get_hero_talents(url, whichone, heroes):
    updated_heroes = get_updated_objects(get_parsed_data(url), whichone)
    heroes = update_heroes(updated_heroes, heroes)


def get_hero_stats(url, whichone, heroes):
    updated_heroes = get_updated_objects(get_parsed_data(url), whichone)
    heroes = update_heroes(updated_heroes, heroes)


def get_pet_stats(url, whichone, pets):
    updated_pets = get_updated_objects(get_parsed_data(url), whichone)
    pets = update_pets(updated_pets, pets)


def get_pet_talents(url, whichone, pets):
    updated_pets = get_updated_objects(get_parsed_data(url), whichone)
    pets = update_pets(updated_pets, pets)


def get_updated_objects(rawdata, whichone):
    to_return = []
    schema = wiki_schemas[whichone]

    for tr in rawdata:
        td = tr.find_all('td')
        to_add = {}
        ascend = ''
        talents = []

        for item in schema:
            if type(item['row']) is list:
                if ascend == '':
                    if item['type'] == 'number':
                        i = 0
                        while i < len(item['row']):
                            property = item['property']['base'] + item['property']['then'][i]
                            to_add[property] = from_td_to_object(td[item['row'][i]], item)
                            i+=1
                    else:
                        i = 0
                        while i < len(item['row']):
                            property = item['property'] + ' ' + str(i+1)
                            to_add[property]= from_td_to_object(td[item['row'][i]], item)
                            i+=1
                else:
                    gears = []
                    i = 0
                    while i < len(item['row']):
                        to_add['ascend'] = ascend
                        item_answer = from_td_to_object(td[item['row'][i]], item)

                        to_add['name'] = item_answer['name']
                        if to_add['name'] != None:
                            to_add['name'] = to_add['name'].replace('\n','')
                            if to_add['name'][0] == ' ':
                                to_add['name'] = to_add['name'][1:]

                        to_add['quality'] = item_answer['quality']
                        gears.append({'ascend': ascend, 'name': to_add['name'], 'quality': to_add['quality']})
                        i+=1

            elif item['schema'] == 'lead':
                lead_answer = from_td_to_object(td[item['row']], item)
                if lead_answer != {}:
                    for key in lead_answer.keys():
                        to_add[key] = lead_answer.get(key)

            elif item['schema'] == 'talent':
                if item['property'] != 'full':
                    talent_list = from_td_to_object(td[item['row']], item)

                    if item['property'] == 'base':
                        to_fill = 6
                    else:
                        to_fill = 3
                    while len(talent_list) < to_fill:
                        talent_list.append(None)

                    i = 0
                    while i < len(talent_list):
                        asc = item['property'] + ' ' + str(i+1)
                        talents.append(Talent(position=asc, name=talent_list[i]))
                        i+=1
                else:
                    if td[item['row']].get_text() != '':
                        to_add['full'] = from_td_to_object(td[item['row']], item)[0]
                    else:
                        to_add['full'] = None
                    

            else:
                if item['property'] != 'ascend':
                    to_add[item['property']] = from_td_to_object(td[item['row']], item)
                else:
                    ascend = from_td_to_object(td[item['row']], item)
                    match ascend:
                        case 'Basic': ascend = 'A0'
                        case '1st': ascend = 'A1'
                        case '2nd': ascend = 'A2'
                        case '3rd': ascend = 'A3'

        if whichone == 'Hero_Gear':
            to_append = {}
            to_append['name'] = to_add['heroname']

            try:
                if any(d['name'] == to_add['heroname'] for d in to_return):
                    to_update = next((sub for sub in to_return if sub['name'] == to_add['heroname']), None)
                    for gear in gears:
                        items.append(Item(ascend=gear['ascend'], name=gear['name'], quality=gear['quality']))
                else:
                    items = []
                    for gear in gears:
                        items.append(Item(ascend=gear['ascend'], name=gear['name'], quality=gear['quality']))
                    to_return.append({'name': to_add['heroname'], 'gear': items})    
            except:
                items = []
                for gear in gears:
                    items.append(Item(ascend=gear['ascend'], name=gear['name'], quality=gear['quality']))
                to_return.append({'name': to_add['heroname'], 'gear': items})
            
        elif whichone == 'Hero_Talents':
            to_add['talents'] = talents
            to_return.append(to_add)

        elif whichone == 'Pet_Talents':
            talents = []
            keys_to_del = []
            for key in to_add.keys():
                if key != 'name' and key != 'image_url':
                    talents.append(Talent(position=key, name=to_add[key]))
                    keys_to_del.append(key)
            to_add['talents'] = talents

            for key in keys_to_del:
                del to_add[key]

            to_return.append(to_add)
            

        else:
            to_return.append(to_add)
    
    return to_return


def from_td_to_object(td, schema):
    match schema['schema']:
        case 'name':
            to_return = td.get_text()
            if 'File:' in to_return: #exception du nom du perso sans image dans la table du Fandom Wiki
                to_return = td.find('a').get_text().split('File:')[1].split(' Portrait')[0]
            while '  ' in to_return:
                to_return = to_return.replace('  ',' ')
            while ' - ' in to_return:
                to_return = to_return.replace(' - ','-')
            to_return_len = int(len(to_return)/2)
            if to_return[:to_return_len] == to_return[to_return_len:]:
                to_return = to_return[:to_return_len]
        
        case 'portrait':
            to_return = td.find('a')['href']
            if 'wiki/Special' in to_return:
                to_return = 'None'
            
        case 'a.title':
            to_return =  td.find('a')['title']
            if 'File:' in to_return:
                if 'Class' in to_return:
                    to_return = to_return.split('File:Class')[1].split('.png')[0]
                else:
                    to_return = to_return.split('File:Trait')[1].split('.png')[0]

        case 'a.title./':
            to_return = ''
            for a in td.find_all('a'):
                to_return += a['title'] + '/'
            to_return = to_return[:-1]

        case 'text':
            to_return = td.get_text()
            if '\n' in to_return:
                to_return = to_return.replace('\n','')
            to_return.replace('  ',' ')

        case 'lead':
            to_return = {}
            base_key = schema['property']
            td_text = td.get_text()

            if 'att' in td_text:
                to_return[base_key + '_att'] = td_text.split('att')[0].split('x')[1]
                while ' ' in to_return[base_key + '_att']:
                    to_return[base_key + '_att'] = to_return[base_key + '_att'].replace(' ','')
            if 'def' in td_text:
                if 'att' in td_text:
                    splitted = td.text.split('att')[1]
                else:
                    splitted = td_text
                to_return[base_key + '_def'] = splitted.split('def')[0].split('x')[1]
                while ' ' in to_return[base_key + '_def']:
                    to_return[base_key + '_def'] = to_return[base_key + '_def'].replace(' ','')

            a = td.find_all('a')
            if len(a) > 0:
                if len(a) == 1 and 'att' in td_text:
                    to_return[base_key + '_color'] = a[0]['title']
                elif len(a) == 1 and not('att') in td_text:
                    to_return[base_key + '_species'] = a[0]['title']
                elif len(a) == 2 and 'att' in td_text:
                        to_return[base_key + '_color'] = a[0]['title']
                        to_return[base_key + '_species'] = a[1]['title']
                elif len(a) == 2 and 'for' in td_text:
                        to_return[base_key + '_talent'] = a[0]['title']
                        to_return[base_key + '_species'] = a[1]['title']

        case 'item':
            to_return = {}
            td_text = td.get_text()
            if td_text != '':
                to_return['quality'] = td_text.split(' ')[0]
                to_return['name'] = td_text.replace(to_return['quality'], '')
                while '  ' in to_return['name']:
                    to_return['name'] = to_return['name'].replace('  ', ' ')
            else:
                to_return['name'] = None
                to_return['quality'] = None

        case 'talent':
            to_return = []
            for a in td.find_all('a'): 
                tal = a['href'].split('.png')[0]
                if a['class'] == ['image']:
                    talName = tal.split('/')
                    talent = talName[len(talName)-1][5:]
                else:
                    talName = tal.split('=')
                    talent = talName[1][5:]

                if '%26' in talent:
                    talent = '&'.join(talent.split('%26'))

                i = 1
                while i < len(talent):
                    if talent[i] == str.upper(talent[i]):
                        talent = talent[0:i] + ' ' + talent[i:]
                        i+=1
                    i+=1

                if 'of' in talent:
                    talent = ' of '.join(talent.split('of'))
                if 'to ' in talent:
                    talent = ' to '.join(talent.split('to '))
                talent = talent.replace('  ', ' ')

                to_return.append(talent)

                
    return to_return


def update_heroes(updated_heroes, db):
    for hero in updated_heroes:
        h_to_update = [item for item in db if item.name == hero['name']]

        if len(h_to_update) == 1:
            h_to_update = h_to_update[0]
            is_a_new_hero = False
        else:
            h_to_update = Hero(name=hero['name'])
            is_a_new_hero = True

        if hero.get('image_url') and hero['image_url'] != 'None':
            h_to_update.image_url = hero['image_url']
        if hero.get('heroclass'):
            h_to_update.heroclass = hero['heroclass']
        if hero.get('color'):
            h_to_update.color = hero['color']
        if hero.get('species'):
            h_to_update.species = hero['species']
        if hero.get('stars'):
            h_to_update.stars = int(hero['stars'])
            if hero.get('attack100'):
                h_to_update.ascend_max = int(hero['stars']) + 3
            else:
                h_to_update.ascend_max = int(hero['stars']) + 2
        if hero.get('type'):
            h_to_update.type = hero['type']
        if hero.get('pattern'):
            h_to_update.pattern = hero['pattern']
        if hero.get('attack75'):
            h_to_update.attack75 = int(hero['attack75'])
        if hero.get('attack85'):
            h_to_update.attack85 = int(hero['attack85'])
        if hero.get('attack95'):
            h_to_update.attack95 = int(hero['attack95'])
        if hero.get('attack100'):
            h_to_update.attack100 = int(hero['attack100'])
        if hero.get('defense75'):
            h_to_update.defense75 = int(hero['defense75'])
        if hero.get('defense85'):
            h_to_update.defense85 = int(hero['defense85'])
        if hero.get('defense95'):
            h_to_update.defense95 = int(hero['defense95'])
        if hero.get('defense100'):
            h_to_update.defense100 = int(hero['defense100'])
        if hero.get('talents'):
            h_to_update.talents = hero['talents']
        if hero.get('gear'):
            h_to_update.gear = hero['gear']
        if hero.get('lead_bonus_color'):
            h_to_update.lead_bonus_color = hero['lead_bonus_color']
        if hero.get('lead_bonus_species'):
            h_to_update.lead_bonus_species = hero['lead_bonus_species']
        if hero.get('base_IA'):
            h_to_update.base_IA = hero['base_IA']
                       
        if is_a_new_hero:
            db.append(h_to_update)

    return db


def update_pets(updated_pets, db):
    for pet in updated_pets:
        p_to_update = [item for item in db if item.name == pet['name']]

        if len(p_to_update) == 1:
            p_to_update = p_to_update[0]
            is_a_new_pet = False
        else:
            p_to_update = Pet(name=pet['name'])
            is_a_new_pet = True
           
        if pet.get('image_url') and pet['image_url'] != 'None':
            p_to_update.image_url = pet['image_url']
        if pet.get('stars'):
            p_to_update.stars = int(pet['stars'])
        if pet.get('petclass'):
            p_to_update.petclass = pet['petclass']
        if pet.get('color'):
            p_to_update.color = pet['color']
        if pet.get('signature'):
            p_to_update.signature = pet['signature']
        if pet.get('signature_bis'):
            p_to_update.signature_bis = pet['signature_bis']
        if pet.get('attack'):
            p_to_update.attack = int(pet['attack'])
        if pet.get('defense'):
            p_to_update.defense = int(pet['defense'])
        if pet.get('manacost'):
            p_to_update.manacost = int(pet['manacost'])
        if pet.get('talents'):
            p_to_update.talents = pet['talents']

        if is_a_new_pet:
            db.append(p_to_update)

    return db