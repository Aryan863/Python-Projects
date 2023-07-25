class Animal:

    def __init__(self):
        self.eyes = 2
    
    def breathe(self):
        print("inhale and exhale")


class Dog(Animal):

    def __init__(self):
        super().__init__()
        self.nose = "brown"

    def breathe(self):
        super().breathe()
        print("fast breathing")


dog = Dog()
print(dog.eyes)
print(dog.nose)
dog.breathe()