import random
prix=random.randint(1,10)
score= 2000
tentatives=0
print("Bienvenue au jeu du juste prix:")
while True:
 try :
   choix_joueur= int(input("Devinez le prix: "))
   tentatives+=1 
 except ValueError:
  print("Entrez un nombre entier et pas des lettres ")
  continue
 if choix_joueur< prix:
    print(" Ce n'est pas le bon prix,c'est plus haut :") 
    score-= 100
 elif choix_joueur> prix:
      print("Ce n'est pas le bon prix,c'est plus bas :")
 score-=100 
 else choix_joueur==prix:  
      print("Vous avez trouvé le bon prix, vous êtes un champion!")
   print("Le score final est de :", score )
  break 
print("Fin du jeu ")

