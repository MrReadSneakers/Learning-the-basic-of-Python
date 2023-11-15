import unittest
from parser import StringParser



class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.pars = StringParser()

    def test_print_parser(self):
        command1 = ('print.driver()')
        self.pars.exactly_parser(command1)
        self.assertEqual(self.pars.control, ('print', 'driver', 'all'))
        self.assertEqual(self.pars.parsered_string, None)

        command2 = 'print.contract(SOT110)'
        self.pars.exactly_parser(command2)
        self.assertEqual(self.pars.control, ('print', 'contract', 'exactly'))
        self.assertEqual(self.pars.parsered_string, ('SOT110'))

    def test_add_parser(self):
        command1 = ('add.component_driver(SOT111: RC1-1, RC2-2, RC3-3, RC4-4, RC5-5)')
        self.pars.exactly_parser(command1)
        self.assertEqual(self.pars.control, ('add', 'component_driver', 'SOT111'))
        self.assertEqual(self.pars.parsered_string, ('RC1', '1', 'RC2', '2', 'RC3', '3', 'RC4', '4', 'RC5', '5'))

        command2 = ('add.driver_contract(five: RC1-1, RC2-2, RC3-3, RC4-4, RC5-5)')
        self.pars.exactly_parser(command2)
        self.assertEqual(self.pars.control, ('add', 'driver_contract', 'five'))
        self.assertEqual(self.pars.parsered_string, ('RC1', '1', 'RC2', '2', 'RC3', '3', 'RC4', '4', 'RC5', '5'))

        command3 = ('add.component(name=fgf502, price=159)')
        self.pars.exactly_parser(command3)
        self.assertEqual(self.pars.control, ('add', 'component'))
        self.assertEqual(self.pars.parsered_string, ('fgf502','159'))

        command4 = ('add.contract(name=five, contract_date=2012/10/12, deadline=2022/10/10)')
        self.pars.exactly_parser(command4)
        self.assertEqual(self.pars.control, ('add', 'contract'))
        self.assertEqual(self.pars.parsered_string, ('five', '2012/10/12', '2022/10/10'))

        command5 = ('add.driver(name=SOT100, power=100, voltage_min=90, voltage_max=170, current=700, protection=IP20)')
        self.pars.exactly_parser(command5)
        self.assertEqual(self.pars.control, ('add', 'driver'))
        self.assertEqual(self.pars.parsered_string, ('SOT100', '100', '90', '170', '700', '20'))


    def test_del_parser(self):
        """в parsered_string передаются имя элемента на удаление"""
        command1 = ('del.driver(SOT140)')
        self.pars.exactly_parser(command1)
        self.assertEqual(self.pars.control, ('del', 'driver'))
        self.assertEqual(self.pars.parsered_string, ('SOT140'))

    def test_find_parser(self):
        """в parsered_string передаются параметр строки, по которой ведется поиск и собственно
        цель поиска"""
        command1 = ('find.component(price=90)')
        self.pars.exactly_parser(command1)
        self.assertEqual(self.pars.control, ('find', 'component', '='))
        self.assertEqual(self.pars.parsered_string, ('price','90'))

    def test_cost_parser(self):
        """ в данной функии все равно на control, поскольку ее вариативноть крайне мала,
        так что тут проверяем только parsered_string
        т.о. передается только имя заказа"""
        command1 = ('cost(two)')
        self.pars.exactly_parser(command1)
        self.assertEqual(self.pars.parsered_string, ('two'))

    def test_components_parser(self):
        """ в данной функии все равно на control, поскольку ее вариативноть крайне мала,
        так что тут проверяем только parsered_string
        т.о. передается только имя драйвера"""
        command1 = ('components(SOT109)')
        self.pars.exactly_parser(command1)
        self.assertEqual(self.pars.parsered_string, ('SOT109'))



if __name__ == '__main__':
    unittest.main()

"""
Проделанный путь в поиске обшибок:
- понял что однотипные переменные command и parsered_string периодически возвращают разные типы. Решил привести к одному --> кортеж.
"""