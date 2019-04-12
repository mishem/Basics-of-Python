# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os

# def make_dir (name):
#     try:
#         os.mkdir(name)
#     # for i in range(1,10):
#     #     os.mkdir('dir_' + str(i))
#     except FileExistsError:
#         print('dir_{} - уже существует'.format(name))
#
# def remove_dir(name):
#
#     try:
#         os.removedirs(name)
#      # for i in range(1,10):
#      #     os.removedirs('dir_' + str(i))
#     except FileNotFoundError:
#         print('dir_{} - папка не существует'.format(name))
#
# def start ():
#     answer =''
#
#     while answer != '3':
#
#         answer = input('Выберите пункт меню:\n'
#                        '1. Создать папки dir_1 - dir_9\n'
#                        '2. Удалить папки dir_1 - dir_9\n'
#                        '3. Выход\n')
#         if answer =='3':
#             break
#         if answer == '1':
#             for i in range(1, 10):
#                 make_dir('dir_' + str(i))
#
#         elif answer == '2':
#             for i in range(1, 10):
#                 remove_dir('dir_' + str(i))
#
# if __name__ == '__main__':
#     start()

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def list_dir():
    list = os.listdir()
    for i in list:
        if os.path.isdir(i):
            print(i)
if __name__ == '__main__':
    list_dir()

# Задача-3:
# Напишите скрипт создающий копию файла, из которого запущен данный скрипт

import shutil

def file_copy ():
    file_name = os.path.realpath(__file__)
    new_file = file_name +'.copy'
    if os.path.isfile(new_file) != True:
        shutil.copy(file_name, new_file)
        return new_file + ' - создан'
    else:
        return 'Файл уже скопирован'

if __name__ == '__main__':
    print(file_copy())


