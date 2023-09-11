def flatten(list1):
  flat_list = []
  for element in list1:
    if isinstance(element, list):
      flat_list.extend(flatten(element))
    else:
      flat_list.append(element)
  return flat_list

list1 = [1, [2, 3], [4, 5, [6, 7] ] ]
print(flatten(list1))

