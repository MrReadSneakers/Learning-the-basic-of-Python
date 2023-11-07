from parser import StringParser
from find_data_base import find_data_base

print("Перечень возможных действий:\ndel() - удаление записи\nadd() - создание новой записи\nprint() - вывод записи\nfind() - поиск информации")
print("Escape - завершение работы\nИные действия будут восприняты как некорректные.\n")

# проверка на наличие документа с заданнм именем, если такового нет, то создаст, но перезапишет если таковой уже существует
try: f = open('INFO')
except: f = open('INFO','w')
f.close()

find_data_base()

#проверка на корректность ввода команды и переход в функцию ее выполняющую
#придумать как это написать через case
while True:
    command = input("Введите команду: ")
    StringParser(command).parser()
    object_string_parser = StringParser(command)
    object_string_parser.exactly_parser()
    print('Значение flag: ', object_string_parser.flag)
    print('Значение parsered_string: ', object_string_parser.parsered_string)