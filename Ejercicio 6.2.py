#Jorge Hinostrosa Paula 
#paulajhinostrosa@ciencias.unam.mx
import random as r

class Agenda:
  def __init__(self,nombre,numero):
    self.nombre=nombre
    self.numero=numero
  def __str__(self):
    return str(self.nombre)+"\n"+str(self.numero)
  def listaPseudo(n):
    l=[]
    for i in range(n):
      numero2=r.randint(5500000000,5599999999)
      abc="abcdefghijklmnopqrstuvwxyz"
      ABC="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
      nombre2=ABC[r.randint(0,25)]  
      for i in range(9):
        nombre2=nombre2+abc[r.randint(0,25)]
      l.append(Agenda(nombre2,numero2))
    return l
  def diccionarioNombres(agenda):
    return {i.nombre:i.numero for i in agenda}
  def diccionarioNumeros(agenda):
    return {i.numero:i.nombre for i in agenda}
  def diccionarioIndices(agenda):
    return {i.nombre:j for i in agenda for j in range(len(agenda)+1)}
a1=Agenda("Mago",5531986820)
print(a1)
lista=Agenda.listaPseudo(10)
print(lista[2])
lno=Agenda.diccionarioNombres(lista)
print(lno)
lnu=Agenda.diccionarioNumeros(lista)
print(lnu)
li=Agenda.diccionarioIndices(lista)
print(li)
