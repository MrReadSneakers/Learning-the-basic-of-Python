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