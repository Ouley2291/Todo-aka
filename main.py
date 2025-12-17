import customtkinter
import csv


# with open('baza.csv', 'w', newline='') as csvfile:
#     fieldnames = ['Data dodania', 'Termin', 'Czynność', 'Kategoria']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writero({'Data dodania': '17.12.2025', 'Termin': '17.12.2025', 'Czynność': 'Aplikacja ToDo', 'Kategoria': 'Studia'})

# with open('baza.csv', 'r', newline='') as csvfile:
#     reader = csv.DictReader(csvfile)

def wyswietl_liste():
    with open('baza.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        for i in reader:
            print(i)

def dodaj_element():
    data = input("Podaj termin ukończenia")
    czynnosc = input("Podaj czynność:")
    kategoria = input("Podaj kategorie:")

    with open('baza.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile)
        writer.writerow({'Data dodania': '17.12.2025', 'Termin': '17.12.2025', 'Czynność': 'Aplikacja ToDo', 'Kategoria': 'Studia'})



while(True):
    try:
        print("Wybierz co chcesz zrobic:")
        print("Wpisz '1' aby wyswietlic liste.")
        print("Wybierz '2' aby dodac nowy element do listy.")
        wybor = input("Twoj wybor: ")
        wybor = int(wybor)
    except ValueError:
        print("Prosze wpisac liczbe calowita")
    if(wybor in [1,2]):
        break
    print("Prosze wpisac liczbe calowita (1 lub 2)")

match wybor:
    case 1:
        wyswietl_liste()
    case 2:
       dodaj_element()


    