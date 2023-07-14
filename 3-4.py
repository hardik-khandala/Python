n = int(input("Enter a number: "))

n0, n1 = 0 , 1
temp = 0

print("Fibonacci Series: ")
while temp <= n:
    print(temp)
    n0 = n1
    n1 = temp
    temp = n0 + n1
