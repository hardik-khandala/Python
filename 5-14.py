def check_if_all_dicts_empty(list_of_dicts):
  for dict in list_of_dicts:
    if dict:
      return False
  return True

list_of_dicts = [{}, {}, {}]
is_all_dicts_empty = check_if_all_dicts_empty(list_of_dicts)
print(is_all_dicts_empty)
