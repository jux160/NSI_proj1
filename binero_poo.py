
class grille():
    
    def __init__(self,difficulte=1):
        """methode constructor qui defini le plateau de jeux et le plateau de correction en fonction duint renseigner 

        Args:
            difficulte (int): difficulte du niveaux, vaut 1 par default 
        """
        
        if difficulte == 1:
            self.plateau =  [["*","*","*","*","*","1"], #grille de depart du niveaux 1
                             ["*","0","*","*","0","*",],
                             ["*","*","*","*","*","1"],
                             ["*","0","1","*","1","*",],
                             ["*","*","*","0","*","*",],
                             ["0","*","1","*","*","*",]]
            
            self.plateau_correcte = [["0","1","0","0","1","1"], #grille de correction du niveaux 1
                                     ["1","0","1","1","0","0"],
                                     ["0","1","0","1","0","1"],
                                     ["1","0","1","0","1","0"],
                                     ["1","1","0","0","1","0"],
                                     ["0","0","1","1","0","1"]]
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
    
    def modif(self,ligne, colonne, car):
        """methode qui modifie le plateau de jeux 

        Args:
            ligne (int): ligne que l'utilisateur veux modifier 
            colonne (int): colonne que l'utilisateur veux modifier 
            car (str): element par laquelle on le place dans le plateau soit 1 ou 0 
        """

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
            
        self.plateau[ligne-1][colonne-1] = str(car)
       

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




grille1 = grille(1)
grille1.affichage()
print()
grille1.modif(1,1,"E")
grille1.affichage()