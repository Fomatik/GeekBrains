# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class DivisionByNull(Exception):
    def __init__(self, msg):
        self.msg = msg


dividend = input("Введите делимое: ")
divider = input("Введите делитель: ")

try:
    quotient = float(dividend) / float(divider)
    print(f'{dividend} / {divider} = {quotient}')
except ZeroDivisionError:
    print('Деление на 0 невозможно!')
except ValueError:
    print("Вы ввели не число!")