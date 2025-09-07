# Function that uses polymorphism
def process_sound(sound_object):
    print(sound_object.make_sound())

# Class 1: Dog
class Dog:
    def make_sound(self):
        return "Woof! Woof!"

# Class 2: Cat
class Cat:
    def make_sound(self):
        return "Meow! Meow!"
