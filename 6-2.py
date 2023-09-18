from functools import reduce

def add(x, y):
    return x + y

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

numbers = list(range(start, end + 1))
sum_of_range = reduce(add, numbers)

print(f"The sum of the range from {start} to {end} is: {sum_of_range}")
