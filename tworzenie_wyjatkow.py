imie = "ble"

try:
    if imie.endswith("a"):
        raise ValueError("Błąd_imie_zenskie")
        print("Imię żeńskie")
    else:
        print("męskie")

except ValueError as e:
    print("Custom ValueError", e)