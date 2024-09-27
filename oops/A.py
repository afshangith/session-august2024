class A:

    def printA(self):
        print("Parent A class method")


    @staticmethod
    def staticMeth():
        print("Static Method")


a=A()
a.printA()

A.staticMeth()