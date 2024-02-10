import os

def pathname():
	"""renvoie le répertoire courant"""

	return os.path.dirname(__file__)


def parent_path():
	"""renvoie le répertoire parent du répertoire courant"""

	return os.path.abspath(os.path.join(pathname(),os.pardir))


def add_rep(rep):
	"""renvoie le sous-répertoire *rep* du répertoire courant"""

	return os.path.join(pathname(),rep)

def add_rep_to_parent(rep):
	"""renvoie le sous-répertoire *rep* du répertoire parent du répertoire courant"""

	return os.path.join(parent_path(),rep)