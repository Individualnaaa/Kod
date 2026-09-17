def zrob_herbate(rodzaj_herbaty, imie="Ania"):
    print(f"Przygotuj kubek {imie}")
    print(f"Przgotuj {rodzaj_herbaty}")
    print("Nalać wody do czajnika")
    print("Zagotuj wodę")
    print("Zalej wodę")
    print("Wymij trebke")
    print(f"Twoja herbata dla {imie} jest gotowa")

zrob_herbate("czarna")
    # najpierw parametry bez wartości,a potem z wartoscią


# poprawić zgodnie z arturem
# def zrob_herbate(rodzaj_herbaty="czarna", imie) -> None:
#     print(f"Przygotuj kubek {imie}")
#     print(f"Przgotuj {rodzaj_herbaty}")
#     print("Nalać wody do czajnika")
#     print("Zagotuj wodę")
#     print("Zalej wodę")
#     print("Wymij trebke")
#     print(f"Twoja herbata dla {imie} jest gotowa")

# print(zrob_herbate(imie="Tomek"))


#separator w wybranym dla nas rodzaju
print("zrob", "herbate", sep="xDs--")