a= 10, 20, 30, 40, True, False
b=()
c= "Ravi"
c1= "Ravi",
c2= ("Ravi",)


print(type(c2))
print(type(a))
print(type(b))
print(type(c))
print(type(c1))
print(a[5])

#updating by index
#a[2] =  100    cannot failed error,cannot add, cannot delete, not even append (immutable)
print(a)
#del a[2] error doesnt support item deletion
print(a)
#a.append(200)-error


print("------------------******* interation ***********___________________________________")
for value in a:
    print(value)

# slicing method works very well list array and list


print(10 in a)
print (100 in a)
print(a)







print("--------------------******** 3. check 2 tuples *************-----------------------------------")

tuple1 = ( 36, 44, 89, 7868, 333, 90)
tuple2 = ( 567, 897, 22, 67, 334, 777, 9.8)
print(tuple1 == tuple2)
print(tuple1 > tuple2)
print(tuple1 < tuple2)








print("--------------------******** iterate tuples *************-----------------------------------")
tuple1 = ( 36, 44, 89, 7868, 333, 90)
for i in tuple1:
    print(i)













print("--------------------******** check item exist in tuples*************-----------------------------------")

tuple1 = ( 36, 44, 89, 7868, 333, 90)
if 87 in tuple1:
    print("yes! the item is present")
else:
    print("Item is not present")


