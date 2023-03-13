# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

# Ввод:  [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# 5
# 15
# Вывод: [1, 9, 13, 14, 19]

# pytest -v tests\test_32.py


def is_in_mass(num_lst,
               min_num: int,
               max_num: int):
    """Возвращает список индексов элементов списка, которые
    находятся в диапазоне [min_num,max_num] """
    
    list_indexes = []
    for i in range(len(num_lst)):
        if num_lst[i] >= min_num and num_lst[i] <= max_num:
            list_indexes.append(i)
    return list_indexes
    # if list_indexes != []:
    #     return print(f'Индесы чисел из указанного вами диапазона: {list_indexes}')
    # if list_indexes == []:
    #     return print('В вашем списке нет чисел из выбранного диапазона')


is_in_mass(list(map(int, input('Введите масив чисел через запятую: ').split(','))), int(input('Минимальное число: ')), int(input('Максимальное число: ')))