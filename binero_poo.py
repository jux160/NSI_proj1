class grille():
    
    def __init__(self,difficulte=1):
        """methode constructor qui defini le plateau de jeux et le plateau de correction en fonction duint renseigner 

           plateau et une liste de liste contenant la grille du jeux les caractere pouvant être modofier sont des chaine
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
            while ligne-1 > len(grille):
                print("votre saisie est incorrect veuillez resaissir avec un chiffre correct ")
                ligne = int(input(": "))


            colonne = int(input("dans quelle colone voulez vous modifier: "+ "\n"))
                #verifie si l'utilisateur a saisie un chiffre corect et lui demande de ressaisir si ce n'est pas le cas             
            while colonne-1 > len(grille):
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
        while grille.correction() != True
            grille.affichage()
            grille.modif()

        return False
     
    def main():
        
    
