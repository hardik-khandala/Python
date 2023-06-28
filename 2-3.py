import math

print("For quadratic equations ax^2+bx+c=0")
a = int(input("Enter value of A: "))
b = int(input("Enter value of B: "))
c = int(input("Enter value of C: "))

d = b**2-4*a*c

if d > 0:
    x1 = (-b + math.sqrt(d))/ (2 * a)
    x2 = (-b -math.sqrt(d))/ (2 * a)
    print ("The roots are",round(x1, 3),"and ",round(x2, 3))
else:
    print("Roots doesn't exits!!, It is an Imaginary")

