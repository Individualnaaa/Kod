# funkcja wykonuje się do returna - ala break, tylko do tego momentu
def hello():
    print(1)
    print(2)
    print(3)
    return "xd"
    print(4)

hello()


# def dodaj(liczba1, liczba2):
#     wynik = liczba1 + liczba2
#     return wynik
# print(dodaj(2, 4, 5))

# drugi sposób

def dodaj(*liczby):
    wynik = 0
    for liczba in liczby:
        wynik += liczba
    return wynik
wynik = dodaj(2, 4, 5, 6)
print(wynik)


def hello(*imiona):
    for imie in imiona:
        print(f"Hello {imie}")

hello("Ania", "Bartek", "Czarek")

lista_imion = ["Ania", "Barek", "Czarek"]
hello(lista_imion) # dajemy 1 worek, w środku jest 3 elementy
hello(*lista_imion) # przekazujemy 3 argumenty z worka


# kwargs
# def hello2(**osoba):
#     for imie, wiek in osoba.items():
#         print(f"Hello {imie} ma {wiek} lat")


#coś tu nie dziala - kwargs, od artura
# slownik = {
#     "Ania": 20,
#     "Barte": 34,
#     "Czarek": 44
# }

# hello(Ania=20, Barte=25, Czarek=44)
# hello(**slownik)

# spisać przykład z ocenami z funkcje kwargs
# def zapisz_oceny_ucznia(imie, *oceny):
#     suma_ocen = 0
#     for ocena in oceny:
