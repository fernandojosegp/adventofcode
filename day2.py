#Partie 1
#On reprend les donnés de l'exercise et on dénifit notre position initial=0,0

movements = [str(x) for x in open(r'day2_input.txt').readlines()]

position=0
depth=0

#On transforme la liste en deux listes: les directions (up, down, forward) et les valeurs associées
directions, values = map(list, zip(*(s.split(" ") for s in movements)))

#pour chaque ligne, on vérifie la direction du sous marin et on actualise notre position et notre profondeur en fonction des valeurs associées
values=[int(i) for i in values]
for index, direction in enumerate(directions):
    if direction=="forward":
        position+=values[index]
    elif direction=="down":
        depth+=values[index]
    elif direction=="up":
        depth-=values[index]

#On multiplie la profondeur par la position horizontale
result=depth*position
print("Partie 1:",result)

#Partie 2
#On dénifit notre position initial=0,0 et notre "aim"=0
position=0
depth=0
aim=0

#pour chaque ligne, on vérifie la direction du sous marin et on actualise notre position et notre profondeur en fonction des valeurs associées
values=[int(i) for i in values]
for index, direction in enumerate(directions):
    if direction=="forward":
        position+=values[index]
        depth+=values[index]*aim
    #ensuite, on actualise notre "aim"
    elif direction=="down":
        aim+=values[index]
    elif direction=="up":
        aim-=values[index]

#On multiplie la profondeur par la position horizontale
result=depth*position
print("Partie 2:",result)