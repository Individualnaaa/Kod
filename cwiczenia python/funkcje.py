# print("hello", "yo")


# każda funkcja, żeby mogła coś wykonać, to ktoś musiał napisać kod
# żeby taka funkcja działała
# podświetlając - widzimy dodatkowe instrukcje, dokumentację 
# lewy cntr i słowo print - pokazuje nam kod tej funkcji, jak to ma działać


# Ania
# print("Przygotuj kubek Ani")
# print("Przgotuj herbate czarną")
# print("Nalać wody do czajnika")
# print("Zagotuj wodę")
# print("Zalej wodę")
# print("Wymij trebke")
# print("Twoja herbata dla Ani jest gotowa")

# funkcje



def zrob_herbate(imie, rodzaj_herbaty):
    print(f"Przygotuj kubek {imie}")
    print(f"Przgotuj {rodzaj_herbaty}")
    print("Nalać wody do czajnika")
    print("Zagotuj wodę")
    print("Zalej wodę")
    print("Wymij trebke")
    print(f"Twoja herbata dla {imie} jest gotowa")

print("To już nie jest funkcja\n")
zrob_herbate("Ania", "czarna")



slownik_ludzi = {
    "Ania": "czarna",
    "Adam": "zielona"
}

def zrob_herbate1(imie, herbata):
    print(f"Przygotuj kubek {imie}")
    print(f"Przgotuj {herbata}")
    print("Nalać wody do czajnika")
    print("Zagotuj wodę")
    print("Zalej wodę")
    print("Wymij trebke")
    print(f"Twoja herbata dla {imie} jest gotowa\n")

for imie, herbata in slownik_ludzi.items():
    zrob_herbate(imie, herbata)



# do spisania z prezki funkcje_wprowadzenia od artura
# imiona = ["adam", "bartek"]

# for osoba in imiona:
#     zrob_herbate(osoba)


# przykład funkcji dodawania

# def dodaj(liczba_1, liczba_2):
#     wynik = liczba_1 + liczba_2
#     return print(wynik)
# dodaj(2, 4)

wynik = "a b c".split(" ")
print(wynik)
