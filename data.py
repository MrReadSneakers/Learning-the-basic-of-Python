import re   # подключение библиотеки для поиска по документу

class DataManager():
    "Класс, работающий с управлением данными"

    def __init__(self, command):
        self.command = command

    # описание функции, удаляющей информацию про указанный драйвер
    def del_line(self):
        if re.search('SOT\d+', self.command):
            target = re.search('\w+\d+', self.command)
            lines = []
            with open('INFO', 'r') as f:
                lines = f.readlines()
                for line in lines:
                    if line.find(target[0]) != -1:
                        lines.remove(line)
                        print("Данные удалены")

            with open('INFO', 'w') as f:
                f.writelines(lines)
        else:
            print("Некорректный ввод данных")

    # описание функуии, добавляющей данные в документ документу
    def add_line(self):
        name = re.search('name=SOT\d+', self.command)
        price = re.search('price=\d+', self.command)
        power = re.search('power=\d+', self.command)
        voltage_min = re.search('voltage_min=\d+', self.command)
        voltage_max = re.search('voltage_max=\d+', self.command)
        current = re.search('current=\d+', self.command)
        protection = re.search('protection=IP\d+', self.command)
        if (name and price and power and voltage_min and voltage_max and current and protection) == None:
            print("error")
        else:
            new_str = name[0] + ', ' + price[0] + ', ' + power[0] + ', ' + voltage_min[0] + ', ' + voltage_max[0] + ', ' + current[0] + ', ' + protection[0]
            voltage_min = voltage_min[0].replace('voltage_min=', '')
            voltage_max = voltage_max[0].replace('voltage_max=', '')
            #print(name[0], voltage_min, voltage_max)
            flag = 1
            lines = []

            with open('INFO', 'r') as f:
                lines = f.readlines()
                for line in lines:
                    if (name[0] in line) or (int(voltage_min) > int(voltage_max)):
                        print('Некорректные данные: найдено совпадение или перепутаны значения напряжений')
                        flag = 0
                        break

            if flag == 1:
                with open('INFO', 'a') as f:
                    new_str = new_str + '\n'
                    f.write(new_str)
                print("Данные добавлены")