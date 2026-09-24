# def pitagoras(a, b):
#     return((a * a) + (b * b)) ** 0.5

# {}.filter(pitagoras(2, 3))

# funkcja jednorazowa
# {}.filter(lambda a, b: ((a * a) + (b * b)) ** 0.5)


# x = [element**2 for element in range (1,6) if element % 2 == 0]
# print(x)


import ctypes
s1 = "ABC"
print(id(s1))
mojeid = 2200737229696
obiekt = ctypes.cast(mojeid, ctypes.py_object).value
print(obiekt)
