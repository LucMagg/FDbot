import discord

from itertools import cycle
from discord.ext import tasks
from utils.miscUtils import str_now
from utils.loadBDD import *
from commands.mainCommand import *


print(f'[{str_now()}] Récupération des BDD')
heroes = get_heroes()
print(f'[{str_now()}] --- Héros OK')
pets = get_pets()
print(f'[{str_now()}] --- Pets OK')
talents = get_talents()
print(f'[{str_now()}] --- Talents OK')
dusts = get_dusts()
print(f'[{str_now()}] --- Poussières OK')
qualities = get_qualities()
print(f'[{str_now()}] --- Qualités OK')
bot_commands = get_messages()
print(f'[{str_now()}] --- Messages du bot OK')


print (f'[{str_now()}] Démarrage du bot...')
bot_key = 'MTExOTczMTU0MTQ4NTAzNTU4MQ.GK140N.TMCXf29j9p51bl19yhK7ISKjVwXZdO5TZppCAY'
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = discord.Client(intents=intents)
status = cycle(['tuer les 5* de Jneb','tchitchi Lars','faire des Kronkeries','soit oui, Soanon','vénérer Tob','mâcher les gants usagés de Procto','prêcher le dhjkisme'])

@tasks.loop(seconds=30)
async def change_status():
	await client.change_presence(activity=discord.Game(next(status)))


@client.event
async def on_ready():
	change_status.start()
	print(f'[{str_now()}] Bot loggé sous {client.user}')


@client.event
async def on_message(msg):
    if msg.author == client.user:
        return

    if msg.content.startswith('/'):
        msg_split = msg.content.split(" ")
        command = str.lower(msg_split[0][1:])

        i = 0
        args = ""
        while i < len(msg_split):
            if i > 0:
                args += msg_split[i] + " "
            i += 1
        args = args[:-1]

        print(f'[{str_now()}] [COMMAND ] commande {command} entrée par {msg.author} dans le chan {msg.channel} du serveur {msg.guild.name} (arguments = {args})')

        return_msg = await main_command(msg, command, args, heroes, pets, talents, dusts, qualities, bot_commands)

        await return_msg[0].edit(embed=return_msg[1])
            
        print(f'[{str_now()}] [COMMAND ] commande {command} exécutée avec succès')

client.run(token=bot_key, reconnect=False)