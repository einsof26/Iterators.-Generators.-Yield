nested_list = [['a', 'b', 'c'],
               ['d', 'e', 'f', 'h', False],
               [1, 2, None],
               ]

flat_generator = (subelem for elem in nested_list for subelem in elem)  # Генератор, обрабатывающий двойное вложние


for item in flat_generator:
    print(item)
print('=================')


def flat_generator(lst):  #Генератор, обрабатывающий любое количество вложеннных списков
    res_lst = []
    while lst:  #Пока список не пустой
        elem = lst.pop()  #Выбирает последний элемент, удаляет и обрабатывает
        if type(elem) == list:  #Если это список то добавляем в конец основного списка, для последующей обработки
            lst.extend(elem)
        else:  #Если одиночный элемент, добавлят его в результирующий список
            res_lst.append(elem)

    return res_lst  #Результирующий список одиночных элементов


for item in flat_generator(nested_list):
    print(item)
