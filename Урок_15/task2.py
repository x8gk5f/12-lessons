# Задание 2. Вместимость автобуса
class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"Вместимость одного автобуса {self.name}  {capacity} пассажиров"

class Autobus(Transport):
    def seating_capacity(self, capacity=50):
        # Возвращаем строку в ожидаемом формате
        return f"Вместимость одного автобуса {self.name}: {capacity} пассажиров"

bus = Autobus("Renaul Logan", 180, 12)
print(bus.seating_capacity())
