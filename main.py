from parser import StringParser
from find_data_base import find_data_base
from output import OutputManager
from data import DataManager


print("Перечень возможных действий:\ndel() - удаление записи\n"
      "add() - создание новой записи\nprint() - вывод записи\nfind() - поиск информации")
print("Escape - завершение работы\n(После ввода команды через '.' вводится дополнение. "
      "Пример: print.driver() )\nФормат даты: ГГГГ/ММ/ДД\nИные действия будут восприняты как некорректные.\n")

find_data_base()

# проверка на корректность ввода команды и переход в функцию ее выполняющую
# придумать как это написать через case
while True:
    command = input("Введите команду: ")
    object_string_parser = StringParser(command)
    object_string_parser.exactly_parser()

    control = object_string_parser.control
    parsered_string = object_string_parser.parsered_string
    print('Значение control: ', object_string_parser.control)
    print(type(parsered_string))
    print('Значение parsered_string: ', object_string_parser.parsered_string)
    print(type(control))

    if control is not None:
        match control[0]:
            # не забыть сделать отчет для пользователя, что действие все таки произошло
            case 'print': OutputManager(control, parsered_string).print_BD()
            case 'find': OutputManager(control, parsered_string).find_BD()
            case 'add': DataManager(control, parsered_string).add_BD()
            case 'del': DataManager(control, parsered_string).del_BD()
            case 'cost': OutputManager(control, parsered_string).cost_BD()
            case 'components': OutputManager(control, parsered_string).components_BD()
