"""
Задание 4.

Реализуйте базовый класс Car. У данного класса должны быть следующие публичные
 атрибуты:
speed, color, name, is_police (булево).

А также публичные методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).

Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.

Добавьте в базовый класс публичный метод show_speed,
который должен показывать текущую скорость автомобиля.

Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar)
и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


# Определяем класс
class Car:

    # Орпеделяем атрибуты
    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    # Орпеделяем метод "движение"
    def go(self):
        return f"Автомобиль {self.name} в движении."

    # Орпеделяем метод "остановки"
    def stop(self):
        return f"\nАвтомобиль {self.name} остановился."

    # Орпеделяем метод "поворот"
    def turn(self, direction):
        return f"\nАвтомобиль {self.name} повернул {direction}"

    # Орпеделяем метод "скорость"
    def show_speed(self):
        return f"\nВаша текущая скорость {self.speed}"


# Орпеделяем класс на базе Car для городского автомобиля
class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f"\nВаша скорость {self.speed} км/ч выше разрешённой " \
                   f"(60 км/ч)!"
        else:
            return f"Ваша скорость: {self.speed}"


# Орпеделяем класс на базе Car для спортивного автомобиля
class SportCar(Car):
    pass


# Орпеделяем класс на базе Car для рабочего автомобиля
class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f"\nВаша скорость {self.speed} км/ч выше разрешённой!"
        else:
            return f"Ваша скорость: {self.speed}"


# Орпеделяем класс на базе Car для полицейского автомобиля
class PoliceCar(Car):
    pass


# Передаём значения
town_car = TownCar("BMW", 50, "жёлтый", False)
print('1:\n' + town_car.go(), town_car.show_speed(), town_car.turn("налево"),
      town_car.turn("направо"), town_car.turn("налево"), town_car.stop())

sport_car = SportCar("Ford Mustang", 120, "красный", False)
print('2:\n' + sport_car.go(), sport_car.show_speed(),
      sport_car.turn("налево"), sport_car.turn("налево"), sport_car.stop())

work_car = WorkCar("Газель", 30, "зелёный", False)
print('3:\n' + work_car.go(), work_car.show_speed(), work_car.turn("налево"),
      work_car.show_speed(), work_car.turn("направо"),
      work_car.turn("в обратном направлении"), work_car.stop())

work_car = WorkCar("ГАЗ 66", 60, "синий", False)
print('4:\n' + work_car.go(), work_car.turn("направо"),
      work_car.show_speed(), work_car.turn("направо"), work_car.stop())

police_car = PoliceCar("Лада Гранта", 100, "белый с синей полосой", True)
print('5:\n' + police_car.go(), police_car.show_speed(),
      police_car.turn("налево"), police_car.turn("налево"),
      police_car.show_speed(), police_car.stop())
