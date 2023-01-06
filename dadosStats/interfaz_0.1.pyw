from tkinter import messagebox
from tkinter.messagebox import showinfo
from logicaStats.creadorstats import *
from tkinter import *
#ESTA ES LA RAIZ
miRaiz=Tk()
miRaiz.resizable(False,False) #PARA QUE SOLAMENTE SE PUEDE REDIMENSIONAR HACIA LOS LATERALES
miRaiz.config(bg="white")
miRaiz.title("Creador de Stats")
miRaiz.iconbitmap("dadosStats\imagenes\d20.ico")
miRaiz.geometry("850x250")

#miRaiz.config(bg="#74b9ff")

#PRIMER FRAME DE RAIZ 
frameClickeo=Frame(miRaiz)
frameClickeo.grid(row=0, column=0,)
frameClickeo.config(bg="")

frameEntradas=Frame(frameClickeo)
frameEntradas.config(bg="")
frameEntradas.grid(row=1,column=0, pady=5, padx=(20,20))
#SEGUNDO FRAME DE RAIZ
frameBotones=Frame(miRaiz)
frameBotones.config(bg="")
frameBotones.grid(row=0,column=1, sticky=NW, padx=(20,10))
#TERCER FRAME DE RAIZ
framResultadoPlayer=Frame(miRaiz)
framResultadoPlayer.config(bg="black", width=300, height=150)
framResultadoPlayer.grid(row=1,column=0,sticky=W, pady=5, padx=(15,0))
#CUARTO FRAME DE RAIZ
#SI SE PONE EN UNA LINE NO DEPENDE DE NADIE, ES LA CONFIGURACION QUE ESCRIBIMOS Y YA, NO SE AJUSTA CON NADA MAS
frameCajaVisual=Frame(miRaiz,relief="groove",border=15, bg="#a4b0be",width=450, height=100).grid(row=1, column=1, padx=(10,0))

frameResultadoDados=Frame(frameCajaVisual)
frameResultadoDados.config(bg="#a4b0be")
frameResultadoDados.grid(row=1,column=1, padx=(10,0))

#----------------TEXTOS DE GUIAS------------------
#CUIDADO: si queremos borrar, algo con destroy, el pack(), grid() o place(), se deben situar en otra linea, es mas que obvio, al borrar lo seleccionado, no puede borrar la ubicacion asociada ej:
#Label(root, text:"pruba").pack() !!!!NO LO PUEDE BORRAR, esta en la misma linea, si destuye LABEL, destruye su ubicacion tmb, ES IMPOSIBLE
# prueba=Label(root, text:"pruba")
# prueba.pack() !!!SI LO PUEDE BORRAR, ya que la ubicacion esta separada de la linea que va a borrar que seria la anterior
def instrucciones():
  global guia1,guia2,guia3
  guia1=Label(frameResultadoDados,bg="#a4b0be", font= ('Helvetica 15 underline'),text="Resultados de tiradas", fg="red")
  guia1.grid(row=0, column=0)
  guia2=Label(frameResultadoDados,bg="#a4b0be",fg="#2d3436", text="1.Introduce en *Cantidad de tiradas*")
  guia2.grid(row=1, column=0)
  guia3=Label(frameResultadoDados,bg="#a4b0be",fg="#2d3436",text="2.Selecciona el dado necesitado: D4, D6, D8, D10, D12, D20")
  guia3.grid(row=2, column=0)

def borrarGuia():
  borrarBoton()
  guia1.destroy()
  guia2.destroy()
  guia3.destroy()


def borrarBoton():
  botonInstrucciones.destroy()
botonInstrucciones=Button(frameResultadoDados, bg="#636e72", fg="white", text="PULSA INSTRUCCIONES", command=lambda: [instrucciones(), borrarBoton()])
botonInstrucciones.grid(row=4,column=0)

#---------------ENTRADA PRINCIPAL---------------
texto0=Label(frameEntradas, bg="white", text="Cantidad de tiradas: ")
texto0.grid(row=0,column=0)
a=Entry(frameEntradas)
a.grid(row=1, column=0)
a.config(bg="#a4b0be")

