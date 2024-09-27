def fun(n1, n2 = 30, n3 = 40):
    print("First number :", n1)
    print("Second number :", n2)
    print("Third number :", n3)


#required arguments
fun(20 )
fun(35 , 49)
fun(n1=200, n3=100)

def fun1(*arg_list):
    for i in arg_list:
        print(i)

fun1("Apple", "Oranges", "Banana", 10,  20,  40)





