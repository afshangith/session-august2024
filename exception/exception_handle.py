
print("testing exception")

a = 10
b = 2
name = [10]
name1 = "testing"
try:
     print(len(name1))
     result = a/b
     print(result)
     print(name[0])
except ZeroDivisionError :
     print("ZeroDivisionError Handler")
except IndexError :
     print("IndexError Handler")
except:
    print("handle all exceptions")
else:
    print("Nothing went wrong")
finally:
     print("finally always execute")
print("done")


x = -1

if x < 0:
    raise Exception("Sorry, no numbers below zero")















