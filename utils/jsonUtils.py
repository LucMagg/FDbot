import json
import os

def exportInJson(my_dict,filename,path):
	"""exporte my_dict dans un json nommé filename dans le répertoire path"""

	json_object = json.dumps(my_dict, sort_keys=True, indent=4)
	with open(os.path.join(path,filename),'w') as outfile:
		outfile.write(json_object)



def importFromJson(filename,path):
	"""retourne le json filename du répertoire path"""

	with open(os.path.join(path,filename)) as inputfile:
		return json.load(inputfile)