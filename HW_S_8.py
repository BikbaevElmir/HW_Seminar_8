# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной

from csv import DictReader, DictWriter
from os.path import exists
class NameError(Exception):
    def __init__(self, txt):
        self.txt = txt

def get_info():
    flag = False
    while not flag:
        try:
            first_name = input('Имя: ')
            if len(first_name) < 2:
                raise NameError('Слишком короткое имя')
            second_name = input('Фамилия: ')
            if len(first_name) < 2:
                raise NameError('Слишком короткая фамилия')
            phone_number = input('Телефон : ')
            if len(phone_number) < 11:
                raise NameError('Номер должен быть не менее 11 символов')
        except NameError as err:
            print(err)
        else:
            flag = True
    return [first_name, second_name, phone_number]

def creat_file(file_name):
    with open(file_name, 'w',encoding='utf-8', newline='') as data:
        f_w = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_w.writeheader()

def write_file(file_name):
    user_data = get_info()
    res = read_file(file_name)
    new_obl = {'first_name' : user_data[0], 'second_name' : user_data[1], 'phone_number': user_data[2]}
    res.append(new_obl)
    standart_write(file_name, res)

def read_file(file_name):
    with open(file_name, encoding='utf-8', newline='') as data:
        f_r = DictReader(data)
        return list(f_r)

def remove_row(file_name):
    search = int(input('Введите номер строки для удаления:'))
    res = read_file(file_name)
    if search <= len(res):
        res.pop(search - 1)
        standart_write(file_name, res)
    else:
        print('Введен неверный номер строки')

def standart_write(file_name, res):
    with open(file_name, 'w', encoding='utf_8', newline='') as data:
        f_w = DictWriter(data, fieldnames=['first_name', 'second_name', 'phone_number'])
        f_w.writeheader()
        f_w.writerows(res)

file_name = 'phone.csv'
new_file_name = 'copy_phone.csv'
def main():
    while True:
        command = input('Введите команду: ')
        if command == 'q':
            break
        elif command == 'w':
            if not exists(file_name):
                creat_file(file_name)
            write_file(file_name)
        elif command == 'r':
            if not exists(file_name):
                print('Файл отсутствует, создайте файл')
                continue
            print(*read_file(file_name))
        elif command == 'd':
            if not exists(file_name):
                creat_file(file_name)
                print('Файл отсутствует, создайте файл')
                continue
            remove_row(file_name)
        elif command == 'c':
            if not exists(file_name):
                print('Файл отсутствует, создайте файл')
                continue
            if not exists(new_file_name):
                creat_file(new_file_name)
                print('Создан файл copy_phone.csv')
            copy_row(file_name, new_file_name)

 main()