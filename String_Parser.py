from Alternative import Dell_Empty_line, Find_Same_Line     # запасной вариант, некогда был основным, дальше скорее всего никогда не будет использован, но пусть тут пока будет
import re
import sys      # Добавлено чисто ради реализации "Escape"

from Output_Manader import Output    # подключение модулей вывода информации
from Data_Manager import Data     # подключение модулей для работы с информацией

class StringParser():
    "Класс, осуществляющий анализ строки и передачу управления. Последнее под вопросом"

    def __init__(self, command):
        self.command = command

    def Parser(self):
        if re.search("Escape", self.command):
            sys.exit()
        elif re.match("del", self.command):
            Data(self.command).del_line()
        elif re.match("add", self.command):
            Data(self.command).add_line()
        elif re.match("print", self.command):
            Output(self.command).print_line()
        elif re.match("find", self.command):
            Output(self.command).find_line()
        else:
            print("Некорректный ввод команды")

        # Find_Same_Line()
        # Dell_Empty_line()


