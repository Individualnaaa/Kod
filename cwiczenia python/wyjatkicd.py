#przykład wyciągniecia blędu

x = 10

#rozszerzenie

try:
    print("Wynik dzielenia", 10/x)
except ZeroDivisionError:
    print("Nie można dzielić przez 0")
except Exception as error_message:
    print("Moja custom wiadomość", error_message) #gdy zmienimy x na np. nazwę
else:
    print("Jednak umiesz dzielić")
finally:
    print("Finally wykona się zawsze")
