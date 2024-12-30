class intro:  
    def __init__(self, x, y):  
        self.x = x  
        self.y = y   
    
    def add(self):  
        print("Addition result is", self.x + self.y)
 
obj1=intro(10,20)
obj1.add()