nazwa_pliku = "plik1.txt"
poziom_uprawnien_append = "a"
plik1 = open(nazwa_pliku, poziom_uprawnien_append)

plik1.write("\ndodatek")
plik1.close()