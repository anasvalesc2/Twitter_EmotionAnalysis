# Import the required libraries
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox as MessageBox

# impor for código---------------------------------------------------------
# utilities

import re  # re para regular expressions
import numpy as np
import pandas as pd
import string
import nltk  # natural language toolkit -> lenguaje natural de los humanos
import seaborn as sns
# from wordcloud import WordCloud
import matplotlib.pyplot as plt
# nltk
from nltk.stem import \
    WordNetLemmatizer  # La lematización es un proceso lingüístico que consiste en hallar el lema correspondiente.
from xgboost import XGBClassifier
# ------------------------------------------------------------------------

from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import sentiment
from nltk import word_tokenize
# analizar=SentimentIntensityAnalyzer()
# Create an instance of Tkinter Frame

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

sentiment = SentimentIntensityAnalyzer()

# EJEMPLO DE COMO SE HACE ESTA PARTE-----------------------------
# text_1 = "The book was a perfect balance between wrtiting style and plot."
# text_2 =  "i hate my life"
# sent_1 = sentiment.polarity_scores(text_1)
# sent_2 = sentiment.polarity_scores(text_2)
# print("Sentiment of text 1:", sent_1)
# print("Sentiment of text 2:", sent_2)
# print(sent_1.get('compound')) #Sara
# import transformers
# FIN DE EJEMPLO----------------------------------------------------------

win = Tk()

# cambio de icono - tweeter
# win.geometry("400x180")
win.resizable(False, False)
win.config(background='#1f2f85')
win.iconbitmap('C:\\Users\\Usuario\\Downloads\\descargatwe_DQe_icon.ico')

# win['bg'] = '#49A'  #Color de la página
win.title("Welcome")
# Set the geometry
win.geometry("880x750")


# Retorna la funcion de un Entry-listo
# def get_data():
#   label.config(text= campo_de_texto.get(), height=3, width=200,font= ('Helvetica 13'))

def get_dataTexto():
    text_intento = campo_de_texto2.get("1.0", 'end-1c')
    sent_intento = sentiment.polarity_scores(text_intento)
    print("Sentiment of text 1:", sent_intento)
    label3.config(text=campo_de_texto2.get("1.0", 'end-1c') + '\n', height=3, width=200, font=("Roboto Cn", 9))
    if ((sent_intento.get('compound')) >= 0.5):
        print("Positivo")
        MessageBox.showinfo("Hi!", "We love your optimism \U0001F601")  # título, mensaje
    # elif (((sent_intento.get('compound'))<=-0.45)|((sent_intento.get('compound'))>-0.5)):
    elif ((sent_intento.get('compound')) < -0.05):
        print("Negativo")
        MessageBox.showinfo("Hi!",
                            "We know times can be difficult so take a look to this helplines worldwide\U0001f641")  # título, mensaje
        MessageBox.showinfo("Hi!",
                            "We know times can be difficult so take a look to this helplines worldwide\U0001f641",
                            webbrowser.open("https://findahelpline.com/"))
    else:
        print("Neutral")
        MessageBox.showinfo("Hi!", "Keep sharing your opinions!")  # título, mensaje
    # MessageBox.showinfo("Hola!", "Hola mundo") # título, mensaje
    # result=campo_de_texto2.get("1.0", 'end-1c')
    # print(result)
    # texto.config(text= entry.get(), height=3, width=300,font= ('Helvetica 13'))
    # con el .get se obtiene lo que está dentro del entry


# Create an Entry Widget
# campo_de_texto = Entry(win, width= 42)
# campo_de_texto.place(relx= .5, rely= .5, anchor= CENTER)

# def test():
#    MessageBox.showinfo("Hola!", "Hola mundo") # título, mensaje
# Button(win, text = "Clícame", command=test).pack()


import webbrowser

# label de texto
label2 = Label(win, text="What's on your mind?", font=("Roboto Cn", 17))
label2.config(bg="#1f2f85", fg="white")
label2.place(relx=0.30, rely=0.01, relwidth=0.39, relheight=0.7)
label2.pack()

# LABEL DONDE SE MUESTRA EL ENTRY
# Inititalize a Label widget
# label= Label(win, text="",width=10,font=('Helvetica 13'))
# label.pack()


# InICIALIZACIÓN DE LABEL PARA CUADRO DE TECTO
label3 = Label(win, text="", width=10, font=('Helvetica 13'))
label3.config(bg="#1f2f85", fg="white")
label3.pack()

# campo de texto para TEXT
campo_de_texto2 = Text(win)
campo_de_texto2.pack()
# campo_de_texto.place(relx= .15, rely= .15)
campo_de_texto2.config(padx=92, pady=5)
campo_de_texto2.config(width=55, height=4)

# BOTON PARA ENTRY
# B1=ttk.Button(win, text= "Click to Show", command= get_data).place(relx= .7, rely= .5, anchor= CENTER)

# BOTON PARA TEXT
B2 = ttk.Button(win, text="Click to Show Text", command=get_dataTexto).place(relx=.50, rely=.20, anchor=CENTER)

# labelestadistica= Label(win, text="ESTADISTICA",font=("Roboto Cn",14))
# labelesradistica.config(bg="#1f2f85",fg="grey")
# labelestadistica.pack()
# labelESTADISTICA.place(relx=0.4, rely=0.8, relwidth=0.6, relheight=0.4)


image = tk.PhotoImage(
    file='C:\\Users\\Usuario\\Pictures\\pr112.gif')  # ponerle \\ en donde este solo \ # Insertarla en una etiqueta.
label = ttk.Label(image=image)
label.pack()
label.place(relx=0.53, rely=0.58, relwidth=0.36, relheight=0.30)

image2 = tk.PhotoImage(
    file='C:\\Users\\Usuario\\Pictures\\pr2011.gif')  # ponerle \\ en donde este solo \ # Insertarla en una etiqueta.
labelima = ttk.Label(image=image2)
labelima.pack()
labelima.place(relx=0.53, rely=0.235, relwidth=0.325, relheight=0.34)

ima3 = tk.PhotoImage(
    file='C:\\Users\\Usuario\\Pictures\\pr302.gif')  # ponerle \\ en donde este solo \ # Insertarla en una etiqueta.
labelima3 = ttk.Label(image=ima3)
labelima3.pack()
labelima3.place(relx=0.15, rely=0.235, relwidth=0.36, relheight=0.66)

# imagen = PhotoImage(file="tablaima")
# imagen1=Label(win, image=imagen, bd=0).pack()
win.mainloop()