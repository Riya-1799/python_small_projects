class animal:
    def __init__(self, habitat):
        self.habitat = habitat

    def display_habit(self):
        print(self.habitat)

    def display_sound(self):
        print("some animal sounds")

class dog(animal):
    def __init__(self):
        super().__init__("Kennel")
    def sound(self):
        print("whooo whooooooooooo")

d = dog()
d.display_habit()
d.sound()
d.display_sound()

a = animal("habit")
a.display_sound()
a.display_habit()