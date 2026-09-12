slownik_owocow = {
    "Artur": "Ananas",
    "Basia": "Banan",
    "Celina": "Cytryna",
    "Dawid": "Daktyle",
    "Ewa": "Eszeweria"
}

klucze = slownik_owocow.keys()
print(f"klucze to: {klucze}")
print("typ kluczy", type(klucze))

lista_kluczy = list(klucze)
print(f"lista_kluczy to: {lista_kluczy}")
print("typ lista kluczy", type(lista_kluczy))

# Metody zwracające wartości (values)
wartosci = slownik_owocow.values()
print(f"wartości to: {wartosci}")
print("typ wartosci", type(wartosci))

# Metody zwracające pary
pary = slownik_owocow.items()
print(f"pary to: {pary}")
print("typ par", type(pary))

#pojedyncza para

print("Pojedyncza para", list(pary)[0])

list(   (1, 2, 3, 4)   )
liczby = dict(a=1, b=1, c=1, d=1)
print(liczby)

liczny = {
    "a": 1,
    "b": 2,
    "c": 3
}
print(liczny)