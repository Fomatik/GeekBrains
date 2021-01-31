# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

rus_original = {'Один': 'One', 'Два': 'Two', 'Три': 'Three', 'Четыре': 'Four'}

with open('exercise_4.txt') as original:
    original_dict = dict(e.split(' — ') for e in original.read().splitlines())
    for k, v in rus_original.items():
        if v in original_dict:
            rus_original[k] = original_dict[v]

with open('exercise_4.1.txt', 'w') as translated_original:
    translated_original.writelines("\n".join([f"{key} — {value}" for key, value in rus_original.items()]))