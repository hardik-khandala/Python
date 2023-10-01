class MyNumber:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        if isinstance(other, MyNumber):
            return MyNumber(self.value + other.value)
        else:
            raise TypeError("Unsupported operand type for +")

    def __str__(self):
        return str(self.value)

num1 = MyNumber(5)
num2 = MyNumber(10)

result = num1 + num2
print(f"Result of num1 + num2: {result}")

result2 = result + MyNumber(7)
print(f"Result of result + MyNumber(7): {result2}")
