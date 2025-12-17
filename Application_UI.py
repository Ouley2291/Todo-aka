# -*- coding: utf-8 -*-
"""
Created on Wed Dec 17 17:35:25 2025

@author: hubki
"""

import customtkinter


#ustawienia aplikacji
app=customtkinter.CTk()
app.title("To-Do APP")
app.geometry("600x400")
title_font=customtkinter.CTkFont(weight="bold",size=24)

#Przyciski etc
title=customtkinter.CTkLabel(app,text="TO-DO APP",font=title_font)



app.mainloop()


