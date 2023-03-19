# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.

# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной

# Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, 
# и Вы должны реализовать функционал для изменения и удаления данных



def show_data():
    with open('phone-list.txt', 'r', encoding='utf-8') as peoples:
        return peoples.read()


def add_data():
    with open('phone-list.txt', 'a', encoding='utf-8') as peoples:
        peoples.write(input('Добавьте данные о человеке: ') + '\n')


def finder():
    with open('phone-list.txt', 'r', encoding='utf-8') as peoples:
        person = peoples.read().split('\n')
        find = input('Введите ключевые фразы для поиска: ')
        for item in person:
            if find in item:
                print(item)




def change_data():
    with open('phone-list.txt', 'r', encoding='utf-8') as peoples:
        person = peoples.read()
        print(person)
    print()

    with open('phone-list.txt', 'r', encoding='utf-8') as peoples:
        person = peoples.read().split('\n')
        find = input('Введите ключевые фразы для поиска: ')
        for item in person:
            if find in item:
                print(item)
    print()    

    
    with open('phone-list.txt', 'r', encoding='utf-8') as peoples:
        person = peoples.read()
        

    new = person.replace(input('Вы выбрали строку для изменения, что вы хотите в ней изменить?: '), input('На что вы хотите поменять?: '))
    print()

    with open('phone-list.txt', 'w', encoding='utf-8') as peoples:
        peoples.write(new)

    with open('phone-list.txt', 'r', encoding='utf-8') as peoples:
        person = peoples.read()
        print(f'ВЫ ВНЕСЛИ ИЗМЕНЕНИЯ, ПЕРЕД ВАМИ ОБНОВЛЕННАЯ БАЗА ДАННЫХ\n\n{person}')




def delete_strings():

    with open('phone-list.txt', 'r', encoding='utf-8') as peoples:
        person = peoples.read()
        print(person)

    print()

    with open('phone-list.txt', 'r', encoding='utf-8') as peoples:
        person = peoples.read().split('\n')
        
        find = input('Введите ключевые фразы для поиска строки, которую хотите удалить: ')
        for item in person:
            if find in item:
                print(f'Вы удаляете строку: {item},\nЕсли уверены, напишите "ДА"')
                a = item 

    print() 

    with open('phone-list.txt', 'r', encoding='utf-8') as peoples:
        person = peoples.read()   

    test_word = input()
    if test_word == 'ДА':
        new = person.replace((f'{a}\n'), (''))
        print()

        with open('phone-list.txt', 'w', encoding='utf-8') as peoples:
            peoples.write(new)

        with open('phone-list.txt', 'r', encoding='utf-8') as peoples:
            person = peoples.read()
            print(f'ВЫ ВНЕСЛИ ИЗМЕНЕНИЯ, ПЕРЕД ВАМИ ОБНОВЛЕННАЯ БАЗА ДАННЫХ\n\n{person}')

    else:
        print('Вы отказались от изменений, ваша база данных остается прежней')
        print()
        with open('phone-list.txt', 'r', encoding='utf-8') as peoples:
            person = peoples.read()
            print(person)
    
    
        

    
def manage_database():
        print('Для управления базой данных используйте следующие команды:\n'
            '"1" - Просмотр всех записей базы данных;\n'
            '"2" - Добавление да нных (построчно);\n'
            '"3" - Поиск данных по ключевому запросу;\n'
            '"4" - Изменение данных (дописать, изменить, либо удалить часть строки);\n'
            '"5" - Удаление строк целиком;\n'
            '"0" - Завершение работы с базой данных')

        work_mode = int(input('Выберите нужную вам команду из предложенных: '))

        if work_mode == 1:
                print(show_data())
        elif work_mode == 2:
                add_data()
        elif work_mode == 3:
                finder()
        elif work_mode == 4:
                change_data()
        elif work_mode == 5:
                delete_strings()
        elif work_mode == 0:
            print('Вы завершили работу с базой данных')
            
            

    
manage_database()


# def finder_2():
#     with open('phone-list.txt', 'r', encoding='utf-8') as peoples:
#         person = peoples.read().split('\n')
#         a 
#         find = input('Введите ключевые фразы для поиска: ')
#         for item in person:
#             if find in item:
#                 a = item











# add_data()

# print(show_data())

# finder()
# change_data()
# new()
# delete_strings()