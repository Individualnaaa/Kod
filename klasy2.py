""" zestaw lego """

class LegoSet:
    def __init__(self, name, pieces_count, price):
        self.name = name 
        self.pieces_count = pieces_count
        self.price = price

def advertise(self):
    print(f"""Produkt: {self.name}!
    Ilość elementów: {self.pieces_count}
    Cena: {self.price} PLN
    """)

lego_barbie = LegoSet("Barbie", "10", "100")
print("Cena", lego_barbie.price)
    
# coś tu nie działa



