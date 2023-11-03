import re
import sys      # Добавлено чисто ради реализации "Escape"

from output import OutputManager    # подключение модулей вывода информации
from data import DataManager     # подключение модулей для работы с информацией

'''
stringparser должен ыв итоге выдавать две переменные: flag - управляющая переменная 
и data - переменная в которой будут собственно содержаться данные
'''

class StringParser():
    "Класс, осуществляющий анализ строки и передачу управления. Последнее под вопросом"

    def __init__(self, command):
        self.command = command

    def parser(self):
        if re.search("Escape", self.command):
            sys.exit()
        elif re.match("del", self.command):
            DataManager(self.command).del_line()
        elif re.match("add", self.command):
            DataManager(self.command).add_line()
        elif re.match("print", self.command):
            OutputManager(self.command).print_line()
        elif re.match("find", self.command):
            OutputManager(self.command).find_line()
        else:
            print("Некорректный ввод команды")

    def print_parser(self):
        print('a')

    def add_parser(self):
        if re.search("driver", self.command):
            name = re.search('name=\d+', self.command)
            price = re.search('price=\d+', self.command)
            power = re.search('power=\d+', self.command)
            voltage_min = re.search('voltage_min=\d+', self.command)
            voltage_max = re.search('voltage_max=\d+', self.command)
            current = re.search('current=\d+', self.command)
            protection = re.search('protection=IP\d+', self.command)
            if (name and price and power and voltage_min and voltage_max and current and protection) == None:
                print("error")
            else: pass

        elif re.search("order", self.command):
            name = re.search('name=\d+', self.command)
            price = re.search('price=\d+', self.command)
            if (name and price) == None:
                print("error")
            else: pass

        elif re.search("component", self.command):
            name = re.search('name=\d+', self.command)
            oder_date = re.search('price=\d+', self.command)
            deadline = re.search('power=\d+', self.command)
            if (name and oder_date and deadline) == None:
                print("error")
            else: pass

        else:
            print("Ошибка в вводе типа обрабатываемых данных")

    def del_parser(self):
        pass

    def find_parser(self):
        pass

    def cost_parser(self):
        pass

    def components_parser(self):
        pass

    def exactly_parser(self):
        action = re.match("\w+", self.command)
        print(action[0])
        match action[0]:
            case "Escape": sys.exit()
            case "print": self.print_parser()
            case "add": self.add_parser()
            case "del": self.del_parser()
            case "find": self.find_parser()
            case "cost": self.cost_parser()
            case "components": self.components_parser()
            case _:
                print("Ошибка во вводе команды")
'''
        data = self.command.replace('print(', 'print, ')
        data = data.replace('=', ', ')
        data = data.replace(')', '')
        print(data)
        data = data.split(', ')

        print(type(data))
'''