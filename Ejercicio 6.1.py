#Jorge Hinostrosa Paula 
#paulajhinostrosa@ciencias.unam.mx

import random as r

#A) 
l=[]
for i in range(100):
  l.append(r.randint(1,100))
diccionario1={l[i]:True if l[i]%2==0 else False for i in range(100)}
print(diccionario1)

#B)
l2=[]
for i in range(100):
  l2.append(r.uniform(-100,100))
diccionario2={l2[i]:"Positivo" if l2[i]>0 else "Negativo" for i in range(100)}
print(diccionario2)

#C)  
listaM=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
listam=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
diccionario3={listaM[i]:listam[i] for i in range(0,26)}
print(diccionario3)

#D) 
abc="abcdefghijklmnopqrstuvwxyz"
n=r.randint(1,20)
cadena=""
for i in range(n):
  cadena=cadena+r.choice(abc)
l=[]
for i in range(100):
  l.append(cadena)
diccionario4={l[i]:len(l[i]) for i in range(100)}
print(diccionario4)

#E)  
nombres=["Hidrogeno","Helio","Litio","Berilio","Boro","Carbono","Nitrogeno","Oxigeno","Fluor","Neon","Sodio","Magnesio","Aluminio","Silicio","Fosforo","Azufre","Cloro","Argon","Potasio","Calcio"]
simbolos=["H","He","Li","Be","B","C","N","O","F","Ne","Na","Mg","Al","Si","P","S","Cl","Ar","K","Ca"]
diccionario5={simbolos[i]:nombres[i] for i in range(20)}
print(diccionario5)

#F)  
numeros=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
l=[[1],[1,2],[1,2,3],[1,2,3,4],[1,2,3,4,5],[1,2,3,4,5,6],[1,2,3,4,5,6,7],[1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9,10],[1,2,3,4,5,6,7,8,9,10,11],[1,2,3,4,5,6,7,8,9,10,11,12],[1,2,3,4,5,6,7,8,9,10,11,12,13],[1,2,3,4,5,6,7,8,9,10,11,12,13,14],[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17],[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18],[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19],[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]]
diccionario6={numeros[i]:l[i] for i in range(20)}
print(diccionario6)
