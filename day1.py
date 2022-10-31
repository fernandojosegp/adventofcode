#Partie 1
#On reprend les donnés de l'exercise et on dénifit notre total initial=0

measurements = [int(x) for x in open(r'day1_input.txt').readlines()]

total=0

#pour chaque mesure, on vérifie si le chiffre est plus grand que l'intérieur et on les compte en cas positif
for index, measurement in enumerate(measurements):
    if measurement>measurements[index-1]:
        total+=1

print("Partie 1:",total)

#Partie 2

total=0

#pour chaque mesure, on vérifie si la somme des trois numéros suivants est plus grande que
#la somme suivante, et on les compte en cas positif
for index, measurement in enumerate(measurements[:-3]):
    if (measurements[index+1]+measurements[index+2]+measurements[index+3])>(measurements[index]+measurements[index+1]+measurements[index+2]):
        total+=1

print("Partie 2:",total)