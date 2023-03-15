class Student:
    pass

s1 = Student()
s2=Student()
s1.name="paras"
s2.rn=123
print(s1.__dict__)
print(s2.__dict__)
print(hasattr(s1,"rn"))