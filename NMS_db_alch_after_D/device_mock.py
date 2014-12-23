#!/usr/bin/env python3

""" Mock classes for device and parameter """

import settings as cnf
from sqlalchemy import Integer


class Device:
    def __init__(self, name, name_rus, protocol, parameters):
        self.name = name
        self.name_rus = name_rus
        self.protocol = protocol
        self.parameters = parameters  # list
        self.params_dict = {param.name: param for param in self.parameters}

    def __repr__(self):
        return 'name = {}, name_rus = {}, protocol = {}, parameters = {}'.\
            format(self.name, self.name_rus, self.protocol, self.parameters)


class Parameter:
    def __init__(self, name, value=1, _type=None):
        self.name = name
        self.value = value
        self._type = _type
        if not self._type:
            try:
                self._type = cnf.parameters[name]
            except:
                pass

    def __repr__(self):
        return '{} = {} (type {})'.format(self.name, self.value, self._type.__name__)

def main():
    par1 = Parameter('param1', 1)
    par2 = Parameter('param2', 2)
    dev1 = Device('dev1', [par1, par2])
    # ...
    # save to db
    # dm_man = DatabaseManager()
    # dm_man.save([dev1])

def create_devices():
    ''' создаем словарь в котором имени соответствует устройство '''
    dev_dict = {}
    for dev_name in cnf.dev_names:
        dev_dict[dev_name] = create_one_device\
            (dev_name, cnf.dev_parameters[dev_name]).get(dev_name)
    return dev_dict

def create_one_device(dev_name, given_parameters):
    dev_dict = {}
    parameter = []
    for param in given_parameters:
        parameter.append(Parameter(name=param))
    dev_dict[dev_name] = Device(dev_name, '', '', parameter)
    return dev_dict




