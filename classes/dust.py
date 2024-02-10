class Dust_conv:
	"""Sous-classe des conversions de dust"""


	def __init__(self,name,quantity):
		self.name = name
		self.quantity = quantity



class Conversion(Dust_conv):
	"""Classe des conversions des dust"""


	def __init__(self,p_input,p_output):
		self.p_input = p_input
		self.p_output = p_output



class Price:
	"""Classe des prix en gemmes"""


	def __init__(self, price, quantity):
		self.price = price
		self.quantity = quantity



class Dust(Conversion, Price):
	"""Classe des dust"""


	def __init__(self, name, icon, conversion, price_in_gems):
		"""Initialise le nom du talent"""
		self.name = name
		self.icon = icon
		self.conversion = conversion
		self.price_in_gems = price_in_gems