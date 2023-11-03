from parser import StringParser

print("Перечень возможных действий:\ndel() - удаление записи\nadd() - создание новой записи\nprint() - вывод записи\nfind() - поиск информации")
print("Escape - завершение работы\nИные действия будут восприняты как некорректные.\n")

# проверка на наличие документа с заданнм именем, если такового нет, то создаст, но перезапишет если таковой уже существует
try: f = open('INFO')
except: f = open('INFO','w')
f.close()


#проверка на корректность ввода команды и переход в функцию ее выполняющую
#придумать как это написать через case
while True:
    command = input("Введите команду: ")
    StringParser(command).parser()
    StringParser(command).exactly_parser()
