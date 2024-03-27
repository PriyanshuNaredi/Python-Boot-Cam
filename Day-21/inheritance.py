

class Animal():
    
    def __init__(self):
        self.num_eyes = 2
        
    def breath(self):
        print("Inhale, Exhale")
        
class Fish(Animal):
    
    def __init__(self):
        super().__init__()
        
    def breath(self):
        super().breath()
        print("breathing under water")
    
    def swim(self):
        print("swimming")
        
nemo = Fish()
nemo.swim()
nemo.breath()
print(nemo.num_eyes)