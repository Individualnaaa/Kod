t = "testerabcd123456"

# jaki jest długi ciąg znaków?
# t - 6
# e - 
# s - 
# t -
# e -   
# r - 

print(len(t)) # długość ciągu znaków
print(t[0]) # pierwszy znak
print(t[1]) # drugi znak

print(t[5]) # ostatni znak
print(t[-1]) # ostatni znak - wtedy unikamy sytuacji ze zmiana

# wycinek
print(t[0:5]) # od 0 do 5 nie włącznie
# prawidłowo
print(t[0:6]) # od 0 do 6 nie włącznie

# co drugi znak
print(t[::2]) # co drugi znak
print(t[0:-1:2]) # co drugi znak od końca

z = "mars"
print(z[::-1])

print(len("element")) # długość ciągu znaków
print(len(z)) # długość ciągu znaków
print(len("123"))
# print(len(123)) # błąd, nie można policzyć długości liczby
print(len(str(123))) # długość liczby po konwersji na string