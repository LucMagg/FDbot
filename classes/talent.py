class Talent:
	"""Classe des talents"""


	def __init__(self, name, position = '', description = '',bonus_count = 0, bonus_type = ''):
		"""Initialise le nom du talent"""
		self.name = name
		self.position = position
		self.description = description
		self.bonus_count = bonus_count
		self.bonus_type = bonus_type


	def toJSON(self):
		"""renvoie le talent sous forme de JSON"""

		return self.__dict__