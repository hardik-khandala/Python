def is_palindrome(list):
    reverse = list[::-1]
    if reverse == list:
        return True
    else:
        return False
    
list1 = [1,2,3,2,1]
if is_palindrome(list1):
    print("list1 is a palindrome.")
else:
    print("list1 is not a palindrome.")