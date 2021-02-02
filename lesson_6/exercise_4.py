# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехал'

    def stop(self):
        return f'{self.name} остановилась'

    def turn(self, direction):
        return f'{self.name} повернул {direction}'

    def show_speed(self):
        return fr'Скорость движения {self.name}: {self.speed} км\ч.'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(fr'Скорость {self.name}: {self.speed} км\ч.')

        if self.speed > 60:
            return f'Скорость движения {self.name} превышена.'
        else:
            return f'Скорость движения {self.name} в норме.'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(fr'Скорость движения {self.name}: {self.speed} км\ч.')

        if self.speed > 40:
            return f'Скорость движения {self.name} превышена.'
        else:
            return f'Скорость движения {self.name} в норме.'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} из Полиции.'
        else:
            return f'{self.name} не из Полиции.'


audi = SportCar(100, 'красный', 'Audi', False)
kia = TownCar(50, 'серый', 'Kia', False)
kamaz = WorkCar(50, 'белый', 'Камаз', False)
uaz = PoliceCar(70, 'синий', 'УАЗ', True)
print(kamaz.turn("налево"))
print(f'Когда {kia.turn("направо")}, тогда {audi.stop()}.')
print(f'{kamaz.go()}.')
print(f'{kamaz.show_speed()}')
print(f'{kamaz.name} {kamaz.color}.')
print(f'{audi.name} из полиции? {audi.is_police}.')
print(f'{kamaz.name} из полиции? {kamaz.is_police}.')
print(audi.show_speed())
print(kia.show_speed())
print(uaz.police())
print(uaz.show_speed())