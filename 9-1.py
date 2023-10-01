class KSV:
    cnt = 0 
    
    def __init__(self, x, y):
        self.x = x  
        self.y = y  
        KSV.cnt += 1 
    
    def get_value(self):
        return self.x, self.y  
    
    def print_value(self):
        print(f'x = {self.x}, y = {self.y}')  

obj1 = KSV(5, 10)
obj2 = KSV(7, 14)

print("Instance 1 values:", obj1.get_value())
print("Instance 2 values:", obj2.get_value())

obj1.print_value()
obj2.print_value()

print("Total instances created:", KSV.cnt)
