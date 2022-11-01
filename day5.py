#Partie 1

#On reprend notre jeu de données et on importe numpy pour les transformer en array

with open('day5_input.txt', 'r') as f:

    data=[eval(line.replace(' -> ', ',')) for line in f.read().split('\n')]

import numpy as np

#On conserve dans un premier temps uniquement les valeurs où x0=x1 ou y0=x1

input2=np.array(data)

max_x = max(max(input2[:,0]),max(input2[:,2]))
max_y = max(max(input2[:,1]),max(input2[:,3]))

#On crée un array de zéros de dimensions égales aux valeurs maximum de x et y

zeros=np.zeros((max_x+1,max_y+1))

#Pour chaque élément dans notre array:

for r in input2:
    
    #Si y0=y1, on actualise ce tableau en additionnant une unité aux valeurs entre x0 et x1
    if r[1]==r[3]:
        x1=max(r[0],r[2])
        x0=min(r[0],r[2])
        for i in range(x0,x1+1):
            zeros[r[1],i]+=1
    #Si x0=x1, on actualise ce tableau en additionnant une unité aux valeurs entre y0 et y1
    elif r[0]==r[2]:
        y1=max(r[1],r[3])
        y0=min(r[1],r[3])
        for i in range(y0,y1+1):
            zeros[i,r[0]]+=1

#On calcule le nombre d'éléments plus grands que 1
total = zeros[zeros>1].shape[0]
print('Partie 1 :', total)

#Partie 2
#On crée un array de zéros de dimensions égales aux valeurs maximum de x et y

zeros=np.zeros((max_x+1,max_y+1))

#Pour chaque élément dans notre array:

for r in input2:
    
    #Si y0=y1, on actualise ce tableau en additionnant une unité aux valeurs entre x0 et x1
    if r[1]==r[3]:
        x1=max(r[0],r[2])
        x0=min(r[0],r[2])
        for i in range(x0,x1+1):
            zeros[r[1],i]+=1
    #Si x0=x1, on actualise ce tableau en additionnant une unité aux valeurs entre y0 et y1
    elif r[0]==r[2]:
        y1=max(r[1],r[3])
        y0=min(r[1],r[3])
        for i in range(y0,y1+1):
            zeros[i,r[0]]+=1
    #Pour les diagonales, on actualise le tableau également.
    else:
        x1=r[2]
        x0=r[0]
        y1=r[3]
        y0=r[1]
        #Le calcul est différent en fonction des relations entre x0,x1,y0,y1
        for i in range(abs(x1-x0)+1):
            if y0<y1 and x0<x1:
                zeros[y0+i,x0+i]+=1
            elif y0>y1 and x0<x1:
                zeros[y0-i,x0+i]+=1
            elif y0<y1 and x0>x1:
                zeros[y0+i,x0-i]+=1
            elif y0>y1 and x0>x1:
                zeros[y0-i,x0-i]+=1  

#On calcule le nombre d'éléments plus grands que 1
total = zeros[zeros>1].shape[0]
print('Partie 2 :', total)