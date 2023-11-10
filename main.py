from parser import StringParser
from find_data_base import find_data_base
from output import OutputManager
from data import DataManager

print("Перечень возможных действий:\ndel() - удаление записи\nadd() - создание новой записи\nprint() - вывод записи\nfind() - поиск информации")
print("Escape - завершение работы\n(После ввода команды через '.' вводится дополнение. Пример: print.driver() )\nФормат даты: ГГГГ/ММ/ДД\nИные действия будут восприняты как некорректные.\n")

find_data_base()

#проверка на корректность ввода команды и переход в функцию ее выполняющую
#придумать как это написать через case
while True:
    command = input("Введите команду: ")
    object_string_parser = StringParser(command)
    object_string_parser.exactly_parser()

    flag = object_string_parser.flag
    parsered_string = object_string_parser.parsered_string
    print('Значение flag: ', object_string_parser.flag)
    print('Значение parsered_string: ', object_string_parser.parsered_string)
    print(flag[0])
    if flag != None:
        match flag[0]:
            #не забыть сделать отчет для пользователя, что действие все таки произошло
            case 'print': OutputManager(flag, parsered_string).print_BD()
            case 'find': OutputManager(flag, parsered_string).find_BD()
            case 'add': DataManager(flag, parsered_string).add_BD()
            case 'del': DataManager(flag, parsered_string).del_BD()
            case 'cost': OutputManager(flag, parsered_string).cost_BD()
            case 'components': OutputManager(flag, parsered_string).components_BD()



'''
#зачатки запоса в БД для поиска стоимости заказа, но что то полно не так
SELECT contract.name, component.component_id, component_driver.driver_id, driver_contract.contract_id, contract.contract_id price FROM contract
JOIN component, component_driver, driver_contract, driver ON component.component_id=component_driver.component_id AND component_driver.driver_id=driver_contract.driver_id AND driver_contract.contract_id=contract.contract_id
'''