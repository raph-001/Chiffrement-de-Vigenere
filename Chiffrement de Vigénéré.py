Liste_des_lettres = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]


texte = input("Donnez le texte : ")

texteChiffre = ""
cle = input("Quelle est cle : ") 
cle_chiffree = []

compteur = 0



def chiffrement():
	global compteur, texteChiffre
	for i in cle:

		if i not in Liste_des_lettres:
			compteur += 0

		else:
			position = Liste_des_lettres.index(i)
			position_Str = str(position)
			cle_chiffree.append(position_Str)
			compteur +=1



	for i in texte:
		if i not in Liste_des_lettres:
			compteur +=0
		else:
			position_texte = Liste_des_lettres.index(i)
			texteChiffre = texteChiffre + (Liste_des_lettres[position_texte + int(cle_chiffree[compteur%len(cle_chiffree)])])
			compteur +=1


	print(texteChiffre)

def dechiffrement():
	global compteur, texteChiffre
	for i in cle:

		if i not in Liste_des_lettres:
			compteur += 0

		else:
			position = Liste_des_lettres.index(i)
			position_Str = str(position)
			cle_chiffree.append(position_Str)
			compteur +=1



	for i in texte:
		if i not in Liste_des_lettres:
			compteur +=0
		else:
			position_texte = Liste_des_lettres.index(i)
			texteChiffre = texteChiffre + (Liste_des_lettres[position_texte - int(cle_chiffree[compteur%len(cle_chiffree)])])
			compteur +=1


	print(texteChiffre)

dechiffrerOuChiffrer = input("Voulez vous chiffrer ce texte avec la clé ou le déchiffrer ? (tappez 'c' pour chiffrer ou 'd' pour dechiffrer)")

if dechiffrerOuChiffrer == "c":
	chiffrement()
elif dechiffrerOuChiffrer == "d":
	dechiffrement()
else:
	print("Vous n'avez pas tappez une réponse valide.")



