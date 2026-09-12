krotka = ("Artur", "Basia", "Czarek", "Artur")

print(krotka)
print(krotka[0])

# Nie można zmieniać elementów

# Można odchodzić od zasad :D

krotkalista = list(krotka)
krotkalista[0] = "Marek"
krotka = tuple(krotkalista)
print(krotka)