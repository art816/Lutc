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
        # db_manage = db_manager.DatabaseManager(cnf.test_database_name)
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

    #def test_save(self):
    #    DB = DB_manager.DatabaseManager(cnf.database)
    #    DB.save_data(name, parameters, values)
    #    pass

    def test_read_table_from_db(self):
        # db_manage = db_manager.DatabaseManager(cnf.test_database_name)
        print("\n\n\ntest_read_table_from_db")
        table = self.db_manage.read_table_from_db('dev1')
        if table:
            print("table_columns=", table.columns)

    def test_read_all_tables_from_db(self):
        print("\n\n\ntest_read_all_table_from_db")
        self.db_manage.read_all_table_from_db()
        for table in self.db_manage.metadata.tables:
            print("table_name=", table)
    #

    def test_insert(self):
        print("\n\n\ntest_insert")
        for table_name in cnf.table_names:
            self.db_manage.create_db(table_name, cnf.parameters)
        # x = {column_name_and_type[0]: val for column_name_and_type, val zip(cnf.parameters, cnf.values)}
        column_values = dict(zip((column_name_and_type[0]
                                  for column_name_and_type in cnf.parameters),
                                 cnf.values))
        table_name = cnf.table_names[0]
        self.db_manage.insert(table_name, column_values)

        # WTF?
        table = self.db_manage.metadata.tables[table_name]
        conn = self.db_manage.engine.connect()
        # WTF?
        res = conn.execute(select([table]))
        for data in res:
            print(data)

        res.close()
        conn.close()





if __name__ == '__main__':
    unittest.main()
