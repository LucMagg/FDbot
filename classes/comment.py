class Comment:
	"""Classe des commentaires"""


	def __init__(self,author,date,commentaire):
		"""Initialise le commentaire"""
		self.author = author
		self.date = date
		self.commentaire = commentaire


	def toJSON(self):
		"""renvoie le commentaire sous forme de JSON"""

		return self.__dict__