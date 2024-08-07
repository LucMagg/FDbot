import requests
import json
import time
import os
from dotenv import load_dotenv


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
    },
    {
        "name": "spire",
        "type": 1,
        "description": "Permet d'envoyer ton score en spire.",
        "options": [
            {
                "name": "screenshot",
                "description": "Screenshot de ton résultat sur la spire",
                "type": 11,
                "required": True
            },
            {
                "name": "guilde",
                "description": "Ta guilde",
                "type": 3,
                "required": True,
                "choices": [
                    {"name": "Bordeciel",
                     "value": "Bordeciel"},
                    {"name": "Brainless",
                     "value": "Brainless"},
                    {"name": "Café noir",
                     "value": "Café noir"},
                    {"name": "DragonFR",
                     "value": "DragonFR"},
                    {"name": "Échec&Malt",
                     "value": "Échec&Malt"},
                    {"name": "[FR]acasse",
                     "value": "[FR]acasse"},
                    {"name": "Frenchies",
                     "value": "Frenchies"},
                    {"name": "FrenchWar",
                     "value": "FrenchWar"},
                    {"name": "[FR]omage",
                     "value": "[FR]omage"},
                    {"name": "fr_viking",
                     "value": "fr_viking"},
                    {"name": "KaamelottFr",
                     "value": "KaamelottFr"},
                    {"name": "Révolte",
                     "value": "Révolte"},
                    {"name": "SoleilVertFR",
                     "value": "SoleilVertFR"},
                    {"name": "TheGuildHall",
                     "value": "TheGuildHall"},
                    {"name": "VeniVidiWipe",
                     "value": "VeniVidiWipe"}
                ]
            },
            {
                "name": "spire",
                "description": "Ton niveau de spire",
                "type": 3,
                "required": True,
                "choices": [
                    {"name": "Aventurier",
                     "value": "Adventurer"},
                    {"name": "Héros",
                     "value": "Hero"},
                    {"name": "Bronze",
                     "value": "Bronze"},
                    {"name": "Argent",
                     "value": "Silver"},
                    {"name": "Or",
                     "value": "Gold"},
                    {"name": "Platine",
                     "value": "Platinum"}
                ]
            }
        ]
    }
]
    
load_dotenv()
url = os.getenv('DISCORD_API_URL')
bot_key = os.getenv('BOT_KEY')

headers = {
    "Authorization": "Bot " + bot_key
}

#def post():
for command in json:
    r = requests.post(url, headers=headers, json=command)
    print(r.text)
    time.sleep(2)

def get():
    r = requests.get(url, headers=headers)
    print(r.text)

def delete():
    r = requests.delete(url + '/1258048932404002900', headers=headers)
    print(r.text)