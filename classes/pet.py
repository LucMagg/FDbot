from .talent import *
from .comment import *


class Pet(Talent, Comment):
	"""Classe des pets"""

	def __init__(self,name, stars, petclass, color, signature, signature_bis, attack, defense, manacost, talents, comments, image_url):
		"""Initialise le pet"""
		self.name = name
		self.stars = int(stars)
		self.petclass = petclass
		self.color = color
		self.signature = signature
		self.signature_bis = signature_bis
		self.attack = int(attack)
		self.defense = int(defense)
		self.manacost = int(manacost)
		self.talents = talents
		self.comments = comments
		self.image_url = image_url


	def toJSON(self):
		"""renvoie le pet sous forme de JSON"""

		return self.__dict__