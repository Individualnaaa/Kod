# druk od 1 do 10

# print("1")
# print("2")
# print("3")

# # pętla for
# lista_liczba = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for liczba in lista_liczba:
#     print(liczba)

# lista_imion = ["Adam", "Basia", "Cezary", "Darek"]

lista_imion = ["Adam", "Basia", "Cezary", "Damian", "Ewa"]
# Używając for napisz do każdej osoby piszać ich imie upperem

for imie in lista_imion:
    print("Start obiegu", imie)
    print(f"Cześć {imie.upper()}")
    print("Koniec obiegu", imie,"\n")