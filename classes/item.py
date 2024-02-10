class Item:
	"""Classe des items"""


	def __init__(self, name, ascend='', quality=None):
		"""Initialise le nom et la qualité de l'item"""
		self.name = name
		self.quality = quality
		self.ascend = ascend


	def toJSON(self):
		"""renvoie l'item sous forme de JSON"""

		return self.__dict__