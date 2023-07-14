n = int(input("Enter a number: "))

print("First Output")
for i in range(1, n+1):
    for j  in range(1, i+1):
        print(j, end=" ")
    print()

print()
print("Second Output")
for i in range(1, n+1):
    for j in range(1, n-i+2):
        print("*", end=" ")
    print()