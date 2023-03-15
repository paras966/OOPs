class Student:

    passingpercent=40
    def studentDetails(self):
        self.name="paras"
        self.percent = 90
        print(self.name , "  ", self.percent)
    
    def isPassed(self):
        if self.percent>Student.passingpercent:
            print("passed")
        else:
            print("Failed")
    
s1=Student()
s1.studentDetails()
s1.isPassed()