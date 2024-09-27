def get_even_numbers(numbers):
    even_numbers =[]
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers

def get_odd_numbers(numbers):
    odd_numbers =[]
    for number in numbers:
        if number % 2 != 0:
            odd_numbers.append(number)
    return odd_numbers

numbers = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
#even_numbers = get_even_numbers(numbers)
#print(even_numbers)
print(get_even_numbers(numbers))

#odd_numbers = get_odd_numbers(numbers)
#print(odd_numbers)
print(get_odd_numbers(numbers))



