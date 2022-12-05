class binero():
    
    def __init__(self,difficulte=1):
        """methode constructor qui defini le plateau de jeux et le plateau de correction en fonction duint renseigner 

           plateau et une liste de liste contenant la binero du jeux les caractere pouvant être modofier sont des chaine
           de caractere et les entiés ne peuvent pas être modifier 
        Args:
            difficulte (int): difficulte du niveaux, vaut 1 par default 
        """
        
        if difficulte == 1:
            self.plateau =  [["*","*","*","*","*",1], #grille de depart du niveaux 1
                             ["*",0,"*","*",0,"*",],
                             ["*","*","*","*","*",1],
                             ["*",0,1,"*",1,"*",],
                             ["*","*","*",0,"*","*",],
                             [0,"*",1,"*","*","*",]]
            
            self.plateau_correcte = [["0","1","0","0","1",1], #grille de correction du niveaux 1
                                     ["1",0,"1","1",0,"0"],
                                     ["0","1","0","1","0",1],
                                     ["1",0,1,"0",1,"0"],
                                     ["1","1","0",0,"1","0"],
                                     [0,"0",1,"1","0","1"]]
        elif difficulte == 2:
            self.plateau = [["1","1","*","*","*","1","*","*","*","*"], #grille de depart du niveaux 2
                            ["*","*","*","*","*","*","*","*","0","*"],
                            ["0","1","*","0","*","*","1","*","*","*"],
                            ["1","*","*","0","*","*","*","*","*","*"],
                            ["*","*","1","*","*","*","0","*","1","1"],
                            ["*","*","*","*","*","*","0","*","*","*"],
                            ["0","*","*","*","*","*","*","*","*","0"],
                            ["*","*","1","*","*","0","*","*","*","*"],
                            ["*","*","1","1","*","*","1","0","*","0"],
                            ["*","0","*","*","*","*","*","*","*","0"]]

            self.plateau_correcte = [["1","1","0","0","1","1","0","1","0","0"],
                                    ["0","0","1","1","0","1","0","1","0","1"],  #grille de correction du niveaux 2
                                    ["0","1","0","0","1","0","1","0","1","1"],
                                    ["1","1","0","0","1","0","1","1","0","0"],
                                    ["0","0","1","1","0","1","0","0","1","1"],
                                    ["1","0","1","0","1","0","0","1","0","1"],
                                    ["0","1","0","1","0","1","1","0","1","0"],
                                    ["0","1","1","0","1","0","0","1","0","1"],
                                    ["1","0","1","1","0","0","1","0","1","0"],
                                    ["1","0","0","1","0","1","1","0","1","0"]]

        elif difficulte == 3:
            self.plateau = [["*","0","*","*","1","1","*","*","*","1"],
                            ["*","*","0","*","*","*","*","*","0","*"],
                            ["*","1","*","1","*","*","*","*","*","*"],
                            ["*","1","*","*","0","*","*","*","*","*"], #grille de depart du niveaux 3
                            ["*","*","*","*","*","*","*","0","1","*"],
                            ["1","*","*","0","*","*","*","0","*","*"],
                            ["1","1","*","*","*","*","*","*","*","*"],
                            ["*","*","*","*","*","*","*","*","*","0"],
                            ["*","*","*","1","*","*","*","1","*","*"],
                            ["*","*","0","*","*","*","*","*","1","*"]]

            self.plateau_correcte = [["0","0","1","0","1","1","0","0","1","1"],
                                    ["1","0","0","1","0","1","1","0","0","1"],
                                    ["1","1","0","1","1","0","0","1","0","0"],
                                    ["0","1","1","0","0","1","0","1","1","0"],
                                    ["0","0","1","1","0","0","1","0","1","1"],  #grille de correction du niveaux 3
                                    ["1","1","0","0","1","0","1","0","0","1"],
                                    ["1","1","0","0","1","1","0","1","0","0"],
                                    ["0","0","1","1","0","1","1","0","1","0"],
                                    ["0","0","1","1","0","0","1","1","0","1"],
                                    ["1","1","0","0","1","0","0","1","1","0"]]
    
    def modif(self):
        """methode permetant de demander aux joueur quelle element il veux modifier et de les modifier
        """
        #creation des variable ligne collonne et car pour pouvoir ensuite ferivier si il sont sous le bon type quand l'utilisateur vas les modifier 
        ligne = 1
        colonne =2
        car = "s"
        while type(ligne) == int and type(colonne) == int and type(car) == str:

            ligne = int(input("dans quelle ligne voulez vous modifier: "+ "\n"))
                #verifie si l'utilisateur a saisie un chiffre corect et lui demande de ressaisir si ce n'est pas le cas             
            while ligne-1 > len(self.plateau):
                print("votre saisie est incorrect veuillez resaissir avec un chiffre correct ")
                ligne = int(input(": "))


            colonne = int(input("dans quelle colone voulez vous modifier: "+ "\n"))
                #verifie si l'utilisateur a saisie un chiffre corect et lui demande de ressaisir si ce n'est pas le cas             
            while colonne-1 > len(self.plateau):
                print("votre saisie est incorrect veuillez resaissir avec un chiffre correct ")
                colonne = int(input(": "))

            #on verifie si le caractére voulant être modifier n'est pas un entier car les entier de la grille ne pauvent pas être modifier   
            if type(self.plateau[ligne-1][colonne-1]) == int: 
                ligne = str(ligne) #on convertit ligne en str pour que la boucle while continuent et redemande a l'utilisateur
                print("votre saisie dans la grille est inpossible vous ne pouvez pas modofier les element present de base ")

            car = input("voulez-vous placer un 0 ou un 1: ")
            #verifie si l'utilisateur a saisie un chiffre corect et lui demande de ressaisir si ce n'est pas le cas 
            while car != 0 or car != 1:
                print("votre saisie est incorrect veuillez resaissir avec un chiffre correct soit 1 soit 0 ")
                car = input(": ")
            
            
        #on modifie par le nombre corespondant en str pour pouvoir le remodifier paar la suite
        self.plateau[ligne-1][colonne-1] = car
       

    def affichage(self):
        """
        affiche le plateau de jeux 
        """
        for i in self.plateau:
            print(i)

    
    def correction(self):
        """methode qui verifie si le plateau du joueur est correcte 

        Returns:
            bool: True si la plateau est egal au plateu de correction et None si non 
        """
        if self.plateau_correcte == self.plateau:
            return True
    def jeux(self):
        """
        fonctions du derouler d'une partie
        """
        while binero.correction() != True:
            binero.affichage()
            binero.modif()

        return False
    def menu():
        """fonction qui demande a l'utilisateur ou il souhaite se rendre entre les regle,le but du jeux ou une partie entre 3 niveaux 

        Returns:
            int: nombre que l'utilisateur a saisie
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
        return choix 


    def main():
        """fonctions principale

        Returns:
            int: retourne 1 pour savoir que l'utilisateur ne jouer pas mais qu'il lisait soit les régle soit le but du jeux
        """

        choix = binero.menu() # variable qui renvoie a la fonctions menu() pour savoir ou l'utilisateur veux se rendre 
        
        #conditions pour savoir se que l'utilisateur a saisie et le renvoyer vers le bon chemin 
        if choix == 1:
            #print les regle du jeux 
            print("\n" + "dans se jeux il y a que 3 régle :" + "\n" + 
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
            binero.__init__(1)
            binero.jeux()
            return 2 #retourn 2 pour savoir que l'utilisateur jouer pour la boucle du jeux 
        
        elif choix == 4:
            #renvoie le joueur vers le niveau 2
            binero.__init__(2)
            binero.jeux()
            return 2 #retourn 2 pour savoir que l'utilisateur jouer pour la boucle du jeux 
        
        elif choix == 5:
            #renvoie le joueur vers le niveau 3
            binero.__init__(3)
            binero.jeux()
            return 2 #retourn 2 pour savoir que l'utilisateur jouer pour la boucle du jeux 


jeux = True        

while jeux:

    choix = binero.menu()

        #conditions pour savoir se que l'utilisateur a saisie et le renvoyer vers le bon chemin 
    if choix == 1:
        #print les regle du jeux 
        print("\n" + "dans se jeux il y a que 3 régle :" + "\n" + 
            "-il faut qu'il y est autant de 0 que de 1 sur une meme ligne et sur une meme colonne" + "\n" + 
            "-il ne peux pas y avoir plus de deux 0 ou deux 1 a la suite en horizontale et en verticale" + "\n" +                 "- il ne peux pas avoir deux ligne ou colonne identique"  + "\n")
        input("entrer" + "\n") # attend que l'utilisateur tape une touche pour continuer
        
    elif choix == 2:
        #print le but du jeux 
        print("\n" + "le but du jeux est de completer entierement la grille sans faire d'erreur" + "\n")
        input("entrer" + "\n") # attend que l'utilisateur tape une touche pour continuer
                
    elif choix == 3:
        #renvoie le joueur vers le niveau 1
        grille= binero(1)
        grille.jeux()        
        
    elif choix == 4:
        #renvoie le joueur vers le niveau 2
        grille= binero(1)
        grille.jeux()   

    elif choix == 5:
        #renvoie le joueur vers le niveau 3
        grille= binero(1)
        grille.jeux()   

    #conditions pour savoir si le joueur etait en train de jouer ou pas, si il jouait alors on lui demande si il veux rejouer 
    if choix == 3 or choix == 4 or choix == 5:
        continuer = input("voulez vous rejouer ou pas (oui/ non : ")
        while continuer 
