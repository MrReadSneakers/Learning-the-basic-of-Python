import re
import sys      # Добавлено чисто ради реализации "Escape"
from datetime import *   #лобавлено для проверки что дата заказа раньше даты дедлайна (если получится)


'''
stringparser должен ыв итоге выдавать две переменные: flag - управляющая переменная 
и data - переменная в которой будут собственно содержаться данные
'''

class StringParser():
    "Класс, осуществляющий анализ строки и передачу управления. Последнее под вопросом"


    def __init__(self, command):
        self.command = command
        self.flag = None
        self.parsered_string = None


    def print_parser(self):
        if re.search("print\.\w+\(\)", self.command) and (('driver' in self.command) or ('contract' in self.command) or ('component' in self.command)):
            if 'driver' in self.command:
                self.flag = ['print','driver',0]
            elif 'contract' in self.command:
                self.flag = ['print','contract',0]
            else:
                self.flag = ['print','component',0]
            self.parsered_string = [0]
            #print(self.flag)
        elif re.search("print\.\w+\(\w+\)", self.command) and (('driver' in self.command) or ('contract' in self.command) or ('component' in self.command)):
            if 'driver' in self.command:
                self.flag = ['print','driver',1]
            elif 'contract' in self.command:
                self.flag = ['print','contract',1]
            else:
                self.flag = ['print','component',1]
            #print(self.flag)
            self.parsered_string = re.search("\(\w+\)", self.command)
            self.parsered_string = self.parsered_string[0]
            self.parsered_string = self.parsered_string.replace('(','')
            self.parsered_string = self.parsered_string.replace(')','')
            #print(self.parsered_string)
        else:
            print("Ошибка в вводе типа обрабатываемых данных")


    def add_parser(self):
        if re.search("component_driver", self.command):
            self.flag = 'add','component_driver','{}'.format(((re.search("\(\w+:", self.command)[0]).replace('(','')).replace(':',''))
            #self.parsered_string = (self.command.split(': '))[1].replace(')','').split(', ').split('-')
            self.parsered_string = re.split(", |-", (self.command.split(': '))[1].replace(')', ''))

        elif re.search("driver_contract", self.command):
            self.flag = 'add','driver_contract','{}'.format(((re.search("\(\w+:", self.command)[0]).replace('(','')).replace(':',''))
            #self.parsered_string = (self.command.split(': '))[1].replace(')','').split(', ').split('-')
            self.parsered_string = re.split(", |-", (self.command.split(': '))[1].replace(')', ''))

        elif re.search("driver", self.command):
            name = re.search('name=\w+', self.command)
            power = re.search('power=\d+', self.command)
            voltage_min = re.search('voltage_min=\d+', self.command)
            voltage_max = re.search('voltage_max=\d+', self.command)
            current = re.search('current=\d+', self.command)
            protection = re.search('protection=IP\d+', self.command)
            #protection = protection[0].replace('IP','')
            select_voltage_min = voltage_min[0].split('=')
            select_voltage_max = voltage_max[0].split('=')
            if ((name and power and voltage_min and voltage_max and current and protection) == None) or (int(select_voltage_min[1]) > int(select_voltage_max[1])):
                print("error")
            else:
                # не забыть  добавить проверку на напряжение
                self.parsered_string = (name[0].replace('name=','') + '=' + power[0].replace('power=','')
                                        + '=' + voltage_min[0].replace('voltage_min=','') + '='
                                        + voltage_max[0].replace('voltage_max=','') + '='
                                        + current[0].replace('current=','') + '='
                                        + protection[0].replace('protection=IP',''))
                self.parsered_string = self.parsered_string.split('=')
                self.flag = ['add','driver',1]
                #print(self.parsered_string)

        elif re.search("component", self.command):
            name = re.search('name=\w+', self.command)
            price = re.search('price=\d+', self.command)
            if (name and price) == None:
                print("error")
            else:
                self.parsered_string = (name[0].replace('name=', '') + '=' + price[0].replace('price=', ''))
                self.parsered_string = self.parsered_string.split('=')
                self.flag = ['add','component',1]

        #придумать как адекватно реализовать этот блок с датами
        elif re.search("contract", self.command):
            name = re.search('name=\w+', self.command)
            contract_date = re.search('contract_date=\d{4}/\d\d/\d\d', self.command)    #не забыть сделать проверку того, что дата заказа раньше даты дедлайна, но это потом. Когда нибудь
            deadline = re.search('deadline=\d{4}/\d\d/\d\d', self.command)

            select_deadline = re.split("=|/|\n", deadline[0])
            select_deadline = date(int(select_deadline[1]), int(select_deadline[2]), int(select_deadline[3]))
            select_contract_date = re.split("=|/|\n", contract_date[0])
            select_contract_date = date(int(select_contract_date[1]), int(select_contract_date[2]), int(select_contract_date[3]))

            if (name and contract_date and deadline) == None:
                print("error")
            else:
                if select_contract_date > select_deadline:
                    print("error")
                else:
                    self.parsered_string = (name[0].replace('name=', '') + '=' + contract_date[0].replace('contract_date=', '')
                                            + '=' + deadline[0].replace('deadline=', ''))
                    self.parsered_string = self.parsered_string.split('=')
                    self.flag = ['add','contract',1]

        else:
            print("Ошибка в вводе типа обрабатываемых данных")


    def del_parser(self):
        if re.search("del\.\w+\(\w+\)", self.command) and (('driver' in self.command) or ('contract' in self.command) or ('component' in self.command)):
            if 'driver' in self.command:
                self.flag = ['del', 'driver', 1]
            elif 'contract' in self.command:
                self.flag = ['del', 'contract', 1]
            else:
                self.flag = ['del', 'component', 1]
            #print(self.flag)
            self.parsered_string = re.search("\(\w+\)", self.command)
            self.parsered_string = self.parsered_string[0]
            self.parsered_string = self.parsered_string.replace('(','')
            self.parsered_string = self.parsered_string.replace(')','')
            #print(self.parsered_string)

        else:
            print("Ошибка в вводе типа обрабатываемых данных")


    def find_parser(self):
        if re.search("find", self.command) and (('driver' in self.command) or ('contract' in self.command) or ('component' in self.command)):
            target = re.search("\w+\(", self.command)
            target = target[0]
            target =target.replace('(','')
            if '>' in self.command:
                self.flag = ['find', target, '>']
                self.parsered_string = re.search("(\w+[>=<]\d{4}.\d\d.\d\d)|(\w+[>=<]\w+)", self.command)
                self.parsered_string = self.parsered_string[0]
                self.parsered_string = self.parsered_string.split(self.flag[2])
            elif '=' in self.command:
                self.flag = ['find', target, '=']
                self.parsered_string = re.search("(\w+[>=<]\d{4}.\d\d.\d\d)|(\w+[>=<]\w+)", self.command)
                self.parsered_string = self.parsered_string[0]
                #print(self.parsered_string)
                self.parsered_string = self.parsered_string.split(self.flag[2])
            elif '<' in self.command:
                self.flag = ['find', target, '<']
                self.parsered_string = re.search("(\w+[>=<]\d{4}.\d\d.\d\d)|(\w+[>=<]\w+)", self.command)
                self.parsered_string = self.parsered_string[0]
                self.parsered_string = self.parsered_string.split(self.flag[2])
            else:
                print("smth wrong")
            print(self.flag)
            print(self.parsered_string)

        else:
            print("Ошибка в вводе типа обрабатываемых данных")

    def cost_parser(self):
        self.flag = ('cost',0,0)
        self.parsered_string = (re.split("\(|\)", self.command))[1]

    def components_parser(self):
        self.flag = ('components',0,0)
        self.parsered_string = (re.split("\(|\)", self.command))[1]

    def exactly_parser(self):
        action = re.match("\w+", self.command)
        #print(action[0])
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
