from abc import ABC,abstractmethod

class Automobile(ABC):
    def __init__(self):
        print("automobile Created")
    @abstractmethod
    def start(self):
        print("Strat Automobile")

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def drive(self):
        pass

class Car(Automobile):
    def __init__(self):
        print("Car created")

    def start(self):
        super().start()
        print("Start car")

    def stop(self):
        pass

    def drive(self):
        pass
c=Car()
c.start()