import re   # подключение библиотеки для поиска по документу

class Output():
    "Класс, работающий с выводом информации"

    def __init__(self, command):
        self.command = command

    # описание функуии, осуществляющей вывод информации из документа
    def print_line(self):
        #вывод информации для конкретного драйвера
        if re.search('SOT\d+', self.command):
            target = re.search('\w+\d+', self.command)
            f = open('INFO', 'r')

            i = 1
            while True:
                # считывание строки
                line = f.readline()

                # поиск совпадений в строке
                if target[0] in line:
                    print(line)

                i += 1  # счетчик для перехода на новую строку

                # прерывание цикла, если строка пустая (т.е. последняя)
                if not line:
                    break

            f.close()

        # вывод информации по всем драйверам, содержащимся в документе
        elif re.match('print\(\)', self.command):
            f = open('INFO', 'r')
            print(*f)
            f.close()

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

            i = 1

            if '=' in target:

                while True:
                    # считывание строки
                    line = f.readline()

                    # прерывание цикла, если строка пустая (т.е. последняя)
                    if not line:
                        break

                    # поиск совпадений в строке
                    # if target or name[0] in line:
                    if target in line:
                        print(line)

                    i += 1  # счетчик для перехода на новую строку



            elif '<' in target:
                target = target.split('<')

                while True:
                    # считывание строки
                    line = f.readline()

                    # прерывание цикла, если строка пустая (т.е. последняя)
                    if not line:
                        break

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

                    i += 1  # счетчик для перехода на новую строку



            elif '>' in target:
                target = target.split('>')

                while True:
                    # считывание строки
                    line = f.readline()

                    # прерывание цикла, если строка пустая (т.е. последняя)
                    if not line:
                        break

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

                    i += 1  # счетчик для перехода на новую строку



            else:
                print('Ашыпка')  # все равно не существует условия, при котором это выведется, но потом убрать

            f.close()

        else:
            print('Некорректный ввод команды')