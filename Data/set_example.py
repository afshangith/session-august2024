a = {10, 20, 30, 40, "Rahul", True, 100, 0.23, 24, 35}
b = {10}
print(a)
print(type(a))
print(type(b))

#print(a[3]) indexing cannot as order is not maintained

# iteration is not possible we can get the output but order is not maintained
'''for value in a:
    print(value)
'''
# we can convert a list into a set ask question we converted it but final should be set
a1 =[ 10, 20, 30, 30, 30, 40, 5.5, True, "Amjad"]
print(a1)
print(type(a1))
print(set(a1))
print(type(a1))

# to create a blank set we need to create an object
a2 = set()
a3 = {}
print(a2)
print(type(a3))
print(type(a2))

a2.add(20)
a2.add(40)
a2.add("Diya")
a2.add(6.9)
print(a2)
# update a value
a2.update([10 , 30])
print(a2)


# to remove a value from a set (only the difference is discard doesn't give the error message if the value is not present
# unlike the remove method)

a2.discard(40)
print(a2)

a2.remove(20)
print(a2)







print("--------------------------****** 4 iterate a set *****------------------------------")
Myset = { "preeti", "diya ", "radhika" , "sharmeen"}
for i in Myset:
    print(i)














print("--------------------------****** item exist in  a set *****------------------------------")
Myset = { "preeti", "diya ", "radhika" , "sharmeen"}
if "asad " in Myset:
    print("yes! 'asad' is present ")
else:
    print(" Item not present")
