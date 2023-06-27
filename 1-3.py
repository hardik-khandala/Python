a = int(input("Enter First Value: "))
b = int(input("Enter Second value: "))

print("Value of A and B before swap is", a,"and", b)

a = a + b
b = a - b
a = a - b

print("Value of A and B After swap is", a,"and", b)