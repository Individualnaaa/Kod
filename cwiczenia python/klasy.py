class Cat:
    pawcount = 4

    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def introduce(self):
        print(f"I am {self.name}")

    def speak(self):
        print("Meow" + self.name)

garfiels = Cat("Garfield", 3, "orange")
garfield.speak()

print("wiek garfielda to: ", garfield.age)
garfield.age = 40

print("wiek garfielda to teraz ", garfield.age)

print(garfield.add(1, 5))