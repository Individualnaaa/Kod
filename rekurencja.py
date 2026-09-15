def suma_rekurencja(number):
    if number == 1:
        return 1
    return number * suma_rekurencja(number - 1)

print(f"Suma zapomocą rekrurencji: {suma_rekurencja(3)}")


# return == 1 dla jedynki - żeby skonczyła się funkcja w tym miejscu
# a nie szła do nieskończoności