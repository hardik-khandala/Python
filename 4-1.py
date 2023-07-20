list = [1, 2, 3, 4, 5, 22]

list.append(22)
print("After append: ", list)

list.insert(2, 12)
print("After insert: ", list)

list.remove(2)
print("After remove: ", list)

popped_element = list.pop(4)
print("After pop: ", list)
print("Popped element: ", popped_element)

index_of_4 = list.index(4)
print("Index of 4: ", index_of_4)

count_of_10 = list.count(22)
print("Count of 22: ", count_of_10)

list.reverse()
print("After reverse(): ", list)

list.sort()
print("After sort(): ", list)

another_list = [7, 8, 9]
list.extend(another_list)
print("After extend(another_list): ", list)

copied_list = list.copy()
print("Copied list: ", copied_list)

list.clear()
print("After clear(): ", list)
