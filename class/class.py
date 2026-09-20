
class Animal:
    def __init__(self, name):
        self.name = name

    def sleep(self):
        print(f"{self.name} is sleeping")


class Dog(Animal):
    def braking(self):
        print(f"{self.name} is barking")


germanSheferd = Dog(name="tommy")

germanSheferd.name
germanSheferd.braking()
germanSheferd.sleep()



        