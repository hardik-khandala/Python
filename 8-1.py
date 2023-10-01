try:
    user_input = float(input("Enter a number: "))
    
    if user_input < 0:
        raise ValueError("Entered value is less than zero")
    
    print("You entered:", user_input)
    
except ValueError as e:
    print("Error:", e)
