# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 14:46:12 2022

@author: julien gadotti
"""

def menu():
    """
    fonctions qui affiche le menu et demande  l'utilisateur oui souhaite aller

    Returns
    -------
    choix : int
        choix de l'utilisateur.

    """
    
    choix = int(input("selectionné se que vous voulez: "+"\n"+  #demande le choix de l'utilisateur 
                      "1.regle du jeux"+"\n"+
                      "2.but du jeux"+"\n"+
                      "3.niveaux facile"+"\n"+
                      "4.niveaux moyen"+"\n"+
                      "5.niveux difficile"+"\n"
                      "saisisez avec 1, 2, 3, 4 ou 5: "))
    while choix != 1 and choix != 2 and choix != 3 and choix != 4 and choix != 5: #verifie que l'utilisateur a bien selectionner 1 2 3 4 ou 5
        choix = int(input("veuillez ressaisir: ")) # demande a l'utilisateur de ressaisir si sa premier saisie est fausse 
        
    return choix # retour le choix de l'utilisateur 

def afficher(tab):
    
    print(tab)

def jeux(niveaux):
    
    ##conditions pour asigner la grille de jeux selon le niveaux 
    
    if niveaux == 1:

        grille = [["*","*","*","*","*","1"], #grille de depart du niveaux 1
               ["*","0","*","*","0","*",],
               ["*","*","*","*","*","1"],
               ["*","0","1","*","1","*",],
               ["*","*","*","0","*","*",],
               ["0","*","1","*","*","*",]]
    
        grillecorrect = [["0","1","0","0","1","1"], #grille de correction du niveaux 1
                      ["1","0","1","1","0","0"],
                      ["0","1","0","1","0","1"],
                      ["1","0","1","0","1","0"],
                      ["1","1","0","0","1","0"],
                      ["0","0","1","1","0","1"]]

    elif niveaux == 2:
        grille = 2
        grillecorection = 2
    
    elif niveaux == 3:
        grille = 3
        grillecorrection =3
    
    #boucle tant que je joueur na pas fini sa parti soit disant dis tant que la grille de jeux n'est pas egal a la grille correct 
    while grille != grillecorrect:
        
        afficher(grille) # affichage de la grille 

        #demande a l'utilisateur dans quelle ligne, colonne, et le chiffre qu'il veux modifier

        modifLigne = int(input("dans quelle ligne voulez vous modifier: "+ "\n"))
        #verifie si l'utilisateur a saisie un chiffre corect 
        while type(modifLigne) != int or modifLigne-1 > len(grille):
            print("votre saisie est incorrect veuillez resaissir avec un chiffre correct ")
            modifLigne = int(input(": "))


        modifColone = int(input("dans quelle colone voulez vous modifier: "+ "\n"))
        #verifie si l'utilisateur a saisie un chiffre corect 
        while type(modifLigne) != int or modifLigne-1 > len(grille):
            print("votre saisie est incorrect veuillez resaissir avec un chiffre correct ")
            modifLigne = int(input(": "))


        modifCar = int(input("voulez-vous placer un 0 ou un 1: "))
        #verifie si l'utilisateur a saisie un chiffre corect 
        while type(modifLigne) != int or modifLigne-1 > len(grille):
            print("votre saisie est incorrect veuillez resaissir avec un chiffre correct soit 1 soit 0 ")
            modifLigne = int(input(": "))
        
        grille[modifLigne-1][modifColone-1] = modifCar #on efectue les modifications demander en enlevant 1 au ligne et au colonne carpython commence a 0

    print("BRAVO!!! tu a gagné le niveux" + niveaux)   
    
def main():
    
    
    choix = menu() # variable qui renvoie a la fonctions menu() pour savoir ou l'utilisateur veux se rendre 
    
    #conditions pour savoir se que l'utilisateur a saisie et le renvoyer vers le bon chemin 
    if choix == 1:
        #print les regle du jeux 
        print("\n" + "dans se jeux il y a que 2 régle :" + "\n" + 
              "-il faut qu'il y est autant de 0 que de 1 sur une meme ligne et sur une meme colonne" + "\n" + 
              "-il ne peux pas y avoir plus de deux 0 ou deux 1 a la suite en horizontale et en verticale" + "\n" + 
              "- il ne peux pas avoir deux ligne ou colonne identique"  + "\n")
        input("entrer" + "\n") # attend que l'utilisateur tape une touche pour continuer
        
        return 1 #retourn 1 pour savoir que l'utilisateur lisez les regle ou le but du jeux pour dans la boucle du jeux 
    
    elif choix == 2:
        #print le but du jeux 
        print("\n" + "le but du jeux est de completer entierement la grille sans faire d'erreur" + "\n")
        input("entrer" + "\n") # attend que l'utilisateur tape une touche pour continuer
        
        return 1 #retourn 1 pour savoir que l'utilisateur lisez les regle ou le but du jeux pour dans la boucle du jeux 
    
    elif choix == 3:
        #renvoie le joueur vers le niveau 1
        jeux(1)
        return 2 #retourn 2 pour savoir que l'utilisateur jouer pour la boucle du jeux 
    
    elif choix == 4:
        #renvoie le joueur vers le niveau 2
        jeux(2)
        return 2 #retourn 2 pour savoir que l'utilisateur jouer pour la boucle du jeux 
    
    elif choix == 5:
        #renvoie le joueur vers le niveau 3
        jeux(3)
        return 2 #retourn 2 pour savoir que l'utilisateur jouer pour la boucle du jeux 
        
if __name__ == "__main__":
    
    
     
    
    jeu = True #variable qui  permet la boucle de jeux principale

    while jeu: #boucle de jeux principale

        m = main()
        if m != 1: #si l'utilisateur a jouer et n'a pas lu les regle alors on lui demande si il veux rejouer, si oui on continu si non on stop la boucle de jeux pincipale 
            fin = input("voulez vous continuera jouer (o/n): ")
            while fin != "o" or fin != "n":
                print("veuillez ressaisir avec le caractere 'o' ou le caractere 'n'")
                fin = input(": ")
            if fin == "n":
                jeu = False 


print("\n"+"Au revoir")