# -*- coding: utf-8 -*-
"""
Created on Wed Dec 17 17:35:25 2025

@author: hubki
"""
import read_the_data
import customtkinter
import add_task


import os




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

        #przycisk dodaj
        self.add_button=customtkinter.CTkButton(self, text="Dodaj Zadanie",command=self.add_task_action)
        self.add_button.grid(row=0,column=0,padx=20,pady=20,sticky="ew")
        
        self.refresh_tasks()
        
    def refresh_tasks(self):
        for widget in self.winfo_children():
            if widget != self.add_button:
                widget.destroy()
        tresc_zadan,daty_zadan,isdone=read_the_data.load_task_from_csv()
        
        for index,(tresc,data) in enumerate(zip(tresc_zadan,daty_zadan,isdone)):

            # Isdone? if 1 kasacja bo continue w for
            if int(isdone) == 1:
                continue


            full_text=f"{tresc}  | Termin: {data}"
            checkbox=customtkinter.CTkCheckBox(self, text=full_text,command=)

            checkbox.grid(row=index+1,column=0,padx=20,pady=5,sticky="w")
            
    def add_task_action(self):
        add_task.add_task_Ui()
        self.refresh_tasks()
        
    
    # - - - -- - - - - - - Funkcje od Oliveiera
    def delete_line(old_file, tresc):
        with open(old_file, 'r') as old, open('temp.txt', 'w') as temp:
            for linia in old:
                if linia.strip() != tresc:
                    temp.write(linia)

            os.replace('temp.txt', old_file)
    


        #teraz przycisk
        #trzeba zrobic przycisk zeby polaczyc go z add task
        #plus tam ustawcie jakies ladne kolorki 
        #a pozniej go ustawcie gdzie ladnie na tej siatce pierdolonej

        #self.button = customtkinter.CTkButton(self, text="add task", #fg_color=, hover_color, command) 
        #self.button.grid(row=, column=, padx=, pady=, sticky=, columnspan albo i nie) 

if __name__=="__main__":
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


