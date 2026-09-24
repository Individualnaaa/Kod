
plik_do_edycji = "plik2.txt"
with open(plik_do_edycji, "r") as mój_plik:
    lista_linii = mój_plik.readlines()
    # print(lista_linii)

dousuniecia = lista_linii[2]
lista_linii.remove(dousuniecia)

print(lista_linii)

with open(plik_do_edycji, "w") as mój_plik:
    mój_plik.writelines(lista_linii)