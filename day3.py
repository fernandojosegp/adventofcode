#Partie 1
#On reprend les donnés du rapport et on les transpose

report = [str(x) for x in open(r'day3_input.txt').readlines()]

bits=[''.join(s) for s in zip(*report)]

#on calcule les nombres plus et moins fréquents dans chaque élément de notre liste, qui correspond à une colonne du rapport
import collections

plusf=[]
for i in bits:
    plusf.append(collections.Counter(i).most_common()[0])
moinsf=[]
for i in bits:
    moinsf.append(collections.Counter(i).most_common()[-1])

#on calcule gamma et epsilon en base 10
gamma=[]
for x,y in plusf:
    gamma.append(x)
binary_gamma=''.join(gamma)
int_gamma=int(binary_gamma, 2)

epsilon=[]
for x,y in moinsf:
    epsilon.append(x)
binary_epsilon=''.join(epsilon)
int_epsilon=int(binary_epsilon, 2)

#on calcule la consommation du moteur en multipliant les deux
power_consumption=int_gamma*int_epsilon
print("Partie 1:",power_consumption)