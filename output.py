import re   # подключение библиотеки для поиска по документу

class OutputManager():
    "Класс, работающий с выводом информации"

    def __init__(self, command):
        self.command = command

    # описание функуии, осуществляющей вывод информации из документа
    def print_line(self):
        # вывод информации для конкретного драйвера
        if re.search('SOT\d+', self.command):
            target = re.search('\w+\d+', self.command)
            lines = []
            with open('INFO', 'r') as f:
                lines = f.readlines()
                for line in lines:
                    if line.find(target[0]) != -1:
                        print(line)

        # вывод информации по всем драйверам, содержащимся в документе
        elif re.match('print\(\)', self.command):
            with open('INFO', 'r') as f:
                print(*f)

        # проверка на правильность введенного названия
        else:
            print("Некорректный ввод данных")


    # описание функуии, осуществляющей поиск по документу
    def find_line(self):
        if re.search('\w+[>=<]\w+', self.command):

            f = open('INFO', 'r')

            # name = re.search('name=SOT\d+',command)
            target = re.search('\w+[>=<]\w+', self.command)
            target = target[0]
            lines = f.readlines()

            if '=' in target:
                for line in lines:
                    # поиск совпадений в строке
                    # if target or name[0] in line:
                    if target in line:
                        print(line)


            elif '<' in target:

                target = target.split('<')

                for line in lines:
                    prog = re.compile(target[0] + '[=]\w+')
                    result = prog.search(line)
                    # print(prog)
                    # print(result)

                    result = result[0]
                    result = result.split('=')
                    # print(result[0])
                    # print(result[1])

                    if 'IP' in result[1] and target[1]:
                        result[1] = result[1].replace('IP', '')
                        target[1] = target[1].replace('IP', '')
                        # print("Correct work")

                    if 'SOT' in result[1] and target[1]:
                        result[1] = result[1].replace('SOT', '')
                        target[1] = target[1].replace('SOT', '')
                        # print("Correct work")

                    # поиск совпадений в строке
                    if (target[0] in line) and (int(result[1]) < int(target[1])):
                        print(line)


            elif '>' in target:
                target = target.split('>')

                for line in lines:
                    prog = re.compile(target[0] + '[=]\w+')
                    result = prog.search(line)
                    # print(prog)
                    # print(result)
                    result = result[0]
                    result = result.split('=')
                    # print(result[0])
                    # print(result[1])

                    if 'IP' in result[1] and target[1]:
                        result[1] = result[1].replace('IP', '')
                        target[1] = target[1].replace('IP', '')
                        # print("Correct work")

                    if 'SOT' in result[1] and target[1]:
                        result[1] = result[1].replace('SOT', '')
                        target[1] = target[1].replace('SOT', '')
                        # print("Correct work")

                    # поиск совпадений в строке
                    if (target[0] in line) and (int(result[1]) > int(target[1])):
                        print(line)


            else:
                print('Ашыпка')  # все равно не существует условия, при котором это выведется, но потом убрать

            f.close()

        else:
            print('Некорректный ввод команды')