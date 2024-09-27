
str1 = "Python's Progrmming"
str2 = 'Java"s Programming'
str3 = '''This C# Programming
         Language'''

print(str1)
print(str2)
print(str3)

print("----------------************* 3. Strings are equals ******************---------------")

#2 string have are equal

str5 = "Texas lone star state"
str6 = "Dallas Cowboys"

print(str5 ==str6)
print(str5 != str6)





print("-------------------********** 4.ITERATION OF STRING **************---------------------------")

for x in " Dallas Cowboys ":
    print(x)







print("-------------------********** check character exist in string **************---------------------------")

Mystring= "A friend in need is a friend in deed"
if "need" in Mystring:
    print("Yes! it is present in the string")
else:
    print("No! it is not present")









print("----------------------------***** 6 string methods  *************--------------------------------------------")
#1 capitalize
txt= "hello and welcome to python programming"
i =txt.capitalize()
print(i)

# 2 count
i= txt.count('welcome')
print(i)

#3 isnumeric
y= "675857859hhh"
i = txt.isnumeric()
print(i)

#4 startwith
txt= "hello and welcome to python programming"
i = txt.startswith("hello")
print(i)

#5 swapacse
txt= "hello and welcome to python programming"
i = txt.swapcase()
print(i)

#6 zfill
w= "59"
i = w.zfill(10)
print(i)

