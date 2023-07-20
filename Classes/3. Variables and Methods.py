class student:
    school = "Hrithik's School"
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    def avg(self):
        return((self.m1+self.m2+self.m3)/3)
    
    
    @classmethod # this is known as decorator, if we want to use info as class method we need to wirte this @classmethod, thats how we define it
    def getSchool(cls):
        return cls.school
    
    #Static Method
    @staticmethod
    def info(): # not related to obj and class, so dont keep any parameters keep it blank. 
        print("This is student Class... in abc Module")
    
    
    
s1 = student(34,33,47)
s2 = student(56,67,68)

print(s1.avg())
print(s2.avg())
print(student.getSchool())
student.info()

