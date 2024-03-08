from jsonUtils import *
from pathUtils import *

def quality():
	quality_name = 'Magic','Epic','Mythic','Legendary','Exalted','Divine','Radiant','Brilliant','Coruscating','Incandescent'
	quality_icon = ':blue_circle:',':purple_circle:',':yellow_circle:',':red_circle:',':green_circle:',':orange_circle:',':purple_circle:',':yellow_circle:',':red_circle:',':orange_circle:'
	quality_price = 20,200,750,1500,2500,4950,200,1000,1800,2500
	quality_discount_price = 10,100,375,750,1000,1980,None,None,None,None
	quality_recycling_gold = 250,1000,2500,10000,25000,50000,1000,2500,10000,None
	quality_recycling_dust = 10,25,20,15,10,5,25,20,15,None
	quality_recycling_dust_name = 'Epic','Epic','Mythic','Legendary','Exalted','Divine','Epic','Mythic','Legendary',None

	quality_list = []
	iter = 0

	while iter < len(quality_name):
		quality = {
			'name': quality_name[iter],
			'icon': quality_icon[iter],
			'price': quality_price[iter],
			'discount_price': quality_discount_price[iter],
			'recycling':{
				'gold': quality_recycling_gold[iter],
				'dust':{
					'quantity': quality_recycling_dust[iter],
					'name': quality_recycling_dust_name[iter]
				}
			}
		}
		quality_list.append(quality)
		iter +=1
	
	exportInJson(quality_list,'quality.json',add_rep_to_parent('JSON'))



	
def dust():
	dust_name = 'Epic','Mythic','Legendary','Exalted','Divine'
	dust_icon = ':purple_circle:',':yellow_circle:',':red_circle:',':green_circle:',':orange_circle:'
	dust_price_gems = 125,375,750,1250,2500
	dust_price_gems_quantity = 50,50,50,50,50
	dust_conversion_input_quantity = None,1500,1250,None,None
	dust_conversion_input_name = None,'Epic','Mythic',None,None
	dust_conversion_output_quantity = None,50,50,None,None
	dust_conversion_output_name = None,'Mythic','Legendary',None,None

	dust_list = []
	iter = 0

	while iter < len(dust_name):
		dust = {
			'name': dust_name[iter],
			'icon': dust_icon[iter],
			'price_in_gems':{
				'price': dust_price_gems[iter],
				'quantity': dust_price_gems_quantity[iter]
			},
			'conversion':{
				'input':{
					'quantity': dust_conversion_input_quantity[iter],
					'name':dust_conversion_input_name[iter]
				},
				'output':{
					'quantity': dust_conversion_output_quantity[iter],
					'name':dust_conversion_output_name[iter]
				}
			}
		}
		dust_list.append(dust)
		iter +=1
	exportInJson(dust_list,'dust.json',add_rep_to_parent('JSON'))


