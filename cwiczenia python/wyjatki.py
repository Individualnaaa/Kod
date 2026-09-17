
# printowanie 

imie = input("podaj imie: ")

try: 
    wiek = int(input("podaj wiek: "))
except:
    wiek = "Nie podano liczby"

print(f"Hello {imie}. Masz {wiek} lat")


# stworz funkcje dzielenia, niech przjmie 2 liczby
# 

# def dzielenie(liczba1, liczba2)
#     wynik = liczba1 + liczba2
#     return wynik
# print(wynik)


# spisać z wujątki i zadania
def dzielenie():
    while True:
        try:
            num1 = int(input("Podaj liczbę1: "))
            break
        except:
            print("To nie jest liczba")
    while True:
        try:
            num2 = int(input("Podaj drugą przez którą chcesz podzielić: "))
            if num2 == 0:
                print("nie możemy dzielić przez 0")
                continue
            break
        except:
            print("To nie jest dobra liczba")



