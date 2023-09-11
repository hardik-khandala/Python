def split_list(list1, n):
  sublists = []
  i = 0
  while i < len(list1):
    sublist = []
    for j in range(n):
      if i < len(list1):
        sublist.append(list1[i])
      i += 1
    sublists.append(sublist)
  return sublists

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(split_list(list1, 2))
