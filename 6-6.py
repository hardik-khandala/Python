#map/filter and function
def cube(x):
    return x * x * x

list1 = [1, 2, 3, 4, 5]
list2 = list(map(cube, list1))
print(list2)

def fahrenheit_to_celsius(f):
    return (5 / 9) * (f - 32)

list1 = [32, 50, 70, 90, 110]
list2 = list(map(fahrenheit_to_celsius, list1))
print(list2)

def is_positive(x):
    return x > 0

list1 = [-1, 0, 1, 2, -3, 4, -5]
list2 = list(filter(is_positive, list1))
print(list2)

import string
def is_alphabet(x):
    return x in string.ascii_letters

list1 = ['a', 'b', '1', '2', 'c', 'd', '3', '4']
list2 = list(filter(is_alphabet, list1))
print(list2)


#map/filter and lambda
list1 = [1, 2, 3, 4, 5]
list2 = list(map(lambda x: x * x * x, list1))
print(list2)

list2 = list(map(lambda f: (5 / 9) * (f - 32), list1))
print(list2)

list1 = [-1, 0, 1, 2, -3, 4, -5]
list2 = list(filter(lambda x: x > 0, list1))
print(list2)

import string
list1 = ['a', 'b', '1', '2', 'c', 'd', '3', '4']
list2 = list(filter(lambda x: x in string.ascii_letters, list1))
print(list2)


#list comprehension
list1 = [1, 2, 3, 4, 5]
list2 = [x * x * x for x in list1]
print(list2)

list2 = [(5 / 9) * (f - 32) for f in list1]
print(list2)

list1 = [-1, 0, 1, 2, -3, 4, -5]
list2 = [x for x in list1 if x > 0]
print(list2)


import string
list1 = ['a', 'b', '1', '2', 'c', 'd', '3', '4']
list2 = [x for x in list1 if x in string.ascii_letters]
print(list2)