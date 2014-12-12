#!/usr/bin/env python3

""" Database configuration file. """

from sqlalchemy import Integer, String

dev_names = ['dev1', 'dev2', 'dev3']

parameters = {'time': Integer,
              'param1': Integer,
              'param2': String,
              'param3': Integer,
              'param4': Integer,
              'param5': String,
              }

dev_parameters = {'dev1': ['param1', 'param2', 'param3'],
                  'dev2': ['param4', 'param5', 'param3'],
                  'dev3': ['param1', 'param2', 'param3']}

test_values = [1, '2', 3]
type_db = 'sqlite:///'
path_db = 'databases/test.db'
test_database_name = type_db + path_db
