class Transport:
    def __init__(self, name, max_speed, capacity):
        self.name = name
        self.max_speed = max_speed
        self.__capacity = capacity

    def move(self):
        return f"{self.name} перевозит грузы."

    def get_capacity(self):
        return self.__capacity

class Truck(Transport):
    def __init__(self, name, wheels, max_speed, capacity):
        super().__init__(name, max_speed, capacity)
        self.wheels = wheels

    def move(self):
        return f"Грузовик {self.name} с {self.wheels} колесами движется со скоростью {self.max_speed} км/ч."

    def ton(self, ton):
        if ton <= self.get_capacity():
            return f'все ок по грузу'
        else:
            return f'круз слишком велик'

truck = Truck( 'грузовик', 4, 150, 10)
print(truck.move())
print(truck.ton(2))
print(truck.ton(150))