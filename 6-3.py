from functools import reduce

def find_max(x, y):
    return x if x > y else y

numbers = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]

max_value = reduce(find_max, numbers)

print(f"The maximum value in the list is: {max_value}")
