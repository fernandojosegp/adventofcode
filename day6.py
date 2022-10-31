#Partie 1
#On reprend la liste des poissons

data = open(r'day6_input.txt').readline()
nums = data.split(",")

lanternfish=[]
for i in nums:
    lanternfish.append(int(i))

#On crée une boucle de durée 80 jours
for x in range(80):
    #Pour chaque élément égal à zero, on le transforme en 6 et on rajoute un élément à la fin de liste égal à 9
    #(la boucle "else" les transformera en 8)
    new=[]
    for index,fish in enumerate(lanternfish):
        if fish==0:
            lanternfish[index]=6
            new.append(8)
        #pour les autres éléments, on diminue d'une unité par itération
        else:
            lanternfish[index]=lanternfish[index]-1
    lanternfish=lanternfish+new
    #On finit notre première boucle puis on passe au jour suivant
print("Partie 1:",len(lanternfish))

#Partie 2
#J'ai du optimiser mon code car ma méthode précedente était trop coûteuse en mémoire pour réaliser le calcul avec 256 jours
#On reprend la liste des poissons

lanternfish=[]
for i in nums:
    lanternfish.append(int(i))

#On profite du fait qu'on n'ait pas besoin de la liste complète de poissons mais uniquement du nombre de poissons dans chaque état à chaque jour
#On compte combien de poissons il y en a avec le même nombre de jours restants
nombre_actuel = {
    0: lanternfish.count(0),
    1: lanternfish.count(1),
    2: lanternfish.count(2),
    3: lanternfish.count(3),
    4: lanternfish.count(4),
    5: lanternfish.count(5),
    6: lanternfish.count(6),
    7: lanternfish.count(7),
    8: lanternfish.count(8)
}

nombre_suivant = {}
# Pour chaque jour, on actualise l'état de chaque poisson en fonction de l'état précedent
for i in range(256):

    nombre_suivant = {
        0: nombre_actuel[1],
        1: nombre_actuel[2],
        2: nombre_actuel[3],
        3: nombre_actuel[4],
        4: nombre_actuel[5],
        5: nombre_actuel[6],
        6: nombre_actuel[7]+nombre_actuel[0],
        7: nombre_actuel[8],
        8: nombre_actuel[0]
    }

    #Pour changer de jour, on transforme "nomnre_suivant" en "nombre_" 
    #Move value of new_states to current_states, reset value new_states
    nombre_actuel = nombre_suivant
    nombre_suivant = {}

#Finalement, on somme les valeurs stockés le dernier jour
somme = 0
for i in nombre_actuel:
    somme += nombre_actuel[i]
    
print("Partie 2",somme)