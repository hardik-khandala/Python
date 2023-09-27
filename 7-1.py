with open('example.txt', 'r') as file:
    content = file.read()
print("Using read() method:")
print(content)

with open('example.txt', 'r') as file:
    lines = file.readlines()
print("\nUsing readlines() method:")
for line in lines:
    print(line.strip())

with open('example.txt', 'r') as file:
    print("\nUsing readline() method:")
    while True:
        line = file.readline()
        if not line:
            break 
        print(line.strip()) 
