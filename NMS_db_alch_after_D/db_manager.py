#!/usr/bin/env python3

""" Sqlalchemy nms db manager. """

import sqlalchemy
from sqlalchemy import Table, Column, Integer, String,\
    MetaData, ForeignKey, create_engine
from sqlalchemy.engine import reflection


class DatabaseManager():

    def __init__(self, database_name):
        self.engine = create_engine(database_name, echo=True)
        # self.con = self.engine.connect()
        self.metadata = MetaData()

    # [param_01_name, Integer], []  []
    def create_db(self, name, parameters):
        columns = [Column('time', Integer, primary_key=True)]
        for param in parameters:
            columns.append(Column(param[0], param[1]))
        table = Table(name, self.metadata, *columns)
        self.metadata.create_all(self.engine)
        return self.metadata

    def read_table_from_db(self, table_name):
        try:
            table = Table(table_name, self.metadata, autoload=True,
                          autoload_with=self.engine)
            return table
        except sqlalchemy.exc.NoSuchTableError:
            print("table with name {} not exist".format(table_name))
            # return 0

    def read_all_table_from_db(self):
        # TODO: comment - where is data?
        # meta = MetaData()
        self.metadata.reflect(bind=self.engine)
        # insp = reflection.Inspector.from_engine(self.engine)
        # print(insp.get_table_names())

    def insert(self, table_name, column_velues):
        table = self.metadata.tables[table_name]

        conn = self.engine.connect()
        conn.execute(table.insert(), column_velues)
        conn.close()

    def save_data(self, name, parameters, values):
        self.metadata.tables[name].insert(parameters[0], values[0])

    def get_devices_last_parameters(self):
        pass

    def get_devices_parameters(self):
        pass

    def get_last_online(self):
        pass

