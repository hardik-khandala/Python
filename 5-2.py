set_a = {1, 2, 3, 4, 5}
set_b = {3, 4, 5, 6, 7}

difference_method = set_a.difference(set_b)
difference_operator = set_a - set_b

intersection_method = set_a.intersection(set_b)
intersection_operator = set_a & set_b

union_method = set_a.union(set_b)
union_operator = set_a | set_b

symmetric_difference_method = set_a.symmetric_difference(set_b)
symmetric_difference_operator = set_a ^ set_b

is_subset = set_a.issubset(set_b)
is_superset = set_a.issuperset(set_b)

print("Set A:", set_a)
print("Set B:", set_b)
print("Difference (Method):", difference_method)
print("Difference (Operator):", difference_operator)
print("Intersection (Method):", intersection_method)
print("Intersection (Operator):", intersection_operator)
print("Union (Method):", union_method)
print("Union (Operator):", union_operator)
print("Symmetric Difference (Method):", symmetric_difference_method)
print("Symmetric Difference (Operator):", symmetric_difference_operator)
print("Is Set A a Subset of Set B:", is_subset)
print("Is Set A a Superset of Set B:", is_superset)