# (a) Method Overriding --

class Parent:
    def show(self):
        print("Parent show")
class Child(Parent):
    def show(self):
        print("Child class")

obj = Child()
obj.show()

# (b) Same function, different objects --

class Dog:
    def sound(self):
        print("Dog is barking")

class Cat:
    def sound(self):
        print("Meow")

for animals in (Dog() , Cat()):
    animals.sound()