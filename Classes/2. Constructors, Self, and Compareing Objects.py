"""
New section starts, creating variables in objects
"""
#init = Instance variables
#if we decalare varianles outslide init function it is a default variable and known as class variables

class car:
    
    Wheels = 4
    def __init__(self):
        self.mil = 10
        self.com = "BMW"

c1 = car()
c2 = car()
print(c1.com,c1.mil)
print(c2.com,c2.mil)

c1.mil = 8
c2.mil = 12

print(c1.com,c1.mil, c1.Wheels)
print(c2.com,c2.mil, c2.Wheels)

car.Wheels = 5
print(c1.com,c1.mil, c1.Wheels)

# Class variables done!!