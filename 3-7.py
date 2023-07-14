n = int(input("Enter a number: "))

print(f"Even number between 1 to {n} except the numbers divisible by 6.")

for i in range(1, n+1):
    if i%2==0:
        if i%6==0:
            pass
        else:
            print(i)