from abc import ABC , abstractmethod

class vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

class Car(vehicle):
    def start(self):
        print("Car start with key")

class Bike(vehicle):
    def start(self):
        print("Bike start with self")
    
obj = Car()
obj.start()
