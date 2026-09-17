import math
# sami

def pierwiatek(liczba):
    return liczba ** (1/2)

print("nasz", pierwiatek(100))


# żeby użyć funkcji:

print(math.sqrt(16))

# lepszy spoosób

from math import sqrt
print(sqrt(100))

# kolejna podobna rzecz- jesli nazwa funkcji brzydka

from math import sqrt as pierwiastek 
print(pierwiatek(16))

from math import *

from math import sqrt, tan, pow
print(pow(2, 3))
print(tan(45))

