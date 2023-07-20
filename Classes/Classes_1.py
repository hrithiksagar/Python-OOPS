class computer:
    def __init__(self):
        self.name = "Hrithik"
        self.age = "23"

c1 = computer()
print(id(c1)) # address of the memory 
c2 = computer()
print(id(c2)) # address, constructor manages this address

print(c1.name)
print(c2.name)

c1.name = "Allu Arjun"
c1.age = 10
print(c1.name)
print(c1.age)

class computer:
    def __init__(self):
        self.name = "Hrithik"
        self.age = "23"
    def update(self):
        self.age = 30
    def compare(self, c2):
        if self.age == c2.age:
            return True
        else:
            return False
c1 = computer()
c2 = computer()
c1.age = 40
if c1.compare(c2):
    print("same")
else:
    print("Diff")
    
"""
Ended this section
New section starts, creating variables in objects
"""
# Class variables done!!
# new video



