#Partie 1
#On reprend la liste des positions

data = open(r'day7_input.txt').readline()
nums = data.split(",")

positions=[]
for i in nums:
    positions.append(int(i))

#On crée la liste des totaux de combustible dépensés pour chaque position
totals=[]
#Pour chaque numéro entre 0 et le valeur maximum, on parcourt la liste
for x in range(0,max(positions)):
    distances=[]
    #Pour chaque élément de la liste, on calcule la distance parcourue et on rajoute la valeur à une liste "distances"
    for i in positions:
        distances.append(abs(i-x))
    #Finalement, on rajoute la somme des distances dans le liste "totals"
    totals.append(sum(distances))
#On prend la valeur minimum de "totals"
print("Partie 1:",min(totals))

#Partie 2

#On crée la liste des totaux de combustible dépensés pour chaque position
totals=[]
#Pour chaque numéro entre 0 et le valeur maximum, on parcourt la liste
for x in range(0,max(positions)):
    distances=[]
    #Pour chaque élément de la liste, on calcule la distance parcourue et on rajoute la valeur à une liste "distances"
    for i in positions:
        #La nouvelle formule prend en compte la non-linéarité de la consommation de combustile
        distances.append(0.5*abs(i-x)+0.5*(abs(i-x))**2)
    #Finalement, on rajoute la somme des distances dans le liste "totals"
    totals.append(sum(distances))
#On prend la valeur minimum de "totals"
print("Partie 2:",int(min(totals)))