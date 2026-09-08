standard = 10
standardf = 10.2
standardc = "Tekst"
suma = standard + standardf
print(suma)
print(f"Suma to {suma}")

print(10 == 10.0) #porównanie typu
print(standard == standardf) # True

# sprawdź typ zmiennej
print(type(standard))

# sprawdź typ drugiej zmiennej
print(type(standardf))
print(type(standardc))

# <class 'int'>
# <class 'float'>
# <class 'str'>

suma1 = standard + standardc
print(suma1) # błąd, nie można dodać int i str