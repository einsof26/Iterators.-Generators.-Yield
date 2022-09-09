nested_list = [['a', 'b', 'c'],
               ['d', 'e', 'f', 'h', False],
               [1, 2, None],
               ]


def FlatIterator(lst):  # Итератор, обрабатывающий вдойное вложение списка
    li = []  # Список для результатовmain
    it = iter(lst)  # создает итератор
    for i in range(
            len(lst)):  # Проходит по элементам базового списка и добавляет элементы вложенного использую метод next
        li.extend(next(it))
    for y in li:  # Добавляет в yield результирующие элементы
        yield y


for item in FlatIterator(nested_list):
    print(item)
flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)
