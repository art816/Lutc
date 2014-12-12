#!/usr/bin/env python3

""" Sqlalchemy nms db manager. """

import sqlalchemy
from sqlalchemy import Table, Column, Integer, String,\
    MetaData, ForeignKey, create_engine
from sqlalchemy.engine import reflection
import settings as cnf


class DatabaseManager():
    def __init__(self, database_name):
        self.engine = create_engine(database_name, echo=True)
        # self.con = self.engine.connect()
        self.metadata = MetaData()

    # [param_01_name, Integer], []  []
    # PRIVATE
    def create_table(self, name, parameters):
        columns = [Column('time', Integer, primary_key=True)]
        for param_name in parameters:
            columns.append(Column(param_name, cnf.parameters[param_name]))
        Table(name, self.metadata, *columns)
        self.metadata.create_all(self.engine)
        # return self.metadata

    def create_db(self, devices):
        for dev in devices.values():
            self.create_table(dev.name, dev.parameters)

    # TODO: do we need this?
    def read_table_from_db(self, table_name):
        try:
            table = Table(table_name, self.metadata, autoload=True,
                          autoload_with=self.engine)
            return table
        except sqlalchemy.exc.NoSuchTableError:
            print("table with name {} not exist".format(table_name))
            # return 0

    # TODO: rename to open_db
    def read_all_table_from_db(self):
        ''' all data save in self.metadata '''
        # TODO: comment - where is data?
        # meta = MetaData()
        self.metadata.reflect(bind=self.engine)
        # insp = reflection.Inspector.from_engine(self.engine)
        # print(insp.get_table_names())

    # TODO: private, rename vElues
    def insert(self, table_name, column_velues):
        table = self.metadata.tables[table_name]
        conn = self.engine.connect()
        conn.execute(table.insert(), column_velues)
        conn.close()

    # TODO: write this
    def save_data(self, name, parameters, values):
        self.metadata.tables[name].insert(parameters[0], values[0])

    def get_devices_last_parameters(self):
        pass

    def get_devices_parameters(self, device_name, parameter_name, begin_t, end_t):
        pass

    def get_last_online(self):
        pass

    # TODO:
    # 1. public and private methods.
    # 2. pylint - program to autocheck code for pep8
    # 3. open NMS,
    # 3.1 find Devices, Parameter creation. devices.py, parameters.py
    # 3.2 insert them in test.py
    # 3.3 insert various parameter values.
