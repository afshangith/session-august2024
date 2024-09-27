#polymorphism (1- method over-riding and 2. method over loading)
# over-riding method

class Animal():

    def speak(self):
        print( "Animal is speaking........")


class Dog(Animal):

    def speak(self):
           print("Dog is barking.........")



class Cat(Animal):

    def speak(self):
            print("Cat is Meowing.........")

dog = Dog()
dog.speak()

cat = Cat()
cat.speak()















