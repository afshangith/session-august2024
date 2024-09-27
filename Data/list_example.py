a =[10, 20, 30, True , False, "Raj","Rahul", "Alice"]
b =[20, 10, 30, True , False, "Raj","Rahul", "Alice"]
'''
print(type(a))
print(a)
print(a[1])

b =[20, 10, 30, True , False, "Raj","Rahul", "Alice"]
print(a==b)

a[2] = "None"
print(a)
'''
# Slicing
'''
print(a[1:4])
print(a[:])
print(a[1:7:2])

print(a[-2])
print(b[-6:-1])
print(a[-4:-2])
'''
a[0] = "Celina"
print(a)
a[1:4] =[65, 75]
print(a)
a[-5] = "Brenda"
#del a
#del a[0]
#del a[-1:-3]
print(a)

# repeat
#l = a * 2
#print(l)

#update a list
a1 =[12, 14, 16]
a2 =["Monday", "Tuesday","Wednesday"]
l1 = a1 + a2
print(l1)
print(len(l1))

#iterate a list
for a in l1:
    print(a)

#checking a value in a list
print(10 in l1)
print('Monday'in l1)

# append a list- add a list
l1.append("Scott")
print(l1)

#remove a value
print(l1)
l1.remove(16)
print(l1)


# to get max value in a array-should be number -integer
print(max(a1))

r= [78, 98, 1003, 9 , 193, 200]
print(r)
print(max(r))
print(min(r))










print("-----------------------******* 3 check 2 list***********---------------------------------------------")

q = [ 27, 78, 90, 0.9, 867, 8]
u = [ 678, 87, 345, 877, 22, 22, 34,68]
if  q == u:
    print("list are equal")
else:
    print("list are not equal")

















print("----------------------------***** 4 iterate list********--------------------------------------------------")
listA= [ 2, 3, 89, 76 ]
for i in listA:
    print(i)














print("-----------------------------------***** check item in a list *************-----------------------------")
u = [ 678, 87, 345, 877, 22, 22, 34,68]
i= 345
if i in u:
    print("exist")
else:
    print("not exist")










print("----------------------*****how to create a nested list and iterate using loop *************------------")

sub =[[i for i in range(3)] for j in range(5)]
print (sub)



