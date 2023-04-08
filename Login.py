import tkinter as tk
from turtle import bgcolor, width
from tkinter import *
from PIL import Image, ImageTk
from tkinter import font
import os
from datetime import datetime
import requests

#variables generales
colorbg='#FFFFFF'
colortext='#572364'
fonttxt='Bold'
#frame definitions
pw = Tk()
pw.geometry('1200x675')
pw.configure(bg='#3F5657')
pw.resizable(0,0)
pw.title('AI Study')
fPrincial = Frame(pw,width=1200,height=675,bg=colorbg)
fPrincial.place(x=0, y=0)
#pdfEntry
pdf=str()
pdfEntry = Entry(fPrincial,textvariable=pdf)
pdfEntry.config(width=30,font=(fonttxt,12))
pdfEntry.place(x=100,y=100)
#API CHAT-GPT
apiKey='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'
prompt=input("INGRESA UNA PREGUNTA")
Headers={
    "Authorization":f"Bearer{apiKey}",
    "Content-Type":"application/json"
}
data={
    "model":"gpt-3.5-turbo",
    "messages":[{
            "role":"user",
            "content":prompt
        }
    ]
}
url="https://api.openai.com/v1/chat/completions"
response=requests.post(url,headers=Headers,json=data)
print("RESPUESTA")
print(response)
ans=response.json()['choices'][0]['message']['content']
print("\n\n"+ans)
#Title Label
lTitle=Label(fPrincial, text='AI STUDY')
lTitle.place(x=80,y=0)
lTitle.config(bg=colorbg,font=(fonttxt,40),fg=colortext)

#pdf Button
def button1():
    print('holamundo')
def on_enter(e):
    button['background'] = colortext
    button['foreground'] = '#FFFFFF'        
            
def on_leave(e):
    button['background'] = '#ffffff'
    button['foreground'] = colortext
button = Button(pw, width=15, height=1, text='Entrar', fg  = colortext, bg='#3F5657', 
                command=button1, border=0, activebackground='#3F5657', activeforeground='#ffffff'
                ,font=('Arial', 16,'bold'))
button.bind("<Enter>", on_enter)
button.bind("<Leave>", on_leave)
button.place(x=250, y=370)
pw.mainloop()