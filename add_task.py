# -*- coding: utf-8 -*-
"""
Created on Thu Dec 18 13:41:07 2025

@author: hubki
"""
import Application_UI as app
import csv
import datetime
import customtkinter
import re
'''
Funkcja dodająca zadanie
zwraca tresc zadania oraz date ukończenia zadania
Do dodania zapis do CSV

'''
def add_task_Ui():
    dialog=customtkinter.CTkInputDialog(text="Wpisz nazwe zadania",title="Zadanie")
    text_tresc=dialog.get_input()
    text_tresc.strip()
    while(True):
        dialog_date=customtkinter.CTkInputDialog(text="Wpisz date ukończenia zadania (w formacie DD-MM-YYYY",title="Data")
        text_date=dialog_date.get_input()
        text_date.strip()
        if re.search("((0[1-9])|1[0-9]|2[0-9]|3[0-1])-((0[1-9])|1[0-2])-[0-9]{4}",text_tresc):
            break

    text_date.split("-")
    if text_tresc and text_date:
        with open('zadania.csv', mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([text_tresc, text_date, datetime.datetime.now().strftime("%Y-%m-%d %H:%M")]) 
    return text_tresc,text_date



