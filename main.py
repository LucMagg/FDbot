import discord
from time import time
from discord import app_commands

from itertools import cycle
from discord.ext import tasks, commands
from utils.miscUtils import str_now
from utils.loadBDD import *
from commands.mainCommand import *
from utils.loggerUtils import *


uptime = time()
print(uptime)
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
loggerData = readLogger()
print(f'[{str_now()}] --- Logger OK')


print (f'[{str_now()}] Démarrage du bot...')
bot_key = 'MTExOTczMTU0MTQ4NTAzNTU4MQ.GK140N.TMCXf29j9p51bl19yhK7ISKjVwXZdO5TZppCAY'
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(intents=intents, command_prefix='/')
status = cycle(['tuer les 5* de Jneb','tchitchi Lars','faire des Kronkeries','soit oui, Soanon','vénérer Tob','mâcher les gants usagés de Procto','prêcher le dhjkisme'])

@tasks.loop(seconds=30)
async def change_status():
	await bot.change_presence(activity=discord.Game(next(status)))


@bot.event
async def on_ready():
    global uptime
    print(uptime)
    change_status.start()
    print(f'[{str_now()}] Bot loggé sous {bot.user}')


@bot.event
async def on_disconnect():
    global uptime
    try:
        totalUptime = time() - uptime
        loggerData['uptime'] += totalUptime
        writeLogger(loggerData)
    except:
        pass

        
#COMMANDS
@bot.tree.command(name="addcomment")
async def command_addcomment(interaction: discord.Interaction):
    await on_command(interaction)
@bot.tree.command(name="bothelp")
async def command_bothelp(interaction: discord.Interaction):
    await on_command(interaction)
@bot.tree.command(name="botstats")
async def command_botstats(interaction: discord.Interaction):
    await on_command(interaction)
@bot.tree.command(name="class")
async def command_class(interaction: discord.Interaction):
    await on_command(interaction)
@bot.tree.command(name="dhjk")
async def command_dhjk(interaction: discord.Interaction):
    await on_command(interaction)
@bot.tree.command(name="hero")
async def command_hero(interaction: discord.Interaction):
    await on_command(interaction)
@bot.tree.command(name="item")
async def command_item(interaction: discord.Interaction):
    await on_command(interaction)
@bot.tree.command(name="pet")
async def command_pet(interaction: discord.Interaction):
    await on_command(interaction)
@bot.tree.command(name="petlist")
async def command_petlist(interaction: discord.Interaction):
    await on_command(interaction)
@bot.tree.command(name="talent")
async def command_talent(interaction: discord.Interaction):
    await on_command(interaction)


async def on_command(msg):
    global uptime
    command = msg.data['name']
    args = ''
    try:
        for arg in msg.data['options']:
            args += ' ' + arg['value']
        args = args[1:]
    except:
        pass    

    print(f'[{str_now()}] [COMMAND ] commande {command} entrée par {msg.user} dans le chan {msg.channel} du serveur {msg.guild.name} (arguments = {args})')
    await msg.response.send_message(embed=main_command(msg, command, args, heroes, pets, talents, dusts, qualities, bot_commands))
    print(f'[{str_now()}] [COMMAND ] commande {command} exécutée avec succès')
    loggerData['message_count'] += 1
    totalUptime = time() - uptime
    uptime = time()
    loggerData['uptime'] += totalUptime
    writeLogger(loggerData)

bot.run(token=bot_key)