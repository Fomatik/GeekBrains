# Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
from abc import ABC, abstractmethod


class AbstractClothes(ABC):
    @property
    @abstractmethod
    def tissue_consumption(self):
        pass

    @property
    @abstractmethod
    def unit(self):
        pass

    @abstractmethod
    def _calc_tissue_required(self):
        pass


class Clothes:
    _clothes = []

    def __init__(self, name, unit):
        self.name = name
        self._unit = unit
        self._tissue_consumption = None
        self._clothes.append(self)

    def _calc_tissue_consumption(self):
        raise NotImplemented

    @property
    def tissue_consumption(self):
        if not self._tissue_consumption:
            self._calc_tissue_consumption()
        return self._tissue_consumption

    @property
    def unit(self):
        return self._unit

    @unit.setter
    def unit(self, unit):
        self._unit = unit
        self._tissue_consumption = None

    @property
    def total_tissue_consumption(self):
        return sum([item.tissue_consumption for item in self._clothes])


class Coat(Clothes):
    def _calc_tissue_consumption(self):
        self._tissue_consumption = round(self.unit / 6.5 + 0.5, 2)

    @property
    def V(self):
        return self.unit

    @V.setter
    def V(self, size):
        self.unit = size

    def __str__(self):
        return f"Для пошива {self.name} {self.unit} размера, требуется {self.tissue_consumption} кв.м. ткани."


class Suit(Clothes):
    def _calc_tissue_consumption(self):
        self._tissue_consumption = round(2 * self.unit + 0.3, 2)

    @property
    def H(self):
        return self.unit

    @H.setter
    def H(self, height):
        self.unit = height

    def __str__(self):
        return f"Для пошива {self.name} {self.unit}м. роста, требуется {self.tissue_consumption} кв.м. ткани."


coat = Coat('пальто от Зара', 12)
print(coat)
coat.V = 14
print(coat)

suit = Suit('костюм от Армани', 1.6)
print(suit)
suit.H = 1.8
print(suit)

print(coat.total_tissue_consumption)
print(suit.total_tissue_consumption)