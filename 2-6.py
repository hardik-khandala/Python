degree = input("Enter degree(B.E. or M.E.): ")
exp = int(input("Enter Experience: "))

if (degree == "B.E") :
    if (exp < 5) :
        salary = 30000
    else :
        salary = 40000
else :
    if (exp < 5) :
        salary = 50000
    else :
        salary = 60000

print("Employees salary is", salary)