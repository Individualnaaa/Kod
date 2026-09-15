punkty = 80

if punkty >= 90:
    ocena = "5"
elif punkty >= 75:
    ocena = "4"
elif punkty >= 60:
    ocena = "3"
else:
    ocena = "2"

print(ocena)

imie = "Asia"
jaka_lazienke_wybrac = "damska" if imie.endswith("a") else "męską"
print("Łazienka", jaka_lazienke_wybrac)