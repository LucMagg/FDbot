import requests
import json
import time


url = "https://discord.com/api/v10/applications/1119731541485035581/commands"

json = [{
        "name": "addcomment",
        "type": 1,
        "description": "Permet d'ajouter un commentaire sur le héros ou le pet passé en paramètre.",
        "options": [
            {
                "name": "héros_ou_pet",
                "description": "Nom du héros ou du pet",
                "type": 3,
                "required": True
            },
            {
                "name": "commentaire",
                "description": "Commentaire à ajouter sur la description du héros/pet",
                "type": 3,
                "required": True
            }]
    },
    {
        "name": "bothelp",
        "type": 1,
        "description": "Affiche le bloc d'aide des commandes disponibles.",
    },
    {
        "name": "botstats",
        "type": 1,
        "description": "Renvoie les données recensées par le bot.",
    },
    {
        "name": "class",
        "type": 1,
        "description": "Permet de lister les différents héros de la classe passée en paramètre.",
        "options": [
            {
                "name": "classe",
                "description": "Nom de la classe",
                "type": 3,
                "required": True
            }] 
    },
    {
        "name": "dhjk",
        "type": 1,
        "description": "Prie le dieu du jeu :)"
    },
    {
        "name": "hero",
        "type": 1,
        "description": "Affiche les informations du héros passé en paramètre.",
        "options": [
            {
                "name": "héros",
                "description": "Nom du héros",
                "type": 3,
                "required": True
            }] 
    },
    {
        "name": "item",
        "type": 1,
        "description": "Permet de lister les différents héros pouvant équiper l'item passé en paramètre.",
        "options": [
            {
                "name": "item",
                "description": "Nom de l'item (avec ou sans la qualité)",
                "type": 3,
                "required": True
            }] 
    },
    {
        "name": "pet",
        "type": 1,
        "description": "Affiche les informations du pet passé en paramètre.",
        "options": [
            {
                "name": "pet",
                "description": "Nom du pet",
                "type": 3,
                "required": True
            }] 
    },
    {
        "name": "petlist",
        "type": 1,
        "description": "Permet de lister les différents pets pouvant être équipés par le héros passé en paramètre.",
        "options": [
            {
                "name": "héros",
                "description": "Nom du héros",
                "type": 3,
                "required": True
            }] 
    },
    {
        "name": "talent",
        "type": 1,
        "description": "Permet de lister les différents héros et/ou pets possédant le talent passé en paramètre.",
        "options": [
            {
                "name": "talent",
                "description": "Nom du talent",
                "type": 3,
                "required": True
            }] 
    },
    {
        "name": "update",
        "type": 1,
        "description": "Permet d'update le bot à partir du wiki.",
        "options": [
            {
                "name": "type",
                "description": "Type de BDD à mettre à jour",
                "type": 3,
                "required": False,
                "choices": [
                    {"name": "Héros",
                     "value": "heroes"},
                    {"name": "Pets",
                     "value": "pets"},
                    {"name": "Tout",
                     "value": "all"}
                ]
            }
            
        ]
    }
]
    
    

# For authorization, you can use either your bot token
headers = {
    "Authorization": "Bot MTExOTczMTU0MTQ4NTAzNTU4MQ.GK140N.TMCXf29j9p51bl19yhK7ISKjVwXZdO5TZppCAY"
}

def post():
    for command in json:
        r = requests.post(url, headers=headers, json=command)
        print(r.text)
        time.sleep(2)

#def get():
r = requests.get(url, headers=headers)
print(r.text)

def delete():
    r = requests.delete(url + '/1223631277530288200', headers=headers)
    print(r.text)