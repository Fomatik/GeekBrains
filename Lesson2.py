# -*- coding: utf-8 -*-


# 1 exercise Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
result_list = [2, 'text', 456, 45.3, None]
for i in result_list:
    print(type(i))

# 2 exercise Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов необходимо использовать функцию input().
s = list(input("Введите несколько элементов списка (без пробелов): "))
n = 0
for i in range(int(len(s)//2)):
    s[n], s[n+1] = s[n+1], s[n]
    n += 2
print(s)

# 3 exercise Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.
year = {
    "зиме": [12, 1, 2],
    "весне": [3, 4, 5],
    "лете": [6, 7, 8],
    "осени": [9, 10, 11]
}
month = int(input("Введите месяц числом: "))
for key, value in year.items():
    if month in value:
        print(f"{month} месяц относится к {key}.")

# 4 exercise Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки. Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.word.split() 
word = input("Введите несколько слов через пробел: ")
for n, i in enumerate(word.split()):
    if len(i) > 10:
        i = i[:10]
    print(n, i)

# 5 exercise Реализовать структуру "Рейтинг", представляющую собой не возрастающий набор натуральных чисел. У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
my_list = [7, 5, 3, 3, 2]
num = int(input("Введите рейтинг от 1 до 9: "))
num_in = None
for i, n in enumerate(my_list) :
    if num > n:
        num_in = i
        break
if num_in is None:
    my_list.append(num)
else:
    my_list.insert(num_in, num)
print(my_list)

# 6  Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения). Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}), 
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например название, а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }
prods = []
while input("Вы хотите добавить товар? введите да/нет: ") == "да":
    prod_char = {}
    num = int(input("Введите номер товара: "))
    prod_char["название"] = input("Введите название товара: ")
    prod_char["цена"] = input("Введите цену товара: ")
    prod_char["количество"] = input("Введите количество товара: ")
    prod_char["ед"] = input("Введите единицу измерения товара: ")
    prods.append(tuple([num, prod_char]))
# print(prods)
analytics = {}
for _tuple, _values in prods:
    for i, n in _values.items():
        if i not in analytics.keys():
            analytics[i] = list()
        analytics[i].append(_values[i])
print(f"Аналитика о товарах:\n {analytics}")
