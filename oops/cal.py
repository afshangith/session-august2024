class Calculation1():

    def mul(self, a, b):
        return a * b;


class Display():

    def display(self, value):
        print(value)


class Divide(Calculation1 , Display):

    def divide(self, a, b):
        return  a/b

d = Divide()
result = d.divide(20, 5)
d.display(result)

result1 = d. mul(20, 5)
d.display(result1)











