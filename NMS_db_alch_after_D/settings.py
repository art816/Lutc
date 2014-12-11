#!/usr/bin/env python3

""" Database configuration file. """

from sqlalchemy import Integer, String

table_names = ['dev1', 'dev2', 'dev3']
parameters = [['param1', Integer], ['param2', String], ['param3', Integer]]
values = [1, 2, 3]
test_database_name = 'sqlite:///databases/test.db'
