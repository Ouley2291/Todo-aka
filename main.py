import customtkinter
import csv


with open('baza.csv', 'w', newline='') as csvfile:
    fieldnames = ['Data dodania', 'Termin', 'Czynność', 'Kategoria']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writero({'Data dodania': '17.12.2025', 'Termin': '17.12.2025', 'Czynność': 'Aplikacja ToDo', 'Kategoria': 'Studia'})

with open('baza.csv', 'r', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
