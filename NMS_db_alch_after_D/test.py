#!/usr/bin/env python3

""" Testing database interface. """

__author__ = 'art'

import unittest
import os
import time
from sqlalchemy import create_engine, select, Integer

import db_manager
import settings as cnf
import device_mock


class TestDeviceMock(unittest.TestCase):
    def test_devices_create(self):
        devices = device_mock.create_devices()
        assert devices, 'got: {}'.format(devices)
        assert 'dev1' in devices


class TestDatabaseManagerPrimitive(unittest.TestCase):
    def tearDown(self):
        try:
            os.remove(cnf.path_db)
        except FileNotFoundError:
            print('FileNotFoundError.', cnf.path_db, 'not exists')
    def test_create_table(self):
        db_manage = db_manager.DatabaseManager(cnf.test_database_name)
        test_table_name = 'test_table'
        test_table_columns = ['param1', 'param2']
        db_manage.create_table(test_table_name, test_table_columns)

        existing_table_names = []
        for table in db_manage.metadata.sorted_tables:
            existing_table_names.append(table.name)
        existing_table_names.sort()
        exp_table_names = ['test_table']

        assert existing_table_names == exp_table_names, 'cant create db.\n' \
            ' tables existing={}, expected={}'.format(existing_table_names,
                                                      exp_table_names)
        table_columns = list(db_manage.metadata.tables['test_table'].columns.keys())
        exp_table_columns = ['time']
        exp_table_columns.extend(test_table_columns)
        assert table_columns == exp_table_columns, \
                'got: {} exp:{}'.format(table_columns, exp_table_columns)


class TestDatabaseManager(unittest.TestCase):

    def setUp(self):
        self.db_manage = db_manager.DatabaseManager(cnf.test_database_name)
        self.devices = device_mock.create_devices()
        self.db_manage.create_db(self.devices)
    # for every test separated
    def tearDown(self):
        try:
            os.remove(cnf.path_db)
        except FileNotFoundError:
            print('FileNotFoundError.', cnf.path_db, 'not exists')

    # @classmethod
    # def setUpClass(cls):
    #   cls.xx = 124
    # for all tests!
    # def tearDownClass(self):

    def test_create_db(self):
        existing_table_names = []
        for table in self.db_manage.metadata.sorted_tables:
            existing_table_names.append(table.name)

        existing_table_names.sort()
        exp_table_names = sorted(cnf.dev_names)

        assert existing_table_names == exp_table_names, 'cant create db.\n' \
            ' tables existing={}, expected={}'.format(existing_table_names,
                                                      exp_table_names)

    def test_read_table_from_db(self):
        dev_name = cnf.dev_names[0]
        table = self.db_manage.read_table_from_db(dev_name)
        assert table is not None

        existing_tablename = table.name
        existing_namecolumns = table.columns.keys()
        namecolumns = ['time']
        namecolumns.extend(cnf.dev_parameters[dev_name])
        # TODO: split asserts to 2.
        assert sorted(namecolumns) == sorted(existing_namecolumns) and \
            existing_tablename == dev_name, \
            'cant read db tables\n existing name={} namecolumns={}\n ' \
            'expected name={} namecolums={}'.\
            format(existing_tablename, existing_namecolumns,
                   dev_name, namecolumns)

    def test_read_all_tables_from_db(self):
        self.db_manage.read_all_table_from_db()

        all_table_name = []
        for table in self.db_manage.metadata.tables:
            all_table_name.append(table)

        assert sorted(all_table_name) == sorted(cnf.dev_names),\
            'cant read all tables db\n exists table name={}\n expected table_names={}'\
            .format(all_table_name, cnf.dev_names)

    def test_insert(self):
        dev_name = cnf.dev_names[0]
        column_values_dict = {param: value for param, value in zip(cnf.dev_parameters[dev_name],
                                                                   cnf.test_values)}
        column_values_dict['time'] = int(time.time())
        self.db_manage.insert(dev_name, column_values_dict)

        # get object table with name table_name
        table = self.db_manage.metadata.tables[dev_name]
        # connect to database
        conn = self.db_manage.engine.connect()
        # get data from table
        rows_with_data = conn.execute(select([table]))
        for row in rows_with_data:
            print(row)

        rows_with_data.close()
        conn.close()
        param_values = list(row)
        param_values = param_values[1:]
        assert param_values == cnf.test_values, \
            'Insert. Not equal exists data:{} expected data:{}'\
            .format(param_values, cnf.test_values)


if __name__ == '__main__':
    unittest.main()
