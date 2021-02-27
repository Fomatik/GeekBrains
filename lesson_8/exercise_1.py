# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class Date:
    def __init__(self, date):
        self.date = str(date)

    @classmethod
    def convert(cls, date):
        date_l = list(map(int, date.split('-')))
        print(date_l)
        print(*date_l, sep=' ')

    @staticmethod
    def valid(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2021 >= year >= 0:
                    print(f'Дата правильная.')
                else:
                    print(f'Неправильный год')
            else:
                print(f'Неправильный месяц')
        else:
            print(f'Неправильный день')


Date.convert('15-02-2021')
Date.valid(15, 2, 2021)
Date.valid(15, 2, 2022)
Date.valid(15, 13, 2021)
Date.valid(33, 12, 2021)