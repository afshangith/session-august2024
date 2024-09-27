from oops.A import A


class B(A):

    def printB(self):
        print("B Child Class Method printed")

b = B()
b.printB()
b.printA()





