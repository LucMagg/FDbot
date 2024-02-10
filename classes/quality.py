from .dust import Dust_conv


class Recycling(Dust_conv):
	"""Classe des recyclages d'objets"""


	def __init__(self, dust, gold):
		self.dust = dust
		self.gold = gold
		
		

class Quality(Recycling):
	"""Classe des qualités d'objets"""


	def __init__(self, name, icon, price, discount_price, recycling):
		self.name = name
		self.icon = icon
		self.price = int(price)
		self.discount_price = discount_price
		self.recycling = recycling



