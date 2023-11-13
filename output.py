import sqlite3 as sq

class OutputManager():
    "Класс, работающий с выводом информации"

    def __init__(self, flag, parsered_string):
        self.flag = flag
        self.parsered_string = parsered_string


    # описание функуии, осуществляющей вывод информации из документа
    def print_BD(self):
        with sq.connect("DB.db") as con:
            cur = con.cursor()

        if self.flag[2] == 0:
            request = "SELECT * FROM '{}'".format(self.flag[1], )
            cur.execute(request)
            #cur.execute("SELECT * FROM driver")
        else:
            request = "SELECT * FROM '{}' WHERE name = '{}'".format(self.flag[1], self.parsered_string)
            cur.execute(request)
            #cur.execute("SELECT * FROM driver WHERE name = ?", (self.parsered_string,))

        rows = cur.fetchall()
        match self.flag[1]:
            case 'driver':
                for row in rows:
                    print('name = ' + row[1] + ', power =', row[2], ', voltage_min =', row[3], ', voltage_max =',
                          row[4], ', current =', row[5], ', protection = IP', row[6])
            case 'component':
                for row in rows:
                    print('name = ' + row[1] + ', price =', row[2])
            case 'contract':
                for row in rows:
                    print('name = ' + row[1] + ', contract_date =', row[2], ', deadline =', row[3])


    # описание функуии, осуществляющей поиск по БД
    def find_BD(self):
        with sq.connect("DB.db") as con:
            cur = con.cursor()

        request = "SELECT * FROM '{}' WHERE {} {} '{}'".format(self.flag[1],self.parsered_string[0],self.flag[2],self.parsered_string[1])
        cur.execute(request)

        rows = cur.fetchall()
        match self.flag[1]:
            case 'driver':
                for row in rows:
                    print('name = ' + row[1] + ', power =', row[2], ', voltage_min =', row[3], ', voltage_max =', row[4],', current =', row[5], ', protection = IP', row[6])
            case 'component':
                for row in rows:
                    print('name = ' + row[1] + ', price =', row[2])
            case 'contract':
                for row in rows:
                    print('name = ' + row[1] + ', contract_date =', row[2], ', deadline =', row[3])


    def cost_BD(self):
        with sq.connect("DB.db") as con:
            cur = con.cursor()

        request = ("SELECT contract.name = '{}', driver_contract.count, component.price FROM contract "
                   "JOIN driver_contract, component_driver, component ON contract.contract_id=driver_contract.contract_id "
                   "AND driver_contract.driver_id=component_driver.driver_id AND component_driver.component_id=component.component_id").format(self.parsered_string, )
        cur.execute(request)
        rows = cur.fetchall()
        total_price = 0
        for row in rows:
            if row[0] != 0:
                total_price += row[1]*row[2]
        print('Стоимость заказа составила: ', total_price)

        #SELECT contract.name, contract.contract_id, driver_contract.contract_id, driver_contract.driver_id, driver_contract.count,     component_driver.driver_id, component_driver.component_id, component.component_id, component.price FROM contract
        #JOIN driver_contract, component_driver, component ON contract.contract_id=driver_contract.contract_id AND driver_contract.driver_id=component_driver.driver_id AND component_driver.component_id=component.component_id


    def components_BD(self):
        with sq.connect("DB.db") as con:
            cur = con.cursor()

        request = (("SELECT driver.name = '{}', component.name, component_driver.count FROM driver "
                   "JOIN component_driver, component ON driver.driver_id=component_driver.driver_id "
                    "AND component.component_id=component_driver.component_id")
                   .format(self.parsered_string, ))
        #SELECT driver.name, component.name, component_driver.count FROM driver
        #JOIN component_driver, component ON driver.driver_id=component_driver.driver_id AND component.component_id=component_driver.component_id
        cur.execute(request)
        rows = cur.fetchall()
        for row in rows:
            if row[0] != 0:
                print('Наименование: ', row[1], ', количество: ', row[2])
