# -*- coding: utf-8 -*-
"""
Created on Wed Dec 17 17:35:25 2025

@author: hubki
"""

import customtkinter
import add_task

#kod przerobiony na klasy 
class App(customtkinter.CTk): #moja klasa dziedziczy po klasie CTk
    def __init__(self): #konstruktor i tam sie ustawia parametry jka tworze obiekt swojej klasy
        super().__init__() #super odnosi sie do rodzica (czyli tu customtkinter.CTk)
        #i ta linijka wyzej uruchamia kod startowy biblioteki, a pozniej dodaje moje ustawienia

        
        #dalsze ustawienia 
        self.title("To-Do app")
        self.geometry("1200x800")
       
       #siatka dynamiczna - zmieniajcie jak chcecie
        self.grid_columnconfigure((0,1,2), weight=1) #dla kolumn 1,2,3 waga = 1 czyli kolumna zabierze cala wolna przestrzen
        self.grid_rowconfigure((0,1,2), weight=1)

        #teraz przycisk
        #trzeba zrobic przycisk zeby polaczyc go z add task
        #plus tam ustawcie jakies ladne kolorki 
        #a pozniej go ustawcie gdzie ladnie na tej siatce pierdolonej

        #self.button = customtkinter.CTkButton(self, text="add task", #fg_color=, hover_color, command) 
        #self.button.grid(row=, column=, padx=, pady=, sticky=, columnspan albo i nie) 

    
app = App()
app.mainloop()













#to bylo
"""#funkcja na przycisk - z tutorialu
def button_callback():
    print("button pressed")


#ustawienia aplikacji
app=customtkinter.CTk()
app.title("To-Do app")
app.geometry("1200x800")
title_font=customtkinter.CTkFont(weight="bold",size=24)



#siatka
#bez tego wszystko jest po lewej stronie 
#wiec to "centruje" tytul i my_button
#tupla ustawia kolumny na te sama wage, dzieki czemu checkboxy sa rowno rozlozone
app.grid_columnconfigure((0, 1), weight=1)





#przycisk z tutorialu
button = customtkinter.CTkButton(app, text="my_button", command=button_callback)
button.grid(row=1, column=0, padx=20, pady=20, sticky="ew", columnspan=2) 
#dodalam sticky i to rozszesza komorke przycisku na cale okno


#przyciski na checkbox - zeby sprawdzic jak dzialaja
#ustawilam je na razie po lewej stronie pod soba
checkbox_1 = customtkinter.CTkCheckBox(app, text="checkbox 1")
checkbox_1.grid(row=3, column=0, padx=20, pady=(0, 20), sticky="w")
checkbox_2 = customtkinter.CTkCheckBox(app, text="checkbox 2")
checkbox_2.grid(row=3, column=1, padx=20, pady=(0, 20), sticky="w")

app.mainloop()"""