#-------------------DADO GENERICO----------------
#HE TENIDO QU ASIGNAR UNA VARIABLE VACIA PARA QUE SE BORRE EL LABER FUTURO AL OBTENER OTRO VALOR DE DADOS
resultado=StringVar()
#HE TENIDO QUE REESCRIBIR, he quitado INTENTOS, y he aplicado un intentos=a.get(), para que funcione
def dadoGenerico(caras):
  global resultado
  crs=int(caras) 
  n0=int(0) 
  b=[]
  #---------MENSAJE ERROR DE VALOR---------
  try:
    intentos=int(a.get())
  except ValueError:
    messagebox.showinfo(message="Debes introducir un número", title="Cantidad de tiradas")

  while n0<intentos:
    if n0<intentos:
      b.append(randint(1,crs))
    if n0==intentos:
      break
    n0=n0+1
    #QUIERO cambiar EL LABEL CREADO CON ANTERIORIDAD, para la segunda vez que creamos otro resultado
  resultado.set("Tu resultado del lanzamiento ha sido: " + str(b))
  Label(frameResultadoDados,textvariable=resultado).grid(row=1, column=0)
  return b

#-------------BOTONES DADOS--------------------
#D4#
imgd4=PhotoImage(file="dadosStats\\imagenesDefinitivas\\buttonD4.png")
imagd4Reducida=imgd4.subsample(3)
botond4= Button(frameBotones,image=imagd4Reducida, cursor="hand2", command=lambda:[dadoGenerico(4), borrarGuia()])
botond4.grid(row=0,column=0)
#D6#
imgd6=PhotoImage(file="dadosStats\\imagenesDefinitivas\\buttonD6.png")
imagd6Reducida=imgd6.subsample(3)
botond6= Button(frameBotones,image=imagd6Reducida, cursor="hand2", command=lambda:[dadoGenerico(6),borrarGuia()])
botond6.grid(row=0,column=1)
#D8#
imgd8=PhotoImage(file="dadosStats\\imagenesDefinitivas\\buttonD8.png")
imagd8Reducida=imgd8.subsample(3)
botond8= Button(frameBotones,image=imagd8Reducida, cursor="hand2", command=lambda:dadoGenerico(8)&borrarGuia())
botond8.grid(row=0,column=2)
#D10#
imgd10=PhotoImage(file="dadosStats\\imagenesDefinitivas\\buttonD10.png")
imagd10Reducida=imgd10.subsample(3)
botond10= Button(frameBotones,image=imagd10Reducida, cursor="hand2", command=lambda:dadoGenerico(10)&borrarGuia())
botond10.grid(row=0,column=3)
#D12#
imgd12=PhotoImage(file="dadosStats\\imagenesDefinitivas\\buttonD12.png")
imagd12Reducida=imgd12.subsample(3)
botond12= Button(frameBotones,image=imagd12Reducida, cursor="hand2", command=lambda:dadoGenerico(12)&borrarGuia())
botond12.grid(row=0,column=4)
#D20#
imgd20=PhotoImage(file="dadosStats\\imagenesDefinitivas\\buttonD20.png")
imagd20Reducida=imgd20.subsample(3)
botond20= Button(frameBotones,image=imagd20Reducida, cursor="hand2", command=lambda: dadoGenerico(20)&borrarGuia())
botond20.grid(row=0,column=5)

#--------------CUADRO INCIAL DE STATS---------------
rFuerza=StringVar()
rDes=StringVar()
rCons=StringVar()
rSab=StringVar()
rInt=StringVar()
rCar=StringVar()
rFuerza.set("\nFUERZA: "+"0"+"\n--------------------")
rDes.set("\nDESTREZA: "+"0"+"\n---------------------")
rCons.set("\nCONSTITUCIÓN: "+"0"+"\n---------------------")
rSab.set("\nSABIDURÍA: "+"0"+"\n--------------------")
rInt.set("\nINTELIGENCIA: "+"0"+"\n---------------------")
rCar.set("\nCARISMA: "+"0"+"\n---------------------")
Label(framResultadoPlayer, textvariable=rFuerza,bg="#ff7979",relief=GROOVE).grid(row=0, column=0)
Label(framResultadoPlayer, textvariable=rDes,bg="#badc58",relief=GROOVE).grid(row=0, column=1)
Label(framResultadoPlayer, textvariable=rCons,bg="#ffbe76",relief=GROOVE).grid(row=0, column=2)
Label(framResultadoPlayer, textvariable=rSab, bg="#9980FA", relief=GROOVE).grid(row=1, column=0)
Label(framResultadoPlayer, textvariable=rInt, bg="#81ecec", relief=GROOVE).grid(row=1, column=1)
Label(framResultadoPlayer, textvariable=rCar,bg="#D980FA", relief=GROOVE).grid(row=1, column=2)

def newPlayerView (intentos, caras, stats):
    a=(0)
    global rFuerza
    while a<=stats:
      if a==0:
        newd=dado(intentos, caras)
        newd.sort(reverse=True)
        newd.pop()
        totalSuma=sum(newd)
        rFuerza.set("\nFUERZA: "+str(totalSuma)+"\n---------------------")
      elif a==1:
        newd=dado(intentos, caras)
        newd.sort(reverse=True)
        newd.pop()
        totalSuma=sum(newd)
        rDes.set("\nDESTREZA: "+str(totalSuma)+"\n---------------------")
      elif a==2:
        newd=dado(intentos, caras)
        newd.sort(reverse=True)
        newd.pop()
        totalSuma=sum(newd)
        rCons.set("\nCONSTITUCIÓN: "+str(totalSuma)+"\n---------------------")
      elif a==3:
        newd=dado(intentos, caras)
        newd.sort(reverse=True)
        newd.pop()
        totalSuma=sum(newd)
        rSab.set("\nSABIDURÍA: "+str(totalSuma)+"\n---------------------")
      elif a==4:
        newd=dado(intentos, caras)
        newd.sort(reverse=True)
        newd.pop()
        totalSuma=sum(newd)
        rInt.set("\nINTELIGENIA: "+str(totalSuma)+"\n---------------------")
      elif a==5:
        newd=dado(intentos, caras)
        newd.sort(reverse=True)
        newd.pop()
        totalSuma=sum(newd)
        rCar.set("\nCARISMA: "+str(totalSuma)+"\n---------------------")
      elif a==stats:
        # PRUEBA PARA JUNTAR TODOS LOS LABEL, PERO NO ES RENTABLE, YA QUE DE LA OTRA FORMA LOS ORDENAMOS POR BLOQUES
        # rTotal=(r1+"   "+r2+"   "+r3+"\n"+"-------------"+"   "+"-------------"+"   "+"-------------"+"\n"+r4+"   "+r5+"   "+r6)
        # RTotal=StringVar()
        # RTotal.set(rTotal)
        #Label(framResultadoPlayer, textvariable=RTotal, bg="#81ecec").grid(row=3, column=0)
        break
      a=a+1  

botonPersonaje=Button(frameEntradas,text="CREA TU PERSONAJE ALEATORIO", cursor="hand2", command=lambda:newPlayerView(4,6,6))
botonPersonaje.grid(row=2, column=0, pady=10)


# def printeoRespuesta():
#   r1=StringVar()
#   r2=StringVar()
#   respuestaTotal=StringVar()
#   respuestaTotal.set(r1.get())#+respuesta2.get())
#   Label(framResultadoPlayer, textvariable=respuestaTotal, bg="#81ecec").grid(row=3, column=0)
#   print(r1)

      #QUEREMEOS UNIFICARLO EN UNA UNICA RESPUESTA

      # def textChange():
      #    textoLabel.set(respuesta1() + respuesta2())
      # textChange()

#TENGO QUE DECIR QUE ME BORRE LO ANTERIOR#

miRaiz.mainloop()