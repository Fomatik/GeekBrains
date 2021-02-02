# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

import random

with open('exercise_5.txt', 'w') as my_file:
    my_file.write(' '.join(str(random.randint(1, 100)) for i in range(20)))

with open('exercise_5.txt', 'r') as my_file_num:
    num = list(e for e in my_file_num.read().split(' '))
    n = 0
    for i in num:
        i = int(i)
        n += i

    print(f'Список чисел: {", ".join(i for i in num)}.')
    print(f'Сумма чисел: {n}.')