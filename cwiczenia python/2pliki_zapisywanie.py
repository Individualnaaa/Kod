nazwa_pliku = "plik1.txt"
poziom_uprawnien_write = "w"
plik1 = open(nazwa_pliku, poziom_uprawnien_write)

plik1.write("linia4")
plik1.writelines("aha")

plik1.close()