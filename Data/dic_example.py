a = {}
b = {1:20, 2:35, 3:45, "A":"Ramesh", 2:50, 2:76, 3:45}
c = {3:34, 9:88}
# for line 7 the duplicate key -takes the last recent added value
print(type(a))
print(type(b))
print(b["A"])
print(b[2])
print(b[3])

#updating using key[if the key is present it update it or else it add the new key
b[1] = "Huma"
b[5] = "Asad"
print(b)

# delation by the key number
del b[1]
print(b)
b.pop(5)
print(b)

c.clear()
print(c)








print("-----------------------------------********* iterate a dictionary *************---------------------------------")
# for iteration
b = { 1 :20, 2: 76, 3: 45, 'A': 'Ramesh'}
for key, value in b.items():
    (print(key, value))







