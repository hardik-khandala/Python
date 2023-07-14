n = int(input("Enter a number: "))

num = str(n)
num1 = num[::-1]
num2 = int(num1)

if n == num2:
    print(f"{n} is a palindrome number")
else:
    print(f"{n} is not a palindrome number")
