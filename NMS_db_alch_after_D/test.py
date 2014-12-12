#!/usr/bin/env python3

""" Testing database interface. """

__author__ = 'art'

import unittest
from sqlalchemy import create_engine
# from sqlalchemy import *
import db_manager
# db_manager
import settings as cnf
import os
from sqlalchemy import select


class TestDatabaseManager(unittest.TestCase):

    def setUp(self):
        self.db_manage = db_manager.DatabaseManager(cnf.test_database_name)
    # for every test separated
    def tearDown(self):
        os.remove(cnf.path_db)

    # @classmethod
    # def setUpClass(cls):
    #   cls.xx = 124
    # for all tests!
    # def tearDownClass(self):

    def test_create_db(self):
        print("\n\n\ntest_create_db")
        for table_name in cnf.table_names:
            self.db_manage.create_db(table_name, cnf.parameters)

        # engine = create_engine(cnf.test_database_name)
        existing_table_names = []
        for table in self.db_manage.metadata.sorted_tables:
            existing_table_names.append(table.name)
        existing_table_names.sort()
        exp_table_names = sorted(cnf.table_names)
        assert existing_table_names == exp_table_names, 'cant create'\
        'db. tables existing={}, expected={}'.format(existing_table_names,
                                                         exp_table_names)


    def test_read_table_from_db(self):
        print("\n\n\ntest_read_table_from_db")
        for table_name in cnf.table_names:
            self.db_manage.create_db(table_name, cnf.parameters)

        table_name = cnf.table_names[0]
        table = self.db_manage.read_table_from_db(table_name)
        # print(type(table), '\t', table)
        existing_namecolumns = []
        existing_tablename = []
        if table != None:
            print("table_columns=", table.columns)
            print("table_columns=", table.name)
            existing_tablename = table.name
            existing_namecolumns = (table.columns.keys())

        namecolumns = []
        for param in cnf.parameters:
            namecolumns.append(param[0])

        assert sorted(namecolumns) == sorted(existing_namecolumns) and \
            existing_tablename == table_name, \
            'cant read db tables\n existing name={} namecolumns={}\n ' \
            'expected name={} namecolums={}'.\
            format(existing_tablename, existing_namecolumns,
                table_name, namecolumns)
        # print(sorted(namecolumns), '\n', sorted(existing_namecolumns), '\n', existing_tablename, '\n', table_name )

    def test_read_all_tables_from_db(self):
        for table_name in cnf.table_names:
            self.db_manage.create_db(table_name, cnf.parameters)
        print("\n\n\ntest_read_all_table_from_db")
        self.db_manage.read_all_table_from_db()
        all_table_name = []
        for table in self.db_manage.metadata.tables:
            print("table_name=", table)
            all_table_name.append(table)

        assert sorted(all_table_name) == sorted(cnf.table_names),\
        'cant read db\n exists table name={}\n expected table_names={}'.format(
            all_table_name, cnf.table_names)

    #

    def test_insert(self):
        print("\n\n\ntest_insert")
        for table_name in cnf.table_names:
            self.db_manage.create_db(table_name, cnf.parameters)
        column_values_dict = {column_name_and_type[0]: val
                               for column_name_and_type, val in
                               zip(cnf.parameters, cnf.values)}
        # column_values = dict(zip((column_name_and_type[0]
        #                           for column_name_and_type in cnf.parameters),
        #                          cnf.values))
        print('column_values_dict=', column_values_dict)
        table_name = cnf.table_names[0]
        self.db_manage.insert(table_name, column_values_dict)


        # get object table with name table_name
        table = self.db_manage.metadata.tables[table_name]
        # print(self.db_manage.metadata.tables)
        conn = self.db_manage.engine.connect()
        # get data from table
        list_rows_with_data = conn.execute(select([table]))
        for row in list_rows_with_data:
            print(row)

        list_rows_with_data.close()
        conn.close()

        assert list(row) == cnf.values, \
            'not equal expected data and ' \
            'exists data{}\n expected data{}'.format(list(row), cnf.values)


if __name__ == '__main__':
    unittest.main()
