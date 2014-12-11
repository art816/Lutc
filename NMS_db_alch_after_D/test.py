#!/usr/bin/env python3

""" Testing database interface. """

__author__ = 'art'

import unittest
from sqlalchemy import create_engine
# from sqlalchemy import *
import db_manager
# db_manager
import settings as cnf


class TestDatabaseManager(unittest.TestCase):

    # def setUp(self):
    # for every test separated
    # def tearDown(self):
    #

    # @classmethod
    # def setUpClass(cls):
    #   cls.xx = 124
    # for all tests!
    # def tearDownClass(self):

    def test_create_db(self):
        db_manage = db_manager.DatabaseManager(cnf.test_database_name)
        for table_name in cnf.table_names:
            metadata = db_manage.create_db(table_name, cnf.parameters)

        engine = create_engine(cnf.test_database_name)
        existing_table_names = []
        for table in metadata.sorted_tables:
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

    def test_open(self):
        db_manage = db_manager.DatabaseManager(cnf.test_database_name)
        table = db_manage.read_table_from_db('dev1')
        print(table.columns)



if __name__ == '__main__':
    unittest.main()
