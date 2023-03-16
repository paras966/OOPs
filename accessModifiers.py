class Student:

    # Private variable can not be used outside the class
    # In python the protected variable used generally in concept of inheritence where it gives sense to the developer that the variable should not be modified and used as minimum as possible
    passingpercent=40
    def studentDetails(self):
        self.__name="paras"
        self._percent = 90
        print(self.__name , "  ", self._percent)
    
    def isPassed(self):
        if self._percent>Student.passingpercent:
            print("passed")
        else:
            print("Failed")
    
s1=Student()
s1.studentDetails()
s1.isPassed()