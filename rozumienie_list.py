lista_poteg = []

for liczba in range(1, 6):
    lista_poteg.append(liczba ** 2)

print(lista_poteg)


wynik = [liczba ** 2 for liczba in range(1, 6)]
print("list comprehension ", wynik)