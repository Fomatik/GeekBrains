# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
with open('exercise_3.txt') as my_file:

    my_file_dict = dict(e.split(' ') for e in my_file.read().splitlines())

    print(f'Список сотрудников и их окладов: {", ".join([f"{key}: {value}" for key, value in my_file_dict.items()])}.')

    min_salary = []
    average_salary = []

    for key, value in my_file_dict.items():
        if int(value) < 20000:
            min_salary.append(key)

    for i in my_file_dict.values():
        average_salary.append(int(i))

    print(f'Список сотрудников с окладом меньше 20 тыс.: {", ".join(min_salary)}.')
    print(f'Средний доход сотрудников: {sum(average_salary) / len(average_salary)}')