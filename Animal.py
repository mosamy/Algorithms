__author__ = 'mosamy'
class Animal(object):
    """Makes cute animals."""
    is_alive = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Add your method here!
    def description():
        print self.name
        print self.age

hippo = Animal("Mido", 3)
hippo.description()
