# -*- coding: utf-8 -*-

# Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.

import json

with open('exercise_7.txt') as report:
    report_list = list(el.split(' ') for el in report.read().splitlines())
    average_profit_list = []
    average_profit = {}
    firm_list = {}
    counter = 0
    for name, ownership, proceeds, costs in report_list:
        profit = int(proceeds) - int(costs)
        firm_list[name] = profit
        if profit > 0:
            average_profit_list.append(profit)
            counter += 1
    average_profit['average_profit'] = sum(average_profit_list) / counter
    json_list = [firm_list, average_profit]
    with open('exercise_7.json', 'w') as json_file:
        json.dump(json_list, json_file, ensure_ascii=False)