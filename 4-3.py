def is_palindrome(lst):
    length = len(lst)

    for i in range(length // 2):
        if lst[i] != lst[length - 1 - i]:
            return False

    return True

list1 = [1, 2, 3, 2, 1]
list2 = [1, 2, 3, 4, 5]

if is_palindrome(list1):
    print("list1 is a palindrome.")
else:
    print("list1 is not a palindrome.")

if is_palindrome(list2):
    print("list2 is a palindrome.")
else:
    print("list2 is not a palindrome.")