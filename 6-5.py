def square(x):
    return x ** 2

def cube(x):
    return x ** 3

start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))

numbers = list(range(start_range, end_range + 1))

squared_numbers = list(map(square, numbers))
cubed_numbers = list(map(cube, numbers))

print(f"Original Numbers: {numbers}")
print(f"Squared Numbers: {squared_numbers}")
print(f"Cubed Numbers: {cubed_numbers}")
