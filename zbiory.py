lista = ["ala", "kot", 1, 2.89, 1]
zbior = {"ala", "kot", 1, 2.89, 1}

print(lista)
print(zbior)

imie = "Adam"
print(f"Czy {imie} w zbiorach?:", imie in zbior)

zbior.add("Maciej")
zbior.update(["Ania", "Kasia"])
zbior.remove("ala")

print(zbior)

# przyklady dzialan

zbior2 = {"mama", "tata", "kot"}

zbior3 = zbior & zbior2
print(zbior3)

zbior4 = zbior | zbior2
print(zbior4)

zbior5 = zbior ^ zbior2
print(zbior5)

lista_meskich_imion = ["Artur", "Bartosz", "Cezary", "Bartosz"]
print("Lista imion bez duplikatow", lista_meskich_imion)

zbior_imion = list(set(lista_meskich_imion))
print("Lista bez duplikatow", zbior_imion)