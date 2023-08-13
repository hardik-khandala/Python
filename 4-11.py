lst=[]
n=int(input("Enter the number of values upto you want to add element into element: "))
for i in range (n):
    lst.append(int(input("enter: ")))

print("List With Duplicacy",lst)
mySet=set(lst)
print("List Without Duplicacy",lst1:=list(mySet)) #directly declaring using walrus operator

