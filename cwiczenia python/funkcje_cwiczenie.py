def przywitanie(imie, liczba=3):
    for _ in range(liczba):
        print(f"cześć {imie}")
        if imie == "Czarek":
            break

              
przywitanie("Adam", 2)
przywitanie("Bartek", 4)
przywitanie("Czarek")

