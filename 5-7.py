my_tuple = (1, 2, 3, 4, 5)

if 3 in my_tuple and 4 in my_tuple:
  print("Both 3 and 4 are present in the tuple.")

for item in my_tuple:
  if item in (3, 4):
    print(item)
