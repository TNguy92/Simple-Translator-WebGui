from tkinter import *
import requests
import sys
#----------------------------------
#Tkinter windows creation:
root = Tk()
root.geometry("500x300")
root.title("Simple Translation - Thomas Nguyen")
#----------------------------------
#Entry box:
Entry_1 = Entry(root)
Entry_1.delete(0, END)
Entry_1.insert(0, "")
#----------------------------------
#Functions:

def Translate_FR():
    url = "http://www.transltr.org/api/translate?text= " + Entry_1.get() + "&to=fr&from=en"
    response = requests.get(url)
    data = response.json()
    tt = data['translationText']
    Entry_2.insert(0, tt)

def Translate_ES():
    url = "http://www.transltr.org/api/translate?text= " + Entry_1.get() + "&to=es&from=en"
    response = requests.get(url)
    data = response.json()
    tt = data['translationText']
    Entry_2.insert(0, tt)

def Translate_DE():
    url = "http://www.transltr.org/api/translate?text= " + Entry_1.get() + "&to=de&from=en"
    response = requests.get(url)
    data = response.json()
    tt = data['translationText']
    Entry_2.insert(0, tt)


#----------------------------------------
#Labels:
Label_SupportedLang = Label(root, text="The supported languages are French, Spanish, and Germany: ")
Label_ALL = Label(root, text="Enter Text Desired For Translation Below:")
#----------------------------------------
#Buttons:
Button_Submit_FR = Button(root, text="French", bd=3, command=Translate_FR)
Button_Submit_ES = Button(root, text="Spanish", bd=3, command=Translate_ES)
Button_Submit_DE = Button(root, text="Germany", bd=3, command=Translate_DE)
#--------------------------------------------------------------
#Entry box 2
Entry_2 = Entry(root)
Entry_2.delete(0, END)
#---------------------------------------------------------------
#Packings:
Label_SupportedLang.pack()
Label_ALL.pack()
Entry_1.pack()
Entry_2.pack()
Button_Submit_FR.pack()
Button_Submit_ES.pack()
Button_Submit_DE.pack()
#--------------------------------------------------------------
#Loops:
root.mainloop()
#--------------------------------------------------------------