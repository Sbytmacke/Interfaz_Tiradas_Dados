#QUIERO HACER UN CREADO DE PERSONAJE EN D&D, haciendo 6 STATS Aleatorias con las reglas que existen
#VOY A ORGANIZAR LOS DADOS

#ALEATORIEDAD
from random import randint
randint(1,10) #ejemplo:del uno al diez, te devuelve un valor aleatorio

#DADO EN FUNCION DE intento Y caras, CREANDOSE UNA LISTA SOLA CON UN APPEND GLOBAL
def dado(intentos,caras):
  #BUCLE PARA REALIZAR TANTAS TIRADAS COMO intentos DETERMINE
  crs=int(caras) 
  n0=int(0) 
  b=[]
  while n0<intentos:
    if n0<intentos:
        b.append(randint(1,crs))
    if n0==intentos:
      break
    n0=n0+1
  print("\n"+"Tu resultado del lanzamiento ha sido: " + str(b))
   #COMENTAMOS, SI SE DUPLICA
  return b

#PROGRAMA PARA CREACION DE STATS (4d6)
#SUMA DEL DADO ELIMINANDO EL VALOR MAS BAJO
def suma_dado (intentos, caras, stats):
  a=(0)
  while a<=stats:
    if a==0:
      newd=dado(intentos, caras)
      newd.sort(reverse=True)
      newd.pop()
      totalSuma=sum(newd)
      print("La suma total sin contar el valor menor: " + str(totalSuma))
      print("FUERZA: "+ str(totalSuma))
      print("------------------------")
    if a==1:
      newd=dado(intentos, caras)
      newd.sort(reverse=True)
      newd.pop()
      totalSuma=sum(newd)
      print("La suma total sin contar el valor menor: " + str(totalSuma))
      print("DESTREZA: "+ str(totalSuma))
      print("------------------------")
    if a==2:
      newd=dado(intentos, caras)
      newd.sort(reverse=True)
      newd.pop()
      totalSuma=sum(newd)
      print("La suma total sin contar el valor menor: " + str(totalSuma))
      print("CONSTITUCIÓN: "+ str(totalSuma))
      print("------------------------")
    if a==3:
      newd=dado(intentos, caras)
      newd.sort(reverse=True)
      newd.pop()
      totalSuma=sum(newd)
      print("La suma total sin contar el valor menor: " + str(totalSuma))
      print("SABIDURÍA: "+ str(totalSuma))
      print("------------------------")
    if a==4:
      newd=dado(intentos, caras)
      newd.sort(reverse=True)
      newd.pop()
      totalSuma=sum(newd)
      print("La suma total sin contar el valor menor: " + str(totalSuma))
      print("INTELIGENCIA: "+ str(totalSuma))
      print("------------------------")
    if a==5:
      newd=dado(intentos, caras)
      newd.sort(reverse=True)
      newd.pop()
      totalSuma=sum(newd)
      print("La suma total sin contar el valor menor: " + str(totalSuma))
      print("CARISMA: "+ str(totalSuma))
      print("------------------------")
    if a==stats:
      break
    a=a+1

def newPlayer(): 
  suma_dado(4,6,6)

