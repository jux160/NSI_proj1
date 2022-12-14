class binero:   
    def __init__(self,difficulte=1):
        """methode constructor qui defini le plateau de jeux et le plateau de correction en fonction duint renseigner 

           plateau et une liste de liste contenant la binero du jeux les caractere pouvant être modofier sont des chaine
           de caractere et les entiés ne peuvent pas être modifier 
        Args:
            difficulte (int): difficulte du niveaux, vaut 1 par default 
        """
        
        if difficulte == 1: 
            # generation du plateu de jeux et du plateau de corections
            self.plateau = self.convertion("niveaux/simple.txt")[0]
            self.plateau_correcte = self.convertion("niveaux/simple.txt")[1]
            
        elif difficulte == 2:
            # on repete la meme chose pour le niveaux 2
            self.plateau = self.convertion("niveaux/moyen.txt")[0]
            self.plateau_correcte = self.convertion("niveaux/moyen.txt")[1]

        elif difficulte == 3:
            self.plateau = self.convertion("niveaux/difficile.txt")[0]
            self.plateau_correcte = self.convertion("niveaux/difficile.txt")[1]
    def convertion(self, fichier):

        """methode qui convertie le fichier du niveaux en liste de liste 

        Args:
            fichier (str): fichier du niveaux
        
        return:
            liste avec la grille en occurence 1 et la correctioon en 2
        """
        f = open(fichier, "r") #overture du fichier du niveaux 1
        taille = int(f.readline()) #lecture de la premier ligne qqui definie le nombre de ligne du plateau 
        grille = [] #definitin de la grille de jeux qui par la suite sera ensuite l'attribut plateau
        correction = [] #grille de corrections
        for i in range(taille):# boucle qui permet de lire les ligne du plateaux de jeux 
            line = f.readline() #on lis la ligne et on la stock ensuite dans la variable line
            line = line.replace("\n", "").replace(" ", "*") #on remplace les espace par des *
            grille.append(list(line))#on ajoute la ligne a grille sous forme de liste de strings
        #permet de convertir les 0 et 1 qui sont en str en int pour les differencier entre les 0,1 ajouter par l,utilisateur et ceux deja present sur le plateau
        for ligne in range(len(grille)):
            for car in range(len(grille[i])):
                if grille[ligne][car] == "1":
                    grille[ligne][car] = 1
                elif grille[ligne][car] == "0":
                    grille[ligne][ligne] = 0            
        #definition du plateau de jeux de correction
        for ligne in range(taille):
            line = f.readline()
            line = line.replace("\n", "") 
            correction.append(list(line))
        for ligne in range(len(grille)):
            for car in range(len(grille)):
                if grille[ligne][car] == "2":#on remplce les 2 par des 1 et les trois par des 0
                    grille[ligne][car] = 1
                elif grille[ligne][car] == "3":
                    grille[ligne][car] = 0
        f.close()
        return [grille,correction]  
    def entre_modif(self):
        """methode permetant de demander aux joueur quelle element il veux modifier et de les modifier
        """
        #on demande a l'utilisateur dans quelle ligne il veux placer
        print("dans quelle ligne voulez vous modifier: "+ "\n")
        ligne = self.entre()

        #on demande la colonne
        print("dans quellecolonne voulez vous modifier ")
        colonne = self.entre()

        #on verifie si l'endroit de la modification n'es pas un int dans qu'elle cas cela signifie qu'on ne peux pas le modifier 
        while type(self.plateau[ligne-1][colonne-1]) == int:  # type: ignore
            print("vous ne pouvais pas modifier se caractere est present de base sur la grille")
            #on redemande la ligne et la colonne
            print("ressaisisez votre ligne: ")
            ligne = self.entre()
            print("ressaisisez votre colonne")
            colonne = self.entre()


        #on demande si l'utilisateur veux placer un 0 ou un 1
        car = input("voulez-vous placer un 0 ou un 1: ")

        #verifie si l'utilisateur a saisie un chiffre corect et lui demande de ressaisir si ce n'est pas le cas 
        while car != "0" and car != "1":
            print("votre saisie est incorrect veuillez resaissir avec un chiffre correct soit 1 soit 0 ")
            car = input(": ")

        #on modifie par le nombre corespondant en str pour pouvoir le remodifier par la suite si besoin
        self.plateau[ligne-1][colonne-1] = car  # type: ignore
    def entre(self):
        """fonction qui demande a l'utilisateur de rentrer une ligne ou un colonne et verifie si la saisie est bonne, 
           si cela ne sort pas de l'index du plateau

        Returns:
           int : numero de la ligne ou colonne entre par l'utilisateur 
        """     
        entre = input(":")
        #verifie si l'utilisateur a saisie un chiffre/nombre pour pouvoir le convertir en int 
        while type(entre) != int: 
            while type(entre) != int:
                try:
                    int(entre)#on regarde si la convertion en int de ligne ne revoie pas d'erreur 

                except ValueError: #si il renvoit une erreur alors on demande de resaisir 
                    print("votre saisie est incorrect veuilez saisir un chiffre")
                    entre = input(": ")
                    
                else:  #on convertit ligne en int maintenant qu'on sait qu'il n'y aurra pas d'erreure
                    entre = int(entre) 

             #verifie si l'utilisateur a saisie un chiffre etant dans le plateau de jeux et lui demande de ressaisir si ce n'est pas le cas             
            if entre-1 > len(self.plateau):  # type: ignore
                print("votre saisie est incorrect veuillez resaissir avec un chiffre correct ")
                entre = (input(": ")) #ligne repasse en str pour pouvoir recommencer le try except pour verifier la saisie fait est bonne 

        return entre 
    def __str__(self):
        """Renvoie de l'utilisateur
        return la chaine du plateau"""
        chaine = ""

        for i in self.plateau:
            for k in i:
                chaine += str(k) + " "

            chaine += "\n"
    
        return chaine
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
        while self.correction() != True:
            print(self.__str__())
            self.entre_modif()
        print("bravo vous avez gagné cette partie")
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

