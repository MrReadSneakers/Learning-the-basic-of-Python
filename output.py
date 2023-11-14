import sqlite3 as sq


class OutputManager():
    "Класс, работающий с выводом информации"

    def __init__(self, control, parsered_string):
        self.control = control
        self.parsered_string = parsered_string

    # описание функуии, осуществляющей вывод информации из документа
    def print_BD(self):
        control_comm, control_tabl, control_extra = self.control
        print(control_comm)
        print(control_tabl)
        print(control_extra)
        with sq.connect("DB.db") as con:
            cur = con.cursor()

        match self.control[2]:
            case 'all':
                request = "SELECT * FROM '{}'".format(self.control[1], )
                cur.execute(request)
            case 'exactly':
                request = "SELECT * FROM '{}' WHERE name = '{}'".format(self.control[1], self.parsered_string)
                cur.execute(request)

        rows = cur.fetchall()
        match self.control[1]:
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

        request = ("SELECT * FROM '{}' WHERE {} {} '{}'"
                   .format(self.control[1],self.parsered_string[0],self.control[2],self.parsered_string[1]))
        cur.execute(request)

        rows = cur.fetchall()
        match self.control[1]:
            case 'driver':
                for row in rows:
                    print('name = ' + row[1] + ', power =', row[2], ', voltage_min =', row[3],
                          ', voltage_max =', row[4],', current =', row[5], ', protection = IP', row[6])
            case 'component':
                for row in rows:
                    print('name = ' + row[1] + ', price =', row[2])
            case 'contract':
                for row in rows:
                    print('name = ' + row[1] + ', contract_date =', row[2], ', deadline =', row[3])

    def cost_BD(self):
        with sq.connect("DB.db") as con:
            cur = con.cursor()

        request = (("SELECT contract.name = '{}', driver_contract.count, component.price FROM contract "
                   "JOIN driver_contract, component_driver, component ON contract.contract_id=driver_contract.contract_id "
                   "AND driver_contract.driver_id=component_driver.driver_id AND component_driver.component_id=component.component_id")
                   .format(self.parsered_string, ))
        cur.execute(request)
        rows = cur.fetchall()
        total_price = 0
        for row in rows:
            if row[0] != 0:
                total_price += row[1]*row[2]
        print('Стоимость заказа составила: ', total_price)

    def components_BD(self):
        with sq.connect("DB.db") as con:
            cur = con.cursor()

        request = (("SELECT driver.name = '{}', component.name, component_driver.count FROM driver "
                   "JOIN component_driver, component ON driver.driver_id=component_driver.driver_id "
                    "AND component.component_id=component_driver.component_id")
                   .format(self.parsered_string, ))
        cur.execute(request)
        rows = cur.fetchall()
        for row in rows:
            if row[0] != 0:
                print('Наименование: ', row[1], ', количество: ', row[2])
