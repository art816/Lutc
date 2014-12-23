#!/usr/bin/env python3

""" Sqlalchemy nms db manager. """

import sqlalchemy
from sqlalchemy import Table, Column, Integer, String, \
    MetaData, ForeignKey, create_engine, select, asc, between
from sqlalchemy.engine import reflection
import settings as cnf
import device_mock


class DatabaseOperator():
    ''' методы базы данных'''

    def __init__(self, database_name):
        ''' Создаем подключение к базе данных.
            Инициализируем метаданные.
            database_name - имя базы данных
        '''
        self.engine = create_engine(database_name, echo=False)
        # self.con = self.engine.connect()
        self.metadata = MetaData()

    def create_table(self, name, parameters):
        ''' Создание одной таблицы в базе данных.
            Вся информация о созданной таблице сохраняется в метаданных.
            name - имя таблицы
            parameters - словарь из имет столбцов и типов значений
        '''
        columns = [Column('time', Integer, primary_key=True)]
        for param in parameters:
            columns.append(Column(param.name, param._type))
        Table(name, self.metadata, *columns)
        self.metadata.create_all(self.engine)
        # return self.metadata

    def create_db(self, devices):
        ''' Создание таблиц соответстующих девайсам
            devices - девайс для которого создается таблица
        '''
        for dev in devices.values():
            self.create_table(dev.name, dev.parameters)

    # TODO: do we need this?
    def read_table_from_db(self, table_name):
        ''' Получить данные о таблице с именем table_name.
            Вся информация о полученной таблице сохраняется в метаданных
            Функция возвращает объект таблицы если она существует или None иначе
            table_name - имя таблица информацию о который мы хотим получить
        '''
        try:
            table = Table(table_name, self.metadata, autoload=True,
                autoload_with=self.engine)
            return table
        except sqlalchemy.exc.NoSuchTableError:
            print("table with name {} not exist".format(table_name))

    # TODO: rename to open_db
    def read_all_table_from_db(self):
        ''' Получить данные о всех таблицах в базе данных.
            вся информация о таблицах сохраняется в метаданных.
            all data save in self.metadata
        '''
        self.metadata.reflect(bind=self.engine)

    # TODO: private, rename vElues
    def insert(self, table_name, column_values):
        ''' Сохранить запись в таблице.
            table_name - имя таблицы куда будем писать
            column_values - словарь из имен имен параметров и значений параметров
        '''
        table = self.metadata.tables[table_name]
        conn = self.engine.connect()
        conn.execute(table.insert(), column_values)
        conn.close()

    def get_devices_last_parameters(self):
        pass

    def get_devices_parameters(self, device_name, parameter_name, begin_t,
                               end_t):
        pass

    def get_last_online(self):
        pass

    def delete_database(self):
        ''' Удалить все дынные из базы дынных
            стереть метаданные
        '''
        self.metadata.drop_all(bind=self.engine)
        self.metadata.clear()

    #TODO подумать об этой функции, можно сделать через metadata
    def get_all_tables(self, database_name=None):
        ''' Возвращает емена всех существующих таблиц
            в базе данных database_name
        '''
        if database_name:
            insp = reflection.Inspector.from_engine(create_engine(database_name,
                                                                  echo=True))
        else:
            insp = reflection.Inspector.from_engine(self.engine)
        table_name = insp.get_table_names()
        return table_name

    @staticmethod
    def parser(time, given_devices):
        ''' Переделать словарь (имя: объект класса)
            в словарь (имя: значение параметра
            возвращает словарь (имя: словарь).
        '''
        table_name_column_values_dict = {}

        if type(given_devices) == dict:
            for device in given_devices.values():
                # params = list(device.params_dict.values())
                # print('\nszdfdfreaf', type(device), '\n')
                params = device.parameters
                # print('\nparams', type(params), '\n')
                column_values_dict = {param.name: param.value for param in params}
                column_values_dict['time'] = time
                table_name_column_values_dict[device.name] = column_values_dict
            return table_name_column_values_dict

        elif type(given_devices) == device_mock.Device:
            params = given_devices.parameters
            column_values_dict = {param.name: param.value for param in params}
            column_values_dict['time'] = time
            table_name_column_values_dict[given_devices.name] = column_values_dict
            return table_name_column_values_dict

        elif type(given_devices) == list or type(given_devices) == tuple:
            for device in given_devices:
                if type(device) == device_mock.Device:
                    params = device.parameters
                    column_values_dict = {param.name: param.value for param in params}
                    column_values_dict['time'] = time
                    table_name_column_values_dict[device.name] = column_values_dict
                else:
                    print('PARSER from SAVE_DATA\n что за херню ты мне передаешь???')
                    return
            return table_name_column_values_dict

        else:
            print('PARSER from SAVE_DATA\n что за херню ты мне передаешь???')

    def save_data(self, time, given_devices):
        ''' Сохранить данные о девайсах в соответствующих таблицах.
            time - полученое время формата инт.
            given_devices - полученные объекты устройств (словарь (имя: девайс)).
        '''
        tablename_column_values_dict = self.parser(time, given_devices)
        for device_name in tablename_column_values_dict:
            self.insert(device_name, tablename_column_values_dict[device_name])

    # TODO: table_name->device_name
    def get_parameter_of_device(self, table_name, column_name=None,
                                begin_time=None, end_time=None):
        ''' Получить все значения из колонок с именами из списка column_name
            из таблицы table_name.
        '''

        conn = self.engine.connect()
        # TODO: remove this.
        try:
            table = self.metadata.tables[table_name]
        except KeyError:
            print('don`t exists table with name ', table_name)
            print('exists table name\n', self.get_all_tables())
            return

        if column_name:
            try:
                list_table = [table.columns[column] for column in column_name]
            except KeyError:
                print('exists column name in table ', table_name)
                exist_column_name = set(self.get_column_name(table_name))
                print(list(exist_column_name))
                print('but you use ', column_name)
                print('column names ', set(column_name) - exist_column_name,
                'don`t exist')
                return
        else:
            list_table = [table.columns[column] for column in
                          table.columns.keys()]

        if begin_time and end_time:
            rows_with_data = conn.execute(select(list_table).
                where(between(table.columns['time'], begin_time, end_time)))
        elif begin_time:
            rows_with_data = conn.execute(select(list_table).
                where(table.columns['time'] >= begin_time))
        elif end_time:
            rows_with_data = conn.execute(select(list_table).
                where(table.columns['time'] <= end_time))
        else:
            rows_with_data = conn.execute(select(list_table))
        return rows_with_data

    def get_column_name(self, table_name):
        ''' Получить имена всех колонок в таблице table_name. '''
        table = self.metadata.tables[table_name]
        return table.columns.keys()

    def get_time_interval(self, table_name):
        ''' Получить временной интервал из таблицы с именем table_name. '''
        conn = self.engine.connect()
        table = self.metadata.tables[table_name]
        rows_with_data = conn.execute(select([table.columns.time]).
            order_by(asc(table.columns.time)))
        row_list = [row for row in rows_with_data]
        return (row_list[0][0], row_list[-1][0])


        # TODO:
        # 1. public and private methods.
        # 2. pylint - program to autocheck code for pep8
        # 3. open NMS,
        # 3.1 find Devices, Parameter creation. devices.py, parameters.py
        # 3.2 insert them in test.py
        # 3.3 insert various parameter values.
