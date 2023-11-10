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
        #request = "SELECT rowid FROM 'contract' WHERE name = '{}'".format(self.parsered_string, )
        return_count_driver = "SELECT count FROM 'driver_contract' WHERE contract_id = (SELECT rowid FROM 'contract' WHERE name = '{}')".format(self.parsered_string, )
        cur.execute(return_count_driver)
        print(cur.fetchall())

        return_id_driver = "SELECT driver_id FROM 'driver_contract' WHERE contract_id = (SELECT rowid FROM 'contract' WHERE name = '{}')".format(self.parsered_string, )
        cur.execute(return_id_driver)
        print(cur.fetchall())

        for row in return_id_driver:
            return_count_component = "SELECT count FROM 'component_driver' WHERE driver_id = '{}'".format(row[1])
            cur.execute(return_count_component)
            print(cur.fetchall())

        return_price_component = "SELECT price FROM 'component' WHERE component_id = (SELECT component_id FROM 'component_driver' WHERE driver_id = (SELECT driver_id FROM 'driver_contract' WHERE contract_id = (SELECT rowid FROM 'contract' WHERE name = '{}')))".format(self.parsered_string, )
        cur.execute(return_price_component)
        print(cur.fetchall())


    def components_BD(self):
        pass
