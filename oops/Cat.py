from oops.Animal import Animal
from oops.Dog import Dog


class Cat(Animal):

    def meow(self):
        print(" meow.......")



dog = Dog()
dog.eat()
dog.run()
dog.bark()

cat = Cat()
cat.eat()
cat.run()
cat.meow()

