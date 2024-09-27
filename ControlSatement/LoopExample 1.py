'''
a = [10, 20, 30, 40, 50, 60, 70]

sum = 0
square = []

for value in a:
    sum +=value
   #print(value)
print(sum)

for value in a:
    sq = value ** 2
    square.append(sq)
print(square)
'''

str = "This  is  python  programming"

count1 = 0
count2 = 0
i = 1
for ch in str:
    print(ch)
    if ch =='a' or ch == 'e' or  ch =='i' or ch =='o' or ch =='u':
      if ch == 'i':
          continue
          count1 += 1

    else:
      count2 +=1
      if ch == 'h':
          break
print("Total number count1 :",count1)
print("Total number count2 :",count2)

'''''
print(range(5))
print(list(range(5)))
print(list(range(3,4)))
print(list(range(2,100,4)))

for i in range(1,11):
    print(2 * i)
 '''''''
'''
#count = 0

#while count < 10:
   # print(count)
   # count +=3
#else:
   # print("Loop execution completed")


