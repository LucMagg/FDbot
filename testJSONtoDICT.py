from jsonUtils import *
from pathUtils import *

mydict = importFromJson('dust.json',add_rep_to_parent('JSON'))

print(mydict[1])