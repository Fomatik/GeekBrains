# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

# Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь.

# Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.

class Storehouse:
    def __init__(self):
        self.__storage = []

    def add(self, item):
        self.__storage.append(item)

    def transfer(self, num, department):
        item = self.__storage[num]
        item.department = department
        del self.__storage[num]

    def __getitem__(self, key):
        return self.__storage[key]

    def __delitem__(self, key):
        del self.__storage[key]

    def __str__(self):
        return f"На складе сейчас {len(self.__storage)} устройства"

    def __repr__(self):
        return '\n'.join(str(item) for item in self.__storage)


class OfficeEquipment:
    def __init__(self, model, color, paper_size, price):
        self.model = model
        self.col = color
        self.paper = paper_size
        self.price = price

    def __str__(self):
        return f'Модель: {self.model}, цветность: {self.col}, формат: {self.paper} , цена: {self.price}'


class Printer(OfficeEquipment):
    def __init__(self, *args, print_type):
        super().__init__(*args)
        self.type = print_type

    def __str__(self):
        return f'Принтер: \n' + OfficeEquipment.__str__(self).replace(',', '\n') + \
               f', технология печати: {self.type}'.replace(',', '\n')


class Scanner(OfficeEquipment):
    def __init__(self, *args, scan_type):
        super().__init__(*args)
        self.scan_type = scan_type

    def __str__(self):
        return f'Сканер: \n' + OfficeEquipment.__str__(self).replace(',', '\n') + \
               f', тип сканирования: {self.scan_type}'.replace(',', '\n')


class Copier(OfficeEquipment):
    def __init__(self, *args, resource):
        super().__init__(*args)
        self.res = resource

    def __str__(self):
        return f'МФУ: \n' + OfficeEquipment.__str__(self).replace(',', '\n') + \
               f', максимальная месячная нагрузка: {self.res}'.replace(',', '\n')


if __name__ == '__main__':
    printer = Printer('HP Laser 107r (5UE14A)', 'черно-белый', 'A4', '8415', print_type='лазерная')
    print(printer)
    scan = Scanner('Canon L36ei (3421V853)', 'цветной', 'А0', '255 288', scan_type='протяжный сканер')
    print(scan)
    copier = Copier('HP Laser 135w', 'черно-белая', 'A4', '12 495', resource='10000 страниц')
    print(copier)

    print('\n')

    storage = Storehouse()
    storage.add(Printer('HP Laser 107r (5UE14A)', 'черно-белый', 'A4', '8415', print_type='лазерная'))
    storage.add(Scanner('Canon L36ei (3421V853)', 'цветной', 'А0', '255 288', scan_type='протяжный сканер'))
    storage.add(Copier('HP Laser 135w', 'черно-белая', 'A4', '12 495', resource='10000 страниц'))
    print(storage)

    print('\n')

    print('Передаём Сканер в "Отдел кадров"')
    storage.transfer(1, 'Отдел Кадров')

    print('\n')

    print(storage)
    print(storage.__repr__())