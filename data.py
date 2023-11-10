import re   # подключение библиотеки для поиска по документу
import sqlite3 as sq

class DataManager():
    "Класс, работающий с управлением данными"

    def __init__(self, flag, parsered_string):
        self.flag = flag
        self.parsered_string = parsered_string

    def del_BD(self):
        with sq.connect("DB.db") as con:
            cur = con.cursor()

        match self.flag[1]:
            case 'driver':
                request2 = "DELETE FROM component_driver WHERE driver_id = (SELECT rowid FROM driver WHERE name = '{}')".format(self.parsered_string, )
                cur.execute(request2)
                request3 = "DELETE FROM driver_contract WHERE driver_id = (SELECT rowid FROM driver WHERE name = '{}')".format(self.parsered_string, )
                cur.execute(request3)
            case 'contract':
                request2 = "DELETE FROM 'driver_contract' WHERE contract_id = (SELECT rowid FROM contract WHERE name = '{}')".format(self.parsered_string, )
                cur.execute(request2)
            case 'component':
                request2 = "DELETE FROM 'component_driver' WHERE component_id = (SELECT rowid FROM component WHERE name = '{}')".format(self.parsered_string, )
                cur.execute(request2)

        request1 = "DELETE FROM '{}' WHERE name = '{}'".format(self.flag[1], self.parsered_string)
        cur.execute(request1)

        con.commit()
        con.close()


    def add_BD(self):
        with sq.connect("DB.db") as con:
            cur = con.cursor()

        #не забыть сделать проверку на то что добавляются только уникальные
        match self.flag[1]:
            case 'component_driver':
                for name_component in range(int(sum(1 for _ in self.parsered_string)/2)):
                    request = ("INSERT INTO component_driver (driver_id, component_id, count) VALUES ((SELECT rowid FROM driver WHERE name = '{}'), "
                               "(SELECT rowid FROM component WHERE name = '{}'), {})"
                               .format(self.flag[2], self.parsered_string[2 * name_component], self.parsered_string[2 * name_component + 1]))
                    cur.execute(request)
            case 'driver_contract':
                for name_component in range(int(sum(1 for _ in self.parsered_string)/2)):
                    request = ("INSERT INTO driver_contract (contract_id, driver_id, count) VALUES ((SELECT rowid FROM 'contract' WHERE name = '{}'), "
                               "(SELECT rowid FROM driver WHERE name = '{}'), {})"
                               .format(self.flag[2], self.parsered_string[2 * name_component], self.parsered_string[2 * name_component + 1]))
                    cur.execute(request)
            case 'driver':
                cur.execute(
                    "INSERT INTO driver(name, power, voltage_min, voltage_max, current, protection) VALUES(?, ?, ?, ?, ?, ?)",
                    (self.parsered_string[0], self.parsered_string[1], self.parsered_string[2], self.parsered_string[3],
                     self.parsered_string[4], self.parsered_string[5],))
            case 'component':
                cur.execute(
                    "INSERT INTO component(name, price) VALUES(?, ?)",
                    (self.parsered_string[0], self.parsered_string[1],))
            case 'contract':
                request = "INSERT INTO 'contract' (name, contract_date, deadline) VALUES('{}', '{}', '{}')".format(self.parsered_string[0], self.parsered_string[1], self.parsered_string[2],)
                cur.execute(request)
                #cur.execute(
                #    "INSERT INTO driver('name', 'contract_date', 'deadline') VALUES(?, ?, ?)",
                #    (self.parsered_string[0], self.parsered_string[1], self.parsered_string[2],))
        con.commit()
        con.close()

