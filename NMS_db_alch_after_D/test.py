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
    '''Тест модуля device_mock.'''

    def test_devices_create(self):
        """Создаются девайсы с параметрами из фаила settings."""
        devices = device_mock.create_devices()
        assert devices, 'got: {}'.format(devices)
        assert 'dev1' in devices

    def test_create_one_device(self):
        """Создается один девайс с передоваемыми параметрами
           type находится из соответствия parameters в фаиле settings.
        """
        test_table_name = 'test_table'
        test_table_columns = ['param1', 'param2']
        devices = device_mock.create_one_device(test_table_name,
                                                test_table_columns)
        assert devices, 'got: {}'.format(devices)


class TestDatabaseManagerPrimitive(unittest.TestCase):
    ''' Тестирование db_manager.
        Функция create_table в этом модуле тестируется отдельно так как
        необходима пустая база данных для ее тестирования
    '''

    def setUp(self):
        ''' Создание подключения к базе данных и инициализация метаданных.'''
        self.db_manage = db_manager.DatabaseOperator(cnf.test_database_name)

    def tearDown(self):
        ''' Удаляем фаил с базой данных.'''
        try:
            os.remove(cnf.path_db)
        except FileNotFoundError:
            print('FileNotFoundError.', cnf.path_db, 'not exists')

    def test_create_table(self):
        ''' Создание одной таблицы.
            Предварительно создается один девайс device_mock.create_one_device
            создается таблица с его именем и параметрами.
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
    ''' Тестирование db_manager '''
    def setUp(self):
        ''' Всегда создаем подключение к базе данных.
            Создаем все девайсы из фаила settings.
            Создаем таблицы соответствующие девайсам
        '''
        self.db_manage = db_manager.DatabaseOperator(cnf.test_database_name)
        self.devices = device_mock.create_devices()
        self.db_manage.create_db(self.devices)
        self.db_name = cnf.test_database_name

    def tearDown(self):
        ''' Удаление фаила содержащего базу данных.
            Можно удалять только информацию о базе данных из фаила
            delete_database().
        '''
        self.db_manage.delete_database()

    def test_create_db(self):
        ''' Проверка созданных имен таблиц с желаемыми значениями.'''
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
        ''' Получить данные о таблице с именем cnf.dev_names[0].
            Сравнить полученное имя таблицы с желаемым.
            Сравнить существующие имена столбцов с желаемыми.
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
        ''' Получить данные о всех таблицах существующих в базе данных.
            Сравнить полученные имена таблиц с желаемыми значениями.
        '''
        self.db_manage.read_all_table_from_db()

        all_table_name = []
        for table in self.db_manage.metadata.tables:
            all_table_name.append(table)

        assert sorted(all_table_name) == sorted(cnf.dev_names), \
            'cant read all tables. exists table_name={} expected table_names={}' \
            .format(all_table_name, cnf.dev_names)

    def test_insert(self):
        ''' Вставить данные в таблицу с именем cnf.dev_names[0]
            и проверить успешность данной операции.
        '''
        dev_name = cnf.dev_names[0]
        column_values_dict = {param: value for param, value in
                              zip(cnf.dev_parameters[dev_name],
                                  cnf.test_values)}
        #TODO: temp
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
        param_values_without_time = [param[1:] for param in param_values]
        assert cnf.test_values in param_values_without_time, \
            'Insert. Not equal exists data:{} expected data:{}' \
            .format(param_values, cnf.test_values)

    def test_delete_database(self):
        ''' Удаляем все данные из базы дынных затираем метаданные.'''
        self.db_manage.delete_database()

    def test_show_tables(self):
        ''' Показать имена всех существующих таблиц. '''
        insp = self.db_manage.get_all_tables(self.db_name)
        assert set(insp) - set(cnf.dev_names) == set()

    # TODO доделать assert
    def test_save_data(self):
        ''' Сохранить данные.'''
        curent_time = int(time.time())
        self.db_manage.save_data(curent_time, self.devices)
        self.db_manage.save_data(curent_time + 20, self.devices)
        for dev_name in self.devices.keys():
            rows_with_data = self.db_manage.get_parameter_of_device(dev_name)
            assert len(rows_with_data.fetchall()) == 2

    def test_get_time_interval(self):
        ''' Получить интервал времен из таблицы parameter_name
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
        self.db_manage.save_data(int(time.time()) + 10, self.devices)
        rows_with_data = self.db_manage.get_parameter_of_device('dev1',
                                                ['time', 'param1', 'param2'])
        assert rows_with_data

        if rows_with_data:
            for row in rows_with_data:
                assert row[1:] == (1, '1'), rows_with_data.close()

    def test_get_times_values(self):
        """ Get times and values from db.
            begin_t and end_t should be integer
        """
        start_time = int(time.time())
        self.db_manage.save_data(start_time, self.devices)
        self.db_manage.save_data(start_time + 10, self.devices)
        rows_with_data = self.db_manage.get_parameter_of_device('dev1',
                                ['time', 'param1', 'param2'], start_time, start_time + 10)
        assert rows_with_data
        if rows_with_data:
            for row in rows_with_data:
                assert row[0] >= start_time and row[0] <= start_time + 10


if __name__ == '__main__':
    unittest.main()
