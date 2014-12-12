#!/usr/bin/env python3

""" Mock classes for device and parameter """


class Device:
    def __init__(self, name, parameters):
        self.name = name
        self.parameters = parameters  # list

class Parameter:
    def __init__(self, name, value):
        self.name = name
        self.value = value

def main():
    par1 = Parameter('param1', 1)
    par2 = Parameter('param2', 2)
    dev1 = Device('dev1', [par1, par2])
    # ...
    # save to db
    dm_man = DatabaseManager()
    dm_man.save([dev1])
