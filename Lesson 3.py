# -*- coding: utf-8 -*-

# 1 exercise Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
def split(z=int(input('Введите делимое число: ')), x=int(input('Введите число делитель: '))):
    if x == 0:
        return print('Деление на 0 невозможно!')
    y = z / x
    return print(f'{z} / {x} = {y}')


split()


# 2 exercise Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
def new_func(name=input("Введите имя: "), surname=input("Введите фамилию: "), year=input("Год рождения: "), city=input("Город проживания: "), email=input("Введите email: "), phone_number=input("Номер телефона: ")):
    return print(f'Имя: {name}, фамилия: {surname}, год рождения: {year}, город: {city}, почта: {email}, телефон: {phone_number}.')


new_func()


# 3 exercise Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
def my_func(f, g, h):
    if f > h and g > h:
        j = f + g
    elif f > g and h > g:
        j = f + h
    else:
        j = g + h
    return j


print("Функция для сложения двух наибольших аргументов из трёх.")
print(
    f"Результат функции: {my_func(int(input('Введите первый аргумент: ')), int(input('Введите второй аргумент: ')), int(input('Ведите третий аргумент: ')))}")


# 4 exercise Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y). При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **. Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
def exponentiation(x, y):
    return x ** y


print('Функция возведения действительного положительного числа в отрицательную степень.')
print(
    f'Результат функции: {exponentiation(float(input("Введите действительное положительное число: ")), int(input("Введите целое отрицательное число: ")))}')


def exponentiation_1(x, y):
    y = abs(y)
    z = 1
    result = 1
    while z <= y:
        result *= x
        z += 1
    return 1/result


print('Функция возведения действительного положительного числа в отрицательную степень.')
print(f'Результат функции: {exponentiation_1(float(input("Введите действительное положительное число: ")), int(input("Введите целое отрицательное число: ")))}')


# 5 exercise Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение программы завершается. Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
def sum_num():
    global el_sum
    num = list(input('Введите числа разделённые пробелами (для окончания ввода цифр и выхода из программы введите "q") : ').split(' '))
    for i in num:
        if i.isdigit():
            el_sum = el_sum + int(i)
    if 'q' in num:
        print('Выход из программы.')
        return el_sum
    else:
        print(f'Результат сложения: {el_sum}')
        print('Продолжите ввод цифр.')
        sum_num()
    return el_sum


print('Функция сложения списка цифр.')
el_sum = 0
a = sum_num()
print(f'Результат сложения: {a}')


# 6 exercise Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().
def int_func(string=input('Введите слово или строку маленькими латинскими буквами: ')):
    print(string.title())


int_func()