def messages():
	messages = {
		'help': {
			'title': {
				'generic':'Aide du bot discord de Friends & Dragons FR',
				'command' :'Aide de la commande /'
			},
			'color': 'default',
			'description': {
				'addcomment': 'Cette commande permet d\'ajouter un commentaire sur le héros ou le pet passé en paramètre.\n' +
							  'Il est possible de laisser jusqu\'à 3 commentaires différents par héros/pet.\n' +
				              'Cependant, si vous avez déjà laissé un commentaire sur le héros/pet en question, il sera simplement mis à jour et non ajouté en tant que commentaire supplémentaire.\n' +
				              'Si le héros/pet en question a déjà 3 commentaires et que vous n\'en aviez jamais laissé un, alors c\'est le plus ancien commentaire qui sera remplacé par le vôtre :wink:\n' +
				              'Exemple de commande valide : /addcomment Adana blablabla blablabla.',
				'class': 'Cette commande permet de lister les différents héros de la classe passée en paramètre.\n' +
						 'Exemple de commande valide : /class Rogue\n\n' +
						 'Les différentes classes recensées sont :\n',
				'generic': 'Voici les différentes commandes disponibles pour le bot :\n\n' +
				           '- /addcomment [NomDuHéros][Commentaire] : permet d\'ajouter un commentaire sur le héros en question\n' +
						   '- /class [NomDeLaClasse] : affiche les héros de la classe passée en paramètre\n' +
						   '- /bothelp : affiche ce bloc d\'aide \n' +
						   '- /hero [NomDuHéros] : affiche les informations du héros passé en paramètre\n' +
						   '- /item [NomDeL\'item] : affiche les héros pouvant équiper l\'item passé en paramètre\n' +
						   '- /pet [NomDuPet] : affiche les informations du pet passé en paramètre\n' +
						   '- /petlist [NomDuHéros] : affiche les pets pouvant être équipés avec le héros passé en paramètre\n' +
						   '- /talent [NomDuTalent] : affiche la liste des héros possédant le talent passé en paramètre\n'
						   '- /update : met à jour le bot\n\n' +
						   'À noter que chacunes des commandes ci-dessus ont un paramètre "help" pour plus d\'info, et qu\'elles ne sont (pour l\'instant) disponibles qu\'en anglais :wink:',
				'hero': 'Cette commande renvoie les caractéristiques suivantes du héros passé en paramètre :\n' +
						'- Le nombre d\'étoiles, la couleur, la classe, l\'espèce, l\'ascend max et le lvl max\n' +
						'- Les attributs à l\'ascend max (attaque et défense), le classement par rapport aux autres héros de la même classe et l\'orientation offensive (ratio attaque/défense)\n' +
						'- Le(s) bonus de leader\n' +
						'- Les talents de base, d\'ascend et de merge s\'il y en a, et le(s) talent(s) unique(s) à la classe s\'il y en a\n' +
						'- La liste des équipements utilisés en fonction de l\'ascend du héros\n' +
						'- Le pet signature et ses bonus/talents s\'il existe\n' +
						'- Le(s) commentaire(s) laissé(s) par les joueurs à propos de ce héros. Vous pouvez vous-même laisser un commentaire si vous le souhaitez via la commande /addcomment (/addcomment help pour + d\'infos :wink:)\n\n' +
						'Exemple de commande valide : /hero Sandor',
				'item': 'Cette commande permet de lister les différents héros pouvant équiper l\'item passé en paramètre.\n' +
						  'Les héros en question sont classés par étoile, et le nombre d\'occurences de l\'item est repris.\n'+
						  'Si la qualité de l\'item n\'est pas indiquée, alors tous les héros pouvant équiper cette catégorie d\'item seront listés\n' +
						  'Exemple de commande valide : /item Exalted Dagger ou /item Dagger',
				'pet': 'Cette commande renvoie les caractéristiques suivantes du pet passé en paramètre :\n' +
					   '- La couleur, le nombre d\'étoiles et la classe privilégiée du pet\n' +
					   '- Le bonus d\'attribut au niveau max (en %)\n'+
					   '- Le(s) héros signature, ainsi que les autres héros pouvant profiter du bonus (même couleur, même classe)\n' +
					   '- Les talents de base, de merge, de classe et le gold talent avec son coût en mana\n'+
					   '- Le(s) commentaire(s) laissé(s) par les joueurs à propos de ce pet. Vous pouvez vous-même laisser un commentaire si vous le souhaitez via la commande /addcomment (/addcomment help pour + d\'infos :wink:)\n\n' +
					   'Exemple de commande valide : /pet Almond',
				'petlist': 'Cette commande permet de lister les différents pets pouvant être équipés par le héros passé en paramètre.\n' +
						   'Les pets en question sont classés par étoile, en indiquant les bonus correspondants, ainsi que le coût en mana s\'il s\'agit du talent gold.\n\n' +
						   'Exemple de commande valide : /petlist Sandor',
				'talent': 'Cette commande permet de lister les différents héros et/ou pets possédant le talent passé en paramètre.\n' +
						  'La liste est classée par étoile, et le nombre d\'occurences du talent est repris.\n\n' +
						  'Exemple de commande valide : /talent Tumble',
				'update': 'Cette commande sert à mettre à jour le bot depuis le site du Fandom Wiki (https://friends-and-dragons.fandom.com/wiki/)\n\n' +
						  'Les différents paramètres possibles sont :\n'+
						  '-   stats : pour mettre à jour les attributs/classes des héros à partir de la page https://friends-and-dragons.fandom.com/wiki/Hero_Stats\n' +
						  '-   gear : pour mettre à jour les stuffs des héros à partir de la page https://friends-and-dragons.fandom.com/wiki/Hero_Gear\n' +
						  '-   talents : pour mettre à jour les talents des héros à partir de la page https://friends-and-dragons.fandom.com/wiki/Hero_Talents\n' +
						  '-   all (ou aucun paramètre) : pour mettre à jour les 3 tables ci-dessus\n\n' +
						  'Si vous souhaitez ajouter un héros du jeu ou modifier un paramètre mal renseigné, il vous suffit de mettre à jour le wiki puis d\'entrer la commande correspondante pour que le bot récupère votre modification.\n' +
						  'Pour info, la page Hero_Stats est utilisée comme référence : si un héros n\'y apparaît pas, il ne sera pas référencé pour le bot.\n' +
						  'Il est donc primordial de mettre à jour cette page si vous souhaitez référencer un nouveau héros :wink:',
				'error': '\n\nSi vous constatez qu\'une erreur s\'est glissée dans le retour du bot, n\'hésitez pas à mettre à jour la source depuis le Fandom Wiki (/update help pour + d\'infos :wink:)'
				}
			},
		'update': {
			'title': 'Récupération des données',
			'color': 'default',
			'description': {
				'all'   :'Récupération de toutes les données du Fandom Wiki réussie \n',
				'part1' :'Récupération de le liste des ',
				'part2' :' du Fandom Wiki réussie \n',
				'thxmsg':'Merci pour ta contribution :thumbsup:',
				'erreur':'Le paramètre entré pour la commande /update n\'a pas été reconnu :cry:\n' +
						 'Merci de vérifier et de réitérer la commande :wink:'
				}
			},
		'petlist': {
			'title': 'Liste des pets équipables par le héros '
			},
		'class' : {
			'title': 'Liste des ',
			'color': 'default',
			},
		'error': {
			'title': 'Erreur',
			'color': 'red'
			},
		'wait': {
			'title': 'Requête en cours...',
			'color': 'default',
			'description': 'Merci de patienter :wink: \n' +
						   'Si ce message ne se met pas à jour, veuillez réitérer la commande :innocent:'
			},
		'none': {
			'title': 'Commande non trouvée',
			'color': 'red',
			'description':'Commande inexistante, merci d\'utiliser /bothelp pour obtenir la liste des commandes utilisables'
			},
		'nocomment': {
			'description': 'Pas de commentaire pour l\'instant :shrug:\n' +
						   'N\'hésitez pas à ajouter le vôtre via la commande /addcomment (/addcomment help pour plus d\'info)'
		},
		'footer': {
			'ok': '*généré par F&D-discord-bot en ',
			'too_long': '\n**[...]**\n\n:warning: la fin est tronquée pour cause de dépassement de la taille maximum d\'un message sur discord :shrug:\nSi possible, merci d\'affiner votre recherche pour avoir le résultat complet :wink:'
		},
		'dhjk': {
			'0': {
				'gif': 'https://media1.tenor.com/m/Vq3qMfYjhS4AAAAC/waynes-world.gif',
				'text': "# Priez DHJK !!! #\nOn mérite pas !\nOn mérite pas !\nOn est tout p'tit !\nOn est à chier !"
				}, 
			'1': {
				'gif': 'https://media1.tenor.com/m/1y-Ew1y_ZLsAAAAC/moses-mitsotakis.gif',
				'text': "# Priez DHJK !!! #\nFracasse est le le lieu qui a donné naissance au dhjkisme. Zeyuka est le messager qui a permis l'exportation internationale de ce courant philosophique qui explique que DHJK est tout, et que sans lui, l'univers n'est rien.\n*Zeyuki[FR]acasse, prophète officiel*"
				},
			'2': {
				'gif': 'https://media1.tenor.com/m/84rqaYkWVVQAAAAC/the-office-michael-scott.gif',
				'text': '# Priez DHJK !!! #\nUn jour Quand j\'étais jeune chef de guilde j\'ai du résoudre un conflit dans la guilde.\nJ\'ai donc tranché pour clore le conflit. Face aux protestations du moment où ca parlait de faire des règles ou une charte ou ce genre de chose, j\'ai poliment rappelé que : "Pas besoin de règles puisque ici le chef c\'est moi!".\nA partir de là ben zeyuka a mouillé son pantalon et tu connais les conséquences.\n(Non pas que ça me déplaise.)\nEt depuis la paix règne sur [FR]acasse!\n*dhjk en personne*'
				},
			'3': {
				'gif': 'https://media1.tenor.com/m/xEcQqDV9bY4AAAAC/estupefacto.gif',
				'text': '# Priez DHJK !!! #\nNom de moi!\n*dhjk en personne*'
				},
			'4': {
				'gif': 'https://media1.tenor.com/m/dB3E-yGFzZkAAAAC/bucher-kaamelot.gif',
				'text': '# Priez DHJK !!! #\nOn a affaire à quelque chose de singulier le DHJKisme, une philosphie véhiculée par son plus grand adepte, un psychopate nommé Zeyuki[FR]acasse Je ne sais pas ce que dhjk lui a fait mais son cerveau est tellement bien lavé que ça brille !\n*Pandaa, mécréant du dhjkisme*'
			},
		}
	}

	exportInJson(messages,'messages.json',add_rep_to_parent('JSON'))



print('Génération du json pour les qualités d\'item...')
quality()
print('Done :)')
print('Génération du json pour les poussières...')
dust()
print('Done :)')
print('Génération du json pour les messages Discord...')
messages()
print('Done :)')