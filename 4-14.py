def remove_even_numbers(list1):
  new_list = []
  for number in list1:
    if number % 2 == 1:
      new_list.append(number)
  return new_list

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(remove_even_numbers(list1))