from abc import ABC, abstractmethod


class Car(ABC):
     @abstractmethod
     def milage(self):
         pass

class Tesla(Car):


    def milage(self):
        print("Milage of Tesla car is 30km ")

class Suzuki:
    def milage(self):
        print("Milage of Suzuki car is 20km ")

class Infinity:
    def milage(self):
        print("Milage of Infinity car is 25km ")


t = Tesla()
t.milage();


s = Suzuki()
s.milage();

i = Infinity()
i.milage();




