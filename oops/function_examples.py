
def get_square(item_list):
   square = []
   for value in item_list:
    square.append(value ** 2)
   return square


list = [10, 20, 30, 40, 50]
a = get_square(list)
print(a)

list1 =[ 2, 4, 6, 8, 10]
print(get_square(list1))


list2 = [ 12, 14, 16, 18, 20]
print(get_square(list2))