if __name__ == "__main__":

    jeux = True
    while jeux:

        choix = binero.menu()

            #conditions pour savoir se que l'utilisateur a saisie et le renvoyer vers le bon chemin 
        if choix == 1:
            #print les regle du jeux 
            print("\n" + "dans se jeux il y a que 3 régle :" + "\n" + 
                "-il faut qu'il y est autant de 0 que de 1 sur une meme ligne et sur une meme colonne" + "\n" + 
                "-il ne peux pas y avoir plus de deux 0 ou deux 1 a la suite en horizontale et en verticale" + "\n" +                 
                "- il ne peux pas avoir deux ligne ou colonne identique"  + "\n")
            input("entrer" + "\n") # attend que l'utilisateur tape une touche pour continuer
            
        elif choix == 2:
            #print le but du jeux 
            print("\n" + "le but du jeux est de completer entierement la grille sans faire d'erreur" + "\n")
            input("entrer" + "\n") # attend que l'utilisateur tape une touche pour continuer
                    
        elif choix == 3:
            #renvoie le joueur vers le niveau 1
            grille = binero(1)
            grille.jeux()        
            
        elif choix == 4:
            #renvoie le joueur vers le niveau 2
            grille= binero(2)
            grille.jeux()   

        elif choix == 5:
            #renvoie le joueur vers le niveau 3
            grille= binero(3)
            grille.jeux()   

        #conditions pour savoir si le joueur etait en train de jouer ou pas, si il jouait alors on lui demande si il veux rejouer 
        if choix == 3 or choix == 4 or choix == 5:
            continuer = input("voulez vous rejouer ou pas (oui/ non : ")
            while continuer != "oui" and continuer != "non":
                continuer = input("veuillez ressaisir avec un oui ou un non :")

            #conditions qui permet d'arreter la boucle principale en passant jeux a False 
            if continuer == "non":
                jeux == False