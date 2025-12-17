# -*- coding: utf-8 -*-
"""
Created on Wed Dec 17 17:35:25 2025

@author: hubki
"""

import customtkinter


#ustawienia aplikacji
app=customtkinter.CTk()
app.title("To-Do APP")
app.geometry("1200x800")
title_font=customtkinter.CTkFont(weight="bold",size=24)

app.grid_columnconfigure(0, weight=1)
#Przyciski etc
title=customtkinter.CTkLabel(app,text="TO-DO APP",font=title_font)


#miejsce
title.grid(row=0, column=0, padx=20, pady=20)


app.mainloop()


