class Circle:
    def __init__(self,radius):
        self.radius=radius
    def __str__(self):
        return "Circle class takes radius as input"

c=Circle(5)
print(c)