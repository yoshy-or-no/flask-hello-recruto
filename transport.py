class Transport:
    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed

    def move(self):
        return f"Транспорт {self.name} движется со скоростью {self.max_speed} км/ч."

class Car(Transport):
    def __init__(self, name, max_speed, wheels):
        super().__init__(name, max_speed)
        self.wheels = wheels
    def move(self):
        return f"Автомобиль {self.name} движется со скоростью {self.max_speed} км/ч, на {self.wheels} колесах"

class Airolane(Transport):
    def __init__(self, name, max_speed, altitude):
        super().__init__(name, max_speed)
        self.altitude = altitude
    def move(self):
        return f"Самолет {self.name} летит на высоте {self.altitude} метров, со скоростью {self.max_speed} км/ч."


car = Car("toyota","180","4")
print(car.move())
airoplane = Airolane("boing","900", "10000")
print(airoplane.move())
