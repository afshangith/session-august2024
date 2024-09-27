class A:

    __count = 0

    def __init__(self):
         A.__count= A.__count + 1;

    def display(self):
         print(self.__count)

class B(A):

    def displayB(self):
        print(self.__count)

b = B()
b.displayB()

a = A()
a.display()

a1 = A()
a1.display()

a3 = A()
a3.display()