from .jsonUtils import *
from .pathUtils import *

my_json = 'logger.json'
my_path = add_rep_to_parent('JSON')


def readLogger(): 
    to_return = importFromJson(my_json, my_path)
    return to_return


def writeLogger(loggerData):
    exportInJson(loggerData, my_json, my_path)