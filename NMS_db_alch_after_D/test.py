#!/usr/bin/env python3

""" Testing database interface. """

__author__ = 'art'

import unittest
import os
import time

from sqlalchemy import select

import db_manager
import settings as cnf
import device_mock


# @unittest.skip('not work')
class TestDeviceMock(unittest.TestCase):
    ''' тест модуля device_mock '''

    def test_devices_create(self):
        """ создаются девайсы с параметрами из фаила settings """

        devices = device_mock.create_devices()
        assert devices, 'got: {}'.format(devices)
        assert 'dev1' in devices

    def test_create_one_device(self):
        """ создается один девайс с передоваемыми параметрами
        type находится из соответствия parameters в фаиле settings"""

        test_table_name = 'test_table'
        test_table_columns = ['param1', 'param2']
        devices = device_mock.create_one_device(test_table_name,
                                                test_table_columns)
        assert devices, 'got: {}'.format(devices)


class TestDatabaseManagerPrimitive(unittest.TestCase):
    ''' тестирование db_manager
    функция create_table в этом модуле тестируется отдельно так как
    необходима пустая база данных для ее тестирования
    '''

    def setUp(self):
        ''' создание подключения к базе данных и инициализация метаданных'''
        self.db_manage = db_manager.DatabaseOperator(cnf.test_database_name)

    def tearDown(self):
        ''' удаляем фаил с базой данных'''

        try:
            os.remove(cnf.path_db)
        except FileNotFoundError:
            print('FileNotFoundError.', cnf.path_db, 'not exists')

    def test_create_table(self):
        ''' создание одной таблицы
        предварительно создается один девайс device_mock.create_one_device
        создается таблица с его именем и параметрами
        '''

        # db_manage = db_manager.DatabaseOperator(cnf.test_database_name)
        test_table_name = 'test_table'
        test_table_columns = ['param1', 'param2']
        for dev in device_mock.create_one_device(test_table_name,
                                                test_table_columns).values():
            self.db_manage.create_table(dev.name, dev.parameters)

        existing_table_names = []
        for table in self.db_manage.metadata.sorted_tables:
            existing_table_names.append(table.name)
        existing_table_names.sort()
        exp_table_names = ['test_table']

        assert existing_table_names == exp_table_names, 'cant create db.\n' \
            'tables existing={}, expected={}'.format(existing_table_names,
                                                     exp_table_names)
        table_columns = list(
            self.db_manage.metadata.tables['test_table'].columns.keys())
        exp_table_columns = ['time']
        exp_table_columns.extend(test_table_columns)
        assert table_columns == exp_table_columns, \
            'got: {} exp:{}'.format(table_columns, exp_table_columns)


class TestDatabaseManager(unittest.TestCase):
    ''' тестирование db_manager '''
    def setUp(self):
        ''' всегда создаем подключение к базе данных
        создаем все девайсы из фаила settings
        создаем таблицы соответствующие девайсам '''
        self.db_manage = db_manager.DatabaseOperator(cnf.test_database_name)
        self.devices = device_mock.create_devices()
        self.db_manage.create_db(self.devices)
        self.db_name = cnf.test_database_name

    # for every test separated
    def tearDown(self):
        ''' удаление фаила содержащего базу данных
        можно удалять только информацию о базе данных из фаила
        delete_database()'''
        self.db_manage.delete_database()
        # try:
        #     os.remove(cnf.path_db)
        # except FileNotFoundError:
        #     print('FileNotFoundError.', cnf.path_db, 'not exists')

    # @classmethod
    # def setUpClass(cls):
    # cls.xx = 124
    # for all tests!
    # def tearDownClass(self):

    def test_create_db(self):
        ''' проверка созданных имен таблиц с желаемыми значениями'''
        existing_table_names = []
        for table in self.db_manage.metadata.sorted_tables:
            existing_table_names.append(table.name)

        existing_table_names.sort()
        exp_table_names = sorted(cnf.dev_names)

        assert existing_table_names == exp_table_names, 'cant create db.\n' \
                                                        ' tables existing={}, expected={}'.format(
            existing_table_names,
            exp_table_names)

    def test_read_table_from_db(self):
        ''' получить данные о таблице с именем cnf.dev_names[0]
        сравнить полученное имя таблицы с желаемым
        сравнить существующие имена столбцов с желаемыми
        '''
        dev_name = cnf.dev_names[0]
        table = self.db_manage.read_table_from_db(dev_name)
        assert table is not None

        existing_tablename = table.name
        existing_namecolumns = table.columns.keys()
        namecolumns = ['time']
        namecolumns.extend(cnf.dev_parameters[dev_name])
        assert existing_tablename == dev_name, \
            'cant read db tables existing name={} expected name={}'\
            .format(existing_tablename, dev_name)
        assert sorted(namecolumns) == sorted(existing_namecolumns), \
            'cant read column_name existing columns={} expected columns={}'\
            .format(existing_namecolumns, namecolumns)

    def test_read_all_tables_from_db(self):
        ''' получить данные о всех таблицах существующих в базе данных
        сравнить полученные имена таблиц с желаемыми значениями
        '''
        self.db_manage.read_all_table_from_db()

        all_table_name = []
        for table in self.db_manage.metadata.tables:
            all_table_name.append(table)

        assert sorted(all_table_name) == sorted(cnf.dev_names), \
            'cant read all tables. exists table_name={} expected table_names={}' \
            .format(all_table_name, cnf.dev_names)

    def test_insert(self):
        ''' вставить данные в таблицу с именем cnf.dev_names[0]
        и проверить успешность данной операции
        '''
        dev_name = cnf.dev_names[0]
        column_values_dict = {param: value for param, value in
                              zip(cnf.dev_parameters[dev_name],
                                  cnf.test_values)}
        column_values_dict['time'] = int(time.time()*10**6)
        self.db_manage.insert(dev_name, column_values_dict)

        # get object table with name table_name
        table = self.db_manage.metadata.tables[dev_name]
        # connect to database
        conn = self.db_manage.engine.connect()
        # get data from table
        rows_with_data = conn.execute(select([table]))
        param_values = []
        for row in rows_with_data:
            param_values.append(list(row))
        rows_with_data.close()
        conn.close()
        # param_values = list(row)
        # print(param_values, '\n')
        param_values_without_time = [param[1:] for param in param_values]
        # print(param_values_without_time, '\n')
        assert cnf.test_values in param_values_without_time, \
            'Insert. Not equal exists data:{} expected data:{}' \
            .format(param_values, cnf.test_values)

    def test_delete_database(self):
        ''' удаляем все данные из базы дынных затираем метаданные'''
        self.db_manage.delete_database()
        # self.db_manage.metadata.clear()

    def test_show_tables(self):
        ''' показать имена всех существующих таблиц '''
        # self.db_manage.delete_database()
        # self.db_manage.metadata.clear()
        # all_table_name = \
        # all_table_name = self.db_manage.read_all_table_from_db()
        # print(all_table_name)
        # all_table_name = []
        # for table in self.db_manage.metadata.tables:
        #     all_table_name.append(table)
        # print(all_table_name)
        insp = self.db_manage.get_all_tables(self.db_name)
        print(insp.get_table_names())
        # assert insp

        # conn = self.db_manage.engine.connect()
        # for table_name in insp.get_table_names():
        #     print(table_name)
        #     column_name=[]
        #     for column in insp.get_columns(table_name):
        #         column_name.append(column['name'])
        #     print(' | '.join(column_name))
        # table = self.db_manage.metadata.tables['dev1']
        # rows_with_data = conn.execute(select([table]))
        # for row in rows_with_data:
        #     print(list(row))
        # assert sorted(self.db_manage.show_tables(self.db_name)) == \
        #        sorted(cnf.dev_names)


    # @unittest.skip('dont work')
    # TODO доделать assert
    def test_save_data(self):
        ''' переделать словарь (имя: объек класса)
        в словарь (имя: значение параметра'''

        curent_time = int(time.time())

        # self.db_manage.parser(curent_time, self.devices)

        self.db_manage.save_data(curent_time, self.devices)
        self.db_manage.save_data(curent_time + 20, self.devices)
        # get_interval = self.db_manage.get_time_interval(device_name)
        # assert get_interval == exp_interval, 'get:{} exp:{}'.format(
        #     get_interval, exp_interval)

    # @unittest.skip('dont work')
    def test_get_time_interval(self):
        ''' получить интервал времен из таблицы parameter_name
        и сравнить с ожидаемым
        '''
        table_name = 'dev1'
        start_time = int(time.time())
        exp_interval = (int(time.time()), int(time.time()) + 10)
        self.db_manage.save_data(start_time, self.devices)
        self.db_manage.save_data(start_time+10, self.devices)
        exist_interval = self.db_manage.get_time_interval(table_name)
        assert exp_interval == exist_interval

    def test_get_parameter_of_device(self):
        ''' Save data and then check if it loads from database. '''
        self.db_manage.save_data(int(time.time()), self.devices)
        self.db_manage.save_data(int(time.time())+10, self.devices)
        rows_with_data = self.db_manage.get_parameter_of_device('dev1',
                                                ['time', 'param1', 'param2'])

        assert rows_with_data

        for table_name in self.db_manage.get_all_tables(self.db_name):
            print(table_name)
            print(self.db_manage.get_column_name(table_name))
            # print(self.db_manage.get_parameter_of_device(table_name))
            for row in self.db_manage.get_parameter_of_device(table_name):
                print(row)
        if rows_with_data:
            for row in rows_with_data:
                print(row)
                assert row[1:] == (1, '1'), rows_with_data.close()

    def test_get_times_values(self):
        """ Get times and values from db.
            begin_t and end_t should be integ"""
        start_time = int(time.time())
        self.db_manage.save_data(start_time, self.devices)
        self.db_manage.save_data(start_time+10, self.devices)
        rows_with_data = self.db_manage.get_parameter_of_device('dev1',
                                ['time', 'param1', 'param2'], start_time, start_time+10)
        assert rows_with_data
        if rows_with_data:
            for row in rows_with_data:
                print(row)
                assert row[0] >= start_time and row[0] <= start_time+5
        # assert


if __name__ == '__main__':
    unittest.main()
