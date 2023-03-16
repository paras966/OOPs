class Student:
    def __init__(self,name,rn):
        self.name=name
        self.rn=rn

s1=Student("paras",1)
s2=Student("Praveen",2)
print(s1.__dict__)
print(s2.__dict__)