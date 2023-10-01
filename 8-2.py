try:
    num = int(input("Enter a number: "))
    result = 10 / num

except ValueError:
    print("Invalid input! Please enter a valid number.")

except ZeroDivisionError:
    print("Error: Division by zero!")

else:
    print("Division result:", result)

finally:
    print("This will always be executed, regardless of exceptions.")
