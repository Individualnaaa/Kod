lista = ["Adam", "Basia", "Rysiek"]

# for imie in lista:
#     print("Start", imie)
#     if imie == "Basia":
#         print("Continue")
#         continue
#     print("Zwracam duże imie", imie.upper())
#     print("Koniec obiegu")

# continue skipuje 
# break przerywa całą pętle

for imie in lista:
    print("Start", imie)
    if imie == "Basia":
        print("break")
        break
    print("Zwracam duże imie", imie.upper())
    print("Koniec obiegu")