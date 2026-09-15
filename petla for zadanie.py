slownik_owocow = {
    "klucz": "wartosc",
    "Artur": "Ananas",
    "Basia": "Banan",
    "Celina": "Cytryna",
    "Dawid": "Daktyle",
    "Ewa": "Eszeweria"
}
# all = list(slownik_owocow.keys())
# for zenskie in all:
#     if (zenskie.endswith("a")):
#         print(zenskie)

# for imiona in list(slownik_owocow.keys()):
#     if (imiona.endswith("a")):
#         print(imiona)

for owoc in list(slownik_owocow.values()):
    if len(owoc) > 6 and owoc != "wartosc":
        print(owoc)