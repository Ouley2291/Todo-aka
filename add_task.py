# -*- coding: utf-8 -*-
"""
Created on Thu Dec 18 13:41:07 2025

@author: hubki
"""
import Application_UI as app
import csv
import datetime
import customtkinter
'''
Funkcja dodająca zadanie
zwraca tresc zadania oraz date ukończenia zadania
Do dodania zapis do CSV

'''
def add_task_Ui():
    dialog=customtkinter.CTkInputDialog(text="Wpisz nazwe zadania")
    text_tresc=dialog.get_input()
    dialog_date=customtkinter.CTkInputDialog(text="Wpisz data ukończenia zadania")
    text_date=dialog_date.get_input()
    if text_tresc and text_date:
        # Otwieramy plik w trybie 'a' (append)
        with open('zadania.csv', mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            # Zapisujemy wiersz z danymi
            writer.writerow([text_tresc, text_date, datetime.datetime.now().strftime("%Y-%m-%d %H:%M")]) 
    return text_tresc,text_date
    

add_task_Ui()

