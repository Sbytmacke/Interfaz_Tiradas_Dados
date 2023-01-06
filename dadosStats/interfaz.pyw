#ESTA ES LA RAIZ
from logicaStats.creadorstats import *
from tkinter import *
miRaiz=Tk()
miRaiz.config(bg="white")
miRaiz.title("Creador de Stats")
miRaiz.iconbitmap("dadosStats\imagenes\d20.ico")
miRaiz.geometry("450x300")
#miRaiz.config(bg="#74b9ff")

#ESTE ES EL FRAME
espacioframe=Frame(miRaiz)
espacioframe.config(height=80)
espacioframe.grid(row=1,column=0)

texto0=Label(miRaiz, bg="white", text="Cantidad de tiradas: ")
texto0.grid(row=0,column=0, pady=20, padx=(10,0))

#HE TENIDO QUE REESCRIBIR, he quitado INTENTOS, y he aplicado un intentos=a.get(), para que funcione
class DADO():
 
  def dadoGenerico(self,caras):
    #BUCLE PARA REALIZAR TANTAS TIRADAS COMO intentos DETERMINE
    intentos=int(a.get())
    crs=int(caras) 
    n0=int(0) 
    self.b=[]
    while n0<intentos:
      if n0<intentos:
          self.b.append(randint(1,crs))
      if n0==intentos:
        break
      n0=n0+1
  def respuesta(self):
    resultado=("Tu resultado del lanzamiento ha sido: " + str(self.b))
    Label(miRaiz,text=resultado).grid(row=3,column=0)
    return self.b
  
#ENTRADA#
a=Entry(miRaiz)
a.grid(row=0, column=1, pady=20, sticky=W)
a.config(bg="grey")

#HAY QUE LLAMAR A LA CLASE MEDIANTE LA VARIABLE:
dadogenerico=DADO()
#BOTON D4#
def d4():
  dadogenerico.dadoGenerico(4)
imgd4=PhotoImage(file="dadosStats\imagenes\buttonD4.png")
imagd4Reducida=imgd4.subsample(3)
botond4= Button(image=imagd4Reducida, cursor="hand2", command=d4)
botond4.grid(row=1,column=0, padx=(20,0))

#D12#
def d12():
  dadogenerico.dadoGenerico(12)
imgd12=PhotoImage(file="dadosStats\imagenes\d12.png")
imagd12Reducida=imgd12.subsample(3)
botond12= Button(image=imagd12Reducida, cursor="hand2", command=d12)
botond12.grid(row=1,column=1, sticky=W)

#D20#
def d20():
  dadogenerico.dadoGenerico(20)
imgd20=PhotoImage(file="dadosStats\imagenes\d20.png")
imagd20Reducida=imgd20.subsample(3)
botond20= Button(image=imagd20Reducida, cursor="hand2", command=d20)
botond20.grid(row=1,column=2, sticky=W)

def newPlayerView():
  suma_dados(4,6,6)
def suma_dados (intentos, caras, stats):
    a=(0)
    while a<=stats:
      if a==0:
        newd=dado(intentos, caras)
        newd.sort(reverse=True)
        newd.pop()
        totalSuma=sum(newd)
        respuesta1=("La suma total sin contar el valor menor: " + str(totalSuma)+"\nFUERZA: "+ str(totalSuma)+"\n""------------------------")

      if a==1:
        newd=dado(intentos, caras)
        newd.sort(reverse=True)
        newd.pop()
        totalSuma=sum(newd)
        respuesta2=("La suma total sin contar el valor menor: " + str(totalSuma)+"\DESTREZA: "+ str(totalSuma)+"\n""------------------------")
      
      if a==2:
        newd=dado(intentos, caras)
        newd.sort(reverse=True)
        newd.pop()
        totalSuma=sum(newd)
        respuesta3=("La suma total sin contar el valor menor: " + str(totalSuma)+"\CONSTITUCIÓN: "+ str(totalSuma)+"\n""------------------------")
        
      if a==3:
        newd=dado(intentos, caras)
        newd.sort(reverse=True)
        newd.pop()
        totalSuma=sum(newd)
        respuesta4=("La suma total sin contar el valor menor: " + str(totalSuma)+"\SABIDURÍA: "+ str(totalSuma)+"\n""------------------------")

      if a==4:
        newd=dado(intentos, caras)
        newd.sort(reverse=True)
        newd.pop()
        totalSuma=sum(newd)
        respuesta5=("La suma total sin contar el valor menor: " + str(totalSuma)+"\INTELIGENIA: "+ str(totalSuma)+"\n""------------------------")
      
      if a==5:
        newd=dado(intentos, caras)
        newd.sort(reverse=True)
        newd.pop()
        totalSuma=sum(newd)
        respuesta6=("La suma total sin contar el valor menor: " + str(totalSuma)+"\CARISMA: "+ str(totalSuma)+"\n""------------------------")

      #respuesaPlayer=f"(respuesta1+respuesta2+respuesta3+respuesta4+respuesta5+respuesta6)
      Label(miRaiz, text=respuesta1).grid(row=3,column=0)

      if a==stats:
        break
      a=a+1

#PersonajeEstandar#
botonPersonaje=Button(text="CREA TU PERSONAJE ALEATORIO", cursor="hand2", command=newPlayerView)
botonPersonaje.grid(row=2, column=0, pady=20)

miRaiz.mainloop()