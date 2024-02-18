import json

from math import *

from .talent import *
from .comment import *
from .item import *
from .pet import *
from utils.findUtils import find_match_names


class Hero(Item,Talent,Comment):
	"""Classe des héros"""


	def __init__(self, name, stars, ascend_max, heroclass, species, color, attack, defense, talents, gear, comments, lead_bonus_color, lead_bonus_species, base_IA, image_url, pet):
		"""Initialise le héros"""
		self.name = name
		self.stars = int(stars)
		self.ascend_max = int(ascend_max)
		self.heroclass = heroclass
		self.species = species
		self.color = color
		self.attack = int(attack)
		self.defense = int(defense)
		self.talents = talents
		self.gear = gear
		self.comments = comments
		self.lead_bonus_color = lead_bonus_color
		self.lead_bonus_species = lead_bonus_species
		self.base_IA = base_IA
		self.image_url = image_url
		self.pet = pet


	def toJSON(self):
		"""renvoie l'item sous forme de JSON"""

		return self.__dict__


	def ascend(cls):
		"""renvoie l'ascend max du héros"""

		return cls.ascend_max - cls.stars


	def lvl_max(cls):
		"""renvoie le lvl max du héros"""

		if cls.ascend() == 2:
			return 95
		else:
			return 100


	def att_gear(cls):
		"""renvoie le bonus d'attaque du full stuff"""

		return ceil(cls.attack * 5 / 100 * cls.ascend())


	def att_merge(cls):
		"""renvoie le bonus d'attaque du full merge"""

		return ceil(cls.attack * 15 / 100)


	def att_pet_boost(cls, pets):
		"""renvoie le bonus du pet signature du héros s'il y en a un, sinon renvoie 0"""

		if cls.pet != None:
			return ceil(cls.attack * find_match_names(cls.pet,pets).attack / 100)
		else:
			return 0


	def att_max(cls, pets):
		"""renvoie l'attaque max du héros full stuff/merge et avec son pet"""

		return cls.attack + cls.att_gear() + cls.att_merge() + cls.att_pet_boost(pets)


	def def_gear_merge(cls):
		"""renvoie le bonus de def du full stuff ou merge (même calcul)"""

		return ceil(cls.defense * 15 / 100)


	def def_pet_boost(cls, pets):
		"""renvoie le bonus du pet signature du héros s'il y en a un, sinon renvoie 0"""

		if cls.pet != None:
			return ceil(cls.defense * find_match_names(cls.pet,pets).defense / 100)
		else:
			return 0


	def def_max(cls, pets):
		"""renvoie la def max du héros full stuff/merge et avec son pet"""

		return cls.defense + cls.def_gear_merge() * 2 + cls.def_pet_boost(pets)