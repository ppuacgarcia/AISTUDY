import random
import tkinter as tk
from tkinter import ttk
from turtle import bgcolor, width
from tkinter import *
from PIL import Image, ImageTk
from tkinter import font
import os
from datetime import datetime
import requests
from PIL import Image
#import os
#import openai
#variables generales
database=[]
database=["¿Cuál es el contenido de la ficha 5? \na) I: Ciclo de vida del mosquito Aedes aegypti \nb) C: Determinación de incidencia de dengue en la población escolar \nc) I:  Experimento de Francesco Redi \nd) I: Clasificar artrópodos",
          " ¿Cuál es el tema principal de la ficha 8? \na) I: La materia viva \nb) I: La genética \nc) I: La organización de la vida: la célula \nd) C: Evaluar la calidad del agua",
          "¿Qué ficha aborda la clasificación de los seres vivos? \na) I: Ficha 3 \nb) C: Ficha 4 \nc) I: Ficha 5 \nd) I: Ficha 6",
          "¿Qué tema trata la ficha 2? \na) C: La materia viva \nb) I: La genética \nc) I: La organización de la vida: la célula \nd) I: La reproducción",
          "¿Qué es lo que sugiere la organización de los seres vivos según el texto? \na) C: Que primero fueron agregados de moléculas. \nb) I: Que surgieron a partir de los meteoritos. \nc) I: Que se originaron a partir de átomos y moléculas. \nd) I: Que la radiación cósmica puede matar a los microorganismos.",
          "¿Cuál es la teoría más aceptada actualmente sobre el origen de la vida según el texto? \na) I: La teoría del creacionismo. \nb) I: La teoría de la panspermia. \nc) C: La teoría de la generación espontánea. \nd) I: La teoría del diseño inteligente.",
          "¿Cuál es el contenido de la ficha 5? \na) I: Ciclo de vida del mosquito Aedes aegypti \nb) C: Determinación de incidencia de dengue en la población escolar \nc) I: Experimento de Francesco Redi \nd) I: Clasificar artrópodos",
          "¿Cuál es la definición más precisa de evolución según el texto? \na) I: El resultado de cambios anatómicos y fisiológicos de los seres vivos. \nb) I: El conjunto de cambios que experimentan los seres vivos con la finalidad de adaptarse a su hábitat. \nc) C: El conjunto de cambios que experimentan los organismos a través del tiempo. \nd) I: El resultado de la supervivencia de determinadas especies con características favorables a su medio.",
          "¿Cuál es la evidencia que se menciona en el texto para demostrar la evolución de las especies? \na) I: La presencia de rudimentos de patas en el esqueleto de las serpientes. \nb) I: La comparación entre una pata de ave y una mano humana. \nc) C: Las similitudes entre el genoma humano y el genoma del chimpancé. \nd) I: Un mosquito atrapado en ámbar."
          "¿Cuál es la teoría que sostiene que los caracteres adquiridos no se fijan en nuestro ADN, por lo tanto no pueden pasar de una generación a otra? \na) I: La selección natural. \nb) I: El uso y desuso. \nc) I: La supervivencia del más apto. \nd) C: El lamarckismo."
          "¿Cuántos productos tradicionales de exportación tiene Guatemala y cuáles son? \na) I: 4: Café, Banano, azúcar, cardamomo \nb) I: 6: Café, Banano, azúcar, carne de res, algodón, cardamomo \nc) C: 7: Café, Banano, azúcar, carne de res, algodón, cardamomo, alta Verapaz \nd) I: 8: Café, Banano, azúcar, carne de res, algodón, cardamomo, alta Verapaz, maíz",
          "¿Cuáles son los principales mercados de exportación de Guatemala? \na) I: China, Japón, Estados Unidos, México \nb) I: Estados Unidos, países centroamericanos, México, Europa \nc) I: Centroamérica, Europa, Asia, Oceanía \nd) C: Estados Unidos, países centroamericanos, México, otros",
          "¿Cuál es la forma de pago más segura a nivel internacional? \na) I: Paypal \nb) I: Transferencias bancarias \nc) C: Cartas de crédito \nd) I: Giros",
          "¿Para qué sirven las notas de crédito? \na) C: Para fijar el precio de compra de un producto en la bolsa de valores. \nb) I: Para asegurar la calidad de los productos exportados. \nc) I: Para hacer transferencias bancarias de grandes cantidades de dinero. \nd) I: Para obtener un certificado de origen de los productos exportados.",
          "¿Qué plataforma se utiliza para generar los documentos de exportación en Guatemala? \na) I: Paypal \nb) C: SEADER WEB \nc) I: Western Union \nd) I: VUPE",
          "¿Cuáles son las estructuras básicas que intervienen en la cefalea de primer orden? \nA) I: Las terminaciones periféricas del nervio trigémino \nB) I: Los sistemas moduladores del dolor en el encéfalo \nC) I: Los gruesos vasos intracraneales y la duramadre \nD) C: Todas las anteriores",
          "¿Qué tipo de dolor de cabeza es de inicio súbito, intensidad severa o muy severa, y empeoramiento con maniobras de valsalva? \nA) I: Cefalea crónica progresiva \nB) C: Cefalea aguda de reciente comienzo \nC) I: Cefalea aguda recurrente \nD) I: Cefalea crónica no progresiva",
          "¿Cuáles son las causas de la cefalea aguda de reciente comienzo? \nA) I: Anomalías oculares y alteraciones dentales \nB) I: Migraña y cefalea tensional \nC) I: Cefalea en racimos y cefalea tusígena \nD) C: Infecciones SNC y foco ORL",
          "¿Cuál es el tipo de cefalea que corresponde a procesos vasculares y se presenta con características pulsátiles? \nA) I: Cefalea crónica no progresiva \nB) C: Cefalea aguda recurrente \nC) I: Cefalea crónica progresiva \nD) I: Ninguna de las anteriores",
          "¿Qué es la insuficiencia renal aguda y cómo se manifiesta?\nA) I: Es un proceso irreversible que afecta la función renal de manera crónica. \nB) C: Es un proceso que puede desarrollarse en días o semanas y se caracteriza por una disminución súbita del filtrado glomerular. \nC) I: Es un proceso que solo afecta a personas mayores de 60 años. \nD) I: Es un proceso que se desarrolla en meses y se caracteriza por una disminución gradual del filtrado glomerular.",
          "¿Cuáles son los criterios para clasificar la insuficiencia renal aguda según RIFLE?\nA) I: Criterios de Fórmula General. \nB) C: Criterios de Función Urinaria. \nC) I: Criterios de Función Glomerular. \nD) I: Criterios de Alta Especificidad.",
          "¿Cuáles son los mecanismos fisiopatológicos de la insuficiencia renal aguda?\nA) I: Disminución de la filtración glomerular y obstrucción tubular. \nB) I: Incremento de la reabsorción tubular y obstrucción tubular. \nC) C: Disminución de la filtración glomerular e incremento de la reabsorción tubular. \nD) I: Incremento de la permeabilidad capilar y disminución de la presión arterial.",
          "¿Cuáles son las causas de la insuficiencia renal aguda de origen prerrenal?\nA) C: Hipovolemia, disminución del gasto cardíaco, vasodilatación periférica, alteración de las respuestas autorreguladoras renales. \nB) I: Hipovolemia, disminución del gasto cardíaco, vasoconstricción renal, alteración de las respuestas autorreguladoras renales. \nC) I: Hipovolemia, disminución del gasto cardíaco, vasoconstricción renal, vasodilatación periférica.\nD) I: Hipovolemia, aumento del gasto cardíaco, vasoconstricción renal, alteración de las respuestas autorreguladoras renales."]
colorbg='#FFFFFF'
colortext='#572364'
fonttxt='Bold'
colorL='#737373'
#frame definitions
pw = Tk()
pw.geometry('1200x675')
pw.configure(bg=colorbg)
pw.resizable(0,0)
pw.title('AI Study')
fPrincial = Frame(pw,width=1200,height=675,bg=colorbg)
fPrincial.place(x=0, y=0)
#Pregunta Label
lPregunta=Label(fPrincial, text='Pregunta')
lPregunta.place(x=100,y=210)
lPregunta.config(bg=colorbg,font=(fonttxt,15),fg=colortext,wraplength=800)
PCorrecta=-1
#Funciones
def button2():
    print("")
def Res0():
    button(0)
def Res1():
    button(1)
def Res2():
    button(2)
def Res3():
    button(3)
def button(index):
    if(index==PCorrecta):
        tk.messagebox.showinfo(title=None, message="Correcto")
    else:
        tk.messagebox.showerror(title=None, message="INCORRECTO")
def button1():
    print('holamundo')
    def separar(txt):
        return txt.split("\n")
    def correcto(res,pos):
        if res.find("C:")!=-1:
            respuesta=res.replace('C:', '')
            return [respuesta,pos]
        else:
            respuesta=res.replace('I:', '')
            return [respuesta,-1]
    rnd = random.randint(0, 20)
    print(rnd)
    texto = database[rnd]
    preguntas=separar(texto)[0]
    respuestas=[]
    respuestas=[separar(texto)[1],separar(texto)[2],separar(texto)[3],separar(texto)[4]]
    global PCorrecta
    PCorrecta=-1
    for i in range (0,4):
        respuestas[i]=correcto(respuestas[i],i)
        if(respuestas[i][1]!=(-1)):
            print("la respuesta correcta es ",str(i))
            PCorrecta=i
            

    lPregunta.config(text=preguntas)
    Respuesta1.config(text=respuestas[0][0],command=Res0,wraplength=400)
    Respuesta2.config(text=respuestas[1][0],command=Res1,wraplength=400)
    Respuesta3.config(text=respuestas[2][0],command=Res2,wraplength=400)
    Respuesta4.config(text=respuestas[3][0],command=Res3,wraplength=400)
def btn(self,x, y, text, bcolor, fcolor, command, font,siz, tipe,wdt,ht,img):
    def on_enter(e):
        button['background'] = colortext
        button['foreground'] = bcolor               
    def on_leave(e):
        button['background'] = bcolor
        button['foreground'] = colortext
    button = Button(self, width=wdt, height=ht, text=text, fg  = colortext, bg=bcolor, 
                    command=command, border=0, activebackground=bcolor, activeforeground=fcolor
                    ,font=(font, siz, tipe),image=img,justify=tk.CENTER)
    button.bind("<Enter>", on_enter)
    button.bind("<Leave>", on_leave)
    button.place(x=x, y=y)
    return button
#pdfEntry
#pdf=str()
#pdfEntry = Entry(fPrincial,textvariable=pdf)
#pdfEntry.config(width=30,font=(fonttxt,12))
#pdfEntry.place(x=425,y=180)
#LABEL
#Title Label
lTitle=Label(fPrincial, text='AI STUDY')
lTitle.place(x=30,y=0)
lTitle.config(bg=colorbg,font=(fonttxt,40),fg=colortext)

#label linea 
lCabecera=Label(fPrincial, text=' ')
lCabecera.place(x=0,y=60)
lCabecera.config(bg=colorL,font=(fonttxt,1),fg=colortext,width=1200,height=1)
#pdf Button
EntrarB=btn(fPrincial,490,100,'Hazme una pregunta',colorbg,colortext,button1,'Arial', 12,'bold',15,5,"")
EntrarB.config(wraplength=100)
#respuestasbutton
Respuesta1=btn(fPrincial,100,350,'Respuesta',"#DC58FC",colortext,button,'Arial', 10,'bold',50,8,"")
Respuesta2=btn(fPrincial,100,500,'Respuesta',"#DC58FC",colortext,button,'Arial', 10,'bold',50,8,"")
Respuesta3=btn(fPrincial,600,350,'Respuesta',"#DC58FC",colortext,button,'Arial', 10,'bold',50,8,"")
Respuesta4=btn(fPrincial,600,500,'Respuesta',"#DC58FC",colortext,button,'Arial', 10,'bold',50,8,"")
#home button
homeImg= (Image.open("images/home.png"))
resized_imageHome= homeImg.resize((50,50), Image.ANTIALIAS)
new_homeImg= ImageTk.PhotoImage(resized_imageHome)
home=btn(fPrincial,370,1,'',colorbg,colortext,button2,'Arial', 12,'bold',50,50,new_homeImg)
#Notas button
NotasImg= (Image.open("images/notas.png"))
resized_imageNotas= NotasImg.resize((50,50), Image.ANTIALIAS)
new_NotasImg= ImageTk.PhotoImage(resized_imageNotas)
notas=btn(fPrincial,470,1,'',colorbg,colortext,button2,'Arial', 12,'bold',50,50,new_NotasImg)
#Comunity button
comunityImg= (Image.open("images/comunity.png"))
resized_imageComunity= comunityImg.resize((50,50), Image.ANTIALIAS)
resized_imageComunity=resized_imageComunity.convert(colors=0)
new_comunityImg= ImageTk.PhotoImage(resized_imageComunity)
comunity=btn(fPrincial,570,1,'',colorbg,colortext,button2,'Arial', 12,'bold',50,50,new_comunityImg)

#Menu button
hamImg= (Image.open("images/ham.png"))
resized_imageMenu= hamImg.resize((50,50), Image.ANTIALIAS)
new_hamImg= ImageTk.PhotoImage(resized_imageMenu)
comunity=btn(fPrincial,1140,2,'',colorbg,colortext,button2,'Arial', 20,'bold',50,50,new_hamImg)
pw.mainloop()