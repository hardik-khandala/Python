n = int(input("Enter the value of Total Number: "))
sum = 0

for i in range(n):
    num = int(input("Enter a number: "))
    sum = sum + num

print(f"The sum of {n} scanned numbers is {sum}")