class Vehical:
    def __init__(self,color, maxSpeed):
        self.color=color
        self.__maxSpeed=maxSpeed

    def getMaxSpeed(self):
        return self.__maxSpeed
    
    def setMaxSpeed(self,newSpeed):
        self.__maxSpeed=newSpeed

    def print(self):
        print(self.color)
        print(self.__maxSpeed)

class Car(Vehical):
    def __init__(self, color, maxSpeed, numGears, isConvertable):
        super().__init__(color, maxSpeed)
        self.numGears=numGears
        self.isConvertable=isConvertable

    # METHOD OVERRIDING
    
    def print(self):
        super().print()
        print(self.numGears)
        print(self.isConvertable)

obj = Car("red",140,5,True)
obj.print()