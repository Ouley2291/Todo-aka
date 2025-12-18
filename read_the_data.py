import Application_UI as app
import csv
import datetime
import customtkinter
import os
"""
def read_the_data_UI():
"""

def load_task_from_csv():
    lista_tresc=[]
    lista_deadline=[]
    if not os.path.exists("zadania.csv"):
        return lista_tresc,lista_deadline
    
    with open("zadania.csv",mode="r",encoding="utf-8") as file:
        reader=csv.reader(file)
        for row in reader:
            if row:
                lista_tresc.append(row[0])
                if len(row)>1:
                    lista_deadline.append(row[1])
                else:
                    lista_deadline.append("Brak daty")
    return lista_tresc,lista_deadline