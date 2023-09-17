my_set = {2, 3, 4, 5, 6}
print(my_set)

my_set1 = set()
my_set1.add(1)
my_set1.add(2)
my_set1.add(3)
my_set1.add(4)
my_set1.add(5)
print(my_set1)

my_list = [1, 2, 3, 4, 5]
my_set2 = set(my_list)
print(my_set2)

my_set3 = {1, 2, 3, 4, 5}
my_set4 = set(my_set3)

my_set5 = set(range(6, 10))
print(my_set5)

my_set6 = {1, 2, 3, 4, 5}
my_set7 = {6, 7, 8, 9, 10}
my_set6.update(my_set7)
print(my_set6)

my_set8 = {1, 2, 3, 4, 5}
for i in my_set8:
  print(i)

my_set = {1, 2, 3, 4, 5}
my_set.remove(3)
print(my_set)

my_set.discard(4)
print(my_set)