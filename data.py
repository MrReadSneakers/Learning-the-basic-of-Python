import sqlite3 as sq


class DataManager():
    "Класс, работающий с управлением данными"

    def __init__(self, control, parsered_string):
        self.control = control
        self.parsered_string = parsered_string

    def del_BD(self):
        with sq.connect("DB.db") as con:
            cur = con.cursor()

        match self.control[1]:
            case 'driver':
                request2 = ("DELETE FROM component_driver WHERE driver_id = (SELECT rowid FROM driver WHERE name = '{}')"
                            .format(self.parsered_string, ))
                cur.execute(request2)
                request3 = ("DELETE FROM driver_contract WHERE driver_id = (SELECT rowid FROM driver WHERE name = '{}')"
                            .format(self.parsered_string, ))
                cur.execute(request3)
            case 'contract':
                request2 = ("DELETE FROM 'driver_contract' WHERE contract_id = (SELECT rowid FROM contract WHERE name = '{}')"
                            .format(self.parsered_string, ))
                cur.execute(request2)
            case 'component':
                request2 = ("DELETE FROM 'component_driver' WHERE component_id = (SELECT rowid FROM component WHERE name = '{}')"
                            .format(self.parsered_string, ))
                cur.execute(request2)

        request1 = "DELETE FROM '{}' WHERE name = '{}'".format(self.control[1], self.parsered_string)
        cur.execute(request1)

        if cur.rowcount == 0:
            print('Данные не удалены. Скорее всего их и не было в перечне')
        else:
            print('Данные успешно удалены')

        con.commit()
        con.close()

    def add_BD(self):
        with sq.connect("DB.db") as con:
            cur = con.cursor()

        match self.control[1]:
            case 'component_driver':
                for name_component in range(int(len(self.parsered_string) / 2)):
                    request = ("INSERT INTO component_driver (driver_id, component_id, count) VALUES "
                               "((SELECT rowid FROM driver WHERE name = '{}'), "
                               "(SELECT rowid FROM component WHERE name = '{}'), {})"
                               .format(self.control[2], self.parsered_string[2 * name_component],
                                       self.parsered_string[2 * name_component + 1]))
                    cur.execute(request)

            case 'driver_contract':
                for name_component in range(int(len(self.parsered_string) / 2)):
                    request = ("INSERT INTO driver_contract (contract_id, driver_id, count) VALUES "
                               "((SELECT rowid FROM 'contract' WHERE name = '{}'), "
                               "(SELECT rowid FROM driver WHERE name = '{}'), {})"
                               .format(self.control[2], self.parsered_string[2 * name_component],
                                       self.parsered_string[2 * name_component + 1]))
                    cur.execute(request)

            case 'driver':
                # как раз таки проверка на то что добавляются уникальные
                unique = "SELECT * FROM '{}' WHERE name = '{}'".format(self.control[1], self.parsered_string[0])
                cur.execute(unique)
                if cur.fetchone() is None:
                    cur.execute(
                        "INSERT INTO driver(name, power, voltage_min, voltage_max, current, protection) "
                        "VALUES(?, ?, ?, ?, ?, ?)",
                        (self.parsered_string[0], self.parsered_string[1], self.parsered_string[2],
                         self.parsered_string[3],self.parsered_string[4], self.parsered_string[5],))
                else:
                    print('Найдено совпадение')

            case 'component':
                # как раз таки проверка на то что добавляются уникальные
                unique = "SELECT * FROM '{}' WHERE name = '{}'".format(self.control[1], self.parsered_string[0])
                cur.execute(unique)
                if cur.fetchone() is None:
                    cur.execute(
                        "INSERT INTO component(name, price) VALUES(?, ?)",
                        (self.parsered_string[0], self.parsered_string[1],))
                else:
                    print('Найдено совпадение')

            case 'contract':
                # как раз таки проверка на то что добавляются уникальные
                unique = "SELECT * FROM '{}' WHERE name = '{}'".format(self.control[1], self.parsered_string[0])
                cur.execute(unique)
                if cur.fetchone() is None:
                    request = ("INSERT INTO 'contract' (name, contract_date, deadline) VALUES('{}', '{}', '{}')"
                               .format(self.parsered_string[0], self.parsered_string[1], self.parsered_string[2],))
                    cur.execute(request)
                else:
                    print('Найдено совпадение')

        # print(cur.rowcount)
        if cur.rowcount == 1:
            print('Данные успешно добавлены')

        con.commit()
        con.close()
