#return object of the class
from datetime import date
class Student:
    def __init__(self,name,age=10,percent=40):
        self.name=name
        self.age=age
        self.percent=percent

    @classmethod
    def fromBirthYear(cls,name,year,percent):
        return cls(name,date.today().year - year,percent)
    
s1=Student.fromBirthYear("paras",2001,80)
print(s1.name,' ', s1.age,' ',s1.percent)