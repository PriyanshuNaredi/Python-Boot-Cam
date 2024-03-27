
def add(*args):
    print(type(args))
    sum = 0
    for i in args:
        sum += i
    return sum
        
print(add(1,2,3))

def calculate(n,**kwargs):
    # print(type(kwargs))
    # print(kwargs)
    # for key,value in kwargs.items():
    #     print(f"{key}:{value}")
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)
    
    
calculate(2,add=3,multiply =5)


class Car:
    def __init__(self, **kw) :
        # self.make = kw["make"]
        # self.model = kw["model"]
        self.make = kw.get("make")
        self.model = kw.get("model")
        
my_car = Car(make="Nissan")
print(my_car.model)