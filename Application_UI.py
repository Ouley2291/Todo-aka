# -*- coding: utf-8 -*-
"""
Created on Wed Dec 17 17:35:25 2025

@author: hubki
"""

import customtkinter

#kod przerobiony na klasy 
class App(customtkinter.CTk): #moja klasa dziedziczy po klasie CTk
    def __init__(self): #konstruktor i tam sie ustawia parametry jka tworze obiekt swojej klasy
        super().__init__() #super odnosi sie do rodzica (czyli tu customtkinter.CTk)
        #i ta linijka wyzej uruchamia kod startowy biblioteki, a pozniej dodaje moje ustawienia

       
        #dalsze ustawienia sa moje
        self.title("To-Do app")
        self.geometry("1200x800")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        #frames
        self.checkbox_frame = customtkinter.CTkFrame(self)
        self.checkbox_frame.grid(row=1, column=0, padx=10, pady=(10, 10), sticky="nsw", rowspan=3)


        #ckeckboxy
        self.checkbox_1 = customtkinter.CTkCheckBox(self, text="checkbox 1")
        self.checkbox_1.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w") #w to west czyli bedzie tylko po lewej
        self.checkbox_2 = customtkinter.CTkCheckBox(self, text="checkbox 2")
        self.checkbox_2.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="w")

        #teraz przycisk
        #dodajac self przycisk staje sie wlasnoscia calego obiektu, nie jest sprzatany z pamieci pozniej
        self.button = customtkinter.CTkButton(self, text="my button", command=self.button_callback) 
        self.button.grid(row=0, column=0, padx=10, pady=10, sticky="n", columnspan=2) #ew to east/west wiec sie rozciagnie sie od lewej do prawej


    #funkcja dla przycisku
    def button_callback(self):
        print("button pressed")
    
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


