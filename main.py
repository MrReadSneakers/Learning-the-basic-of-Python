import re   # подключение библиотеки для поиска по документу

print("Перечень возможных действий:\ndel() - удаление записи\nadd() - создание новой записи\nprint() - вывод записи\nfind() - поиск информации")
print("Escape - завершение работы\nИные действия будут восприняты как некорректные.\n")

# проверка на наличие документа с заданнм именем, если такового нет, то создаст, но перезапишет если таковой уже существует

try: f = open('INFO')
except: f = open('INFO','w')
f.close()


# здесь будет объявление функций
# функция, проверяющая и удаляющая ИДЕНТИЧНЫЕ строки / реализация не очень удалась
def Find_Same_Line():
    # прочесть все строчки документа в память
    f = open('INFO', 'r')
    lines = f.readlines()
    f.close()

    unique_elements = list(set(lines))  # удаление нужной строки из памяти
    #unique_elements = set(lines)  # удаление нужной строки из памяти

    # перезапись всех строк в документ из памяти, кроме удаленной
    f = open('INFO', 'w')
    f.writelines(unique_elements)
    f.close()



# функция, удаляющая ПУСТЫЕ строки
# возможно, потом удалю, она не то что бы решает поставленную задачу / реализация не очень удалась
def Dell_Empty_line():
    f = open('INFO', 'r+')
    for line in f:
        # strip() function
        if line.strip():
            f.write(line)
    f.close()


# описание функции, удаляющей информацию про указанный драйвер
def del_line(command):
    if re.search('SOT\d+', command):
        target = re.search('\w+\d+', command)
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
def add_line(command):
    name = re.search('name=SOT\d+', command)
    price = re.search('price=\d+', command)
    power = re.search('power=\d+', command)
    voltage_min = re.search('voltage_min=\d+', command)
    voltage_max = re.search('voltage_max=\d+', command)
    current = re.search('current=\d+', command)
    protection = re.search('protection=IP\d+', command)
    if (name and price and power and voltage_min and voltage_max and current and protection) == None:
        print("error")
    else:

        f = open('INFO', 'r')
        new_str = name[0] + ', ' + price[0] + ', ' + power[0] + ', ' + voltage_min[0] + ', ' + voltage_max[0] + ', ' + current[0] + ', ' + protection[0]
        voltage_min = voltage_min[0].replace('voltage_min=', '')
        voltage_max = voltage_max[0].replace('voltage_max=', '')
        print(name[0], voltage_min, voltage_max)
        i = 1
        j = 1
        while True:
            # считывание строки
            line = f.readline()

            # поиск совпадений в строке
            if (name[0] in line) or (int (voltage_min) > int (voltage_max)):
                print('Некорректные данные: найдено совпадение или перепутаны значения напряжений')
                j = 0
                break

            i += 1  # счетчик для перехода на новую строку

            # прерывание цикла, если строка пустая (т.е. последняя)
            if not line:
                break


        f.close()
        if j == 1:
            f = open('INFO', 'a')
            new_str = new_str + '\n'
            f.write(new_str)
            f.close()
            print("Данные добавлены")




# описание функуии, осуществляющей вывод информации из документа
def print_line(command):
    # вывод информации для конкретного драйвера
    if re.search('SOT\d+', command):
        target = re.search('\w+\d+', command)
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
    elif re.match('print\(\)', command):
        f = open('INFO', 'r')
        print(*f)
        f.close()

    # проверка на правильность введенного названия
    else: print("Некорректный ввод данных")


# описание функуии, осуществляющей поиск по документу
def find_line(command):
    if re.search('\w+[>=<]\w+',command):

        f = open('INFO', 'r')

        #name = re.search('name=SOT\d+',command)
        target = re.search('\w+[>=<]\w+',command)
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
                #if target or name[0] in line:
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

                prog = re.compile(target[0]+'[=]\w+')
                result = prog.search(line)
                #print(prog)
                #print(result)
                result = result[0]
                result = result.split('=')
                #print(result[0])
                #print(result[1])

                if 'IP' in result[1] and target[1]:
                    result[1] = result[1].replace('IP', '')
                    target[1] = target[1].replace('IP', '')
                    #print("Correct work")

                if 'SOT' in result[1] and target[1]:
                    result[1] = result[1].replace('SOT', '')
                    target[1] = target[1].replace('SOT', '')
                    #print("Correct work")

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

                prog = re.compile(target[0]+'[=]\w+')
                result = prog.search(line)
                #print(prog)
                #print(result)
                result = result[0]
                result = result.split('=')
                #print(result[0])
                #print(result[1])

                if 'IP' in result[1] and target[1]:
                    result[1] = result[1].replace('IP', '')
                    target[1] = target[1].replace('IP', '')
                    #print("Correct work")

                if 'SOT' in result[1] and target[1]:
                    result[1] = result[1].replace('SOT', '')
                    target[1] = target[1].replace('SOT', '')
                    #print("Correct work")

                # поиск совпадений в строке
                if (target[0] in line) and (int(result[1]) > int(target[1])):
                    print(line)

                i += 1  # счетчик для перехода на новую строку



        else:
            print('Ашыпка') #все равно не существует условия, при котором это выведется, но потом убрать


        f.close()

    else: print('Некорректный ввод команды')


#проверка на корректность ввода команды и переход в функцию ее выполняющую
#придумать как это написать через case
while True:
    command = input("Введите команду: ")
    if re.search("Escape", command): break
    elif re.match("del", command): del_line(command)
    elif re.match("add", command): add_line(command)
    elif re.match("print", command): print_line(command)
    elif re.match("find", command): find_line(command)
    else:
        print("Некорректный ввод команды")

    #Find_Same_Line()
    #Dell_Empty_line()
