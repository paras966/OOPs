class Mother:
    def __init__(self) -> None:
        self.name="manju"
        super().__init__()
    def print(self):
        print("Mother")
class Father:
    def __init__(self) -> None:
        self.name="Ajay"
        #super().__init__()
    def print(self):
        print("Father")

class Child(Mother, Father):
    def __init__(self) -> None:
        super().__init__()
    def print(self):
        print("CHILD name ",self.name)

c=Child()
c.print()
print(Child.mro())

        