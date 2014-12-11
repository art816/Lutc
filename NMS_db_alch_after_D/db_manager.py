#!/usr/bin/env python3

""" Sqlalchemy nms db manager. """

#import sqlalchemy as al
from sqlalchemy import Table, Column, Integer, String,\
    MetaData, ForeignKey, create_engine


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
        table = Table(table_name, self.metadata, autoload=True,
                      autoload_with=self.engine)
        return table

    def save_data(self, name, parameters, values):
        self.metadata.tables[name].insert(parameters[0], values[0])
        pass

    def get_devices_last_parameters(self):
        pass

    def get_devices_parameters(self):
        pass

    def open(self):

        return self.metadata

    def get_last_online(self):
        pass

