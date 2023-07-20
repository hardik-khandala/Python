string_list = []

num_strings = int(input("Enter the number of strings you want to store: "))

for i in range(num_strings):
    string = input(f"Enter string {i+1}: ")
    string_list.append(string)

print("\nStrings stored in the list:")
print(string_list)