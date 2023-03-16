import math

class Point:
    def __init__(self,x,y) -> None:
        self.__x = x
        self.__y = y
    
    def __str__(self) -> str:
        return "Point is " + str(self.__x)+","+str(self.__y)

    def __add__(self,obj):
        return Point(self.__x+obj.__x, self.__y+obj.__y)
    
    def __lt__(self,obj):
        return math.sqrt(self.__x**2+self.__y**2)  <  math.sqrt(obj.__x**2+obj.__y**2)
    
p1=Point(1,2)
p2=Point(2,3)
p3=p1+p2
print(p1<p2)
print(p3)
    