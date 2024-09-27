# +,-,/, *, %,(modula operator) // ()
'''
a = 10
b = 2

print(a+b)
print(a-b)
print(a*b)
print(a%b)

a = 13
print(a/b)#gives answer in decimal
print(a%b)#(gives only remainder)


a = 20
b = 3
print(a//b)#gives answer without reminder
'''
#comparision -operators(ans: True or False)1. ==(double equal),2. !=(not equal),3.<,4.>, 5.>=,6.<=
'''
a = 4
b = 24
print(a != b)
print(a == b)
print(a<b)
print(a>b)
print(a>=b)
print(a<=b)
'''
# Assignment operator ----[= ,+= ,-= ,*= , /= , %= , //=]

#a = 10
'''
a += 20 #a= a + 20
a -= 5 #a= a - 5
a *= 5 # a= a * 5
a /=5# a= a / 5
a %=3# a= a % 3
a //=4 # a= a // 4
print(a)
'''
# bitwise operator- |-or(pipe), &(and)
'''
a = 10
b = 20
c = 30
print(a<b & b<c) # True and True = True
print(a>b & b<c) #false and  True = False
print(a>b & b>c) #false and  False = False

print(a<b | b<c) # True or True = True
print(a<b | b<c) #True or True = True
print(a>b | b<c)  #fasle or True = False
'''

# logical operator  and, or, not
'''''
a = 10
b = 20
c = 30
''
and
print(a > b and b > c) # False and False = False
print(a < b and b > c) # True and False = False
print(a < b and b < c) # True and True = True
print(a < b and b > c) # True and False = False

or
print(a > b or  b > c) # False and False = False
print(a < b or b > c) # True and False = True
print(a < b or b < c) # True and True = True
print(a < b or b > c) # True and False = True
'''
'''
not -opposite of or 
print(not(a > b or  b > c)) # False and False =not False= True
print(not(a < b or b > c)) # True and False = not True= False
print(not(a < b or b < c))# True and True =not True= False
print(not(a < b or b > c)) # True and False =not True= False
'''

''''
# membership operator 2 types in and not-both gives true or false answer
x = [1,2,3,4,5]
y = ["One", "Two","Three"]
print(5 in x)# True
print("one" in y)#one o is lower case -false
print("One" in y)#true
'''
#name = "Afshan Nureen"
#print('K' in name)


# identity Operator ---is ,is not
'''''
a = 10
b = 10
print(a is b)# True
print(a is not b)# false
'''



