import discord
from utils.spireUtils import process_pic


from utils.miscUtils import get_discord_color


def get_spire(msg, pj, author, guild, bracket, spire_scores, bot_commands):
    
    print(author)
    img_url = msg.data['resolved']['attachments'][pj]['url']
    result = process_pic(img_url)
    result['name'] = author
    result['guild'] = guild
    result['bracket'] = bracket


    print(result)
            
    description = 'score: ' + str(result['score']) + '\n' 
    description += 'étages terminés: ' + str(result['floors']) + '\n'
    description += 'pertes: ' + str(result['loss']) + '\n'
    description += 'tours: ' + str(result['turns']) + '\n'
    description += 'bonus: ' + str(result['bonus']) + ' (soit ' + str(result['bonus']*250) + ')\n'
    description += guild
    description += bracket

    return discord.Embed(title='This is a TEST',
                         description=description,
                         color=get_discord_color(bot_commands['update']['color'])).set_image(url=img_url)