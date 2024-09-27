

def get_cube(item_list):
 cube = []
 for value in item_list:
    cube.append(value*value*value)

 return cube



list = [10, 20, 30, 40, 50]
a = get_cube(list)
print(a)

list1 =[ 2, 4, 6, 8, 10]
print(get_cube(list1))

list2 = [ 12, 14, 16, 18, 20]
print(get_cube(list2))
