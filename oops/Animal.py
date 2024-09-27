class Animal:

    def run(self):
        print("Animal is Running.......")

    def eat(self):
        print("Animal is Eating.......")


  # when we are creating classes we nee dto give two lines
class Cat(Animal):

    def meow(self):
        print(" meow.......")



class Dog(Animal):

    def bark(self):
        print("bark............")

dog = Dog()
dog.eat()
dog.run()
dog.bark()

cat = Cat()
cat.eat()
cat.run()
cat.meow()




