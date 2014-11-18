#!/usr/bin/env python3

import sys
import re

def ip_host(ip_host_f):
    ''' соответствие ip и имени host'''
    line_number = 0
    #ipPattern = re.compile(r'^(\d+.\d+.\d+.\d+)*(\b\w+)$')
    #ipPattern = re.compile(r'^(\d+.\d+.\d+.\d+).*[\t|\ ](\w+[.\w]*)$')
    #ipPattern = re.compile(r'^(\d+.\d+.\d+.\d+)([[\t|\ ].*[\t|\ ]]|[\t|\ ])(\w+[\W\w+]*)$')
    ipPattern = re.compile(r'^(\d+.\d+.\d+.\d+).*[\t|\ ](\w+[\W\w+]*)$')
    with open(ip_host_f) as a_file:
        for a_line in a_file:
            line_number += 1
            a_rez=ipPattern.match(a_line.rstrip())
            #a_rez=ipPattern.search('1.2.3.4  \t\t\   gfdfgdfgs sfgsdf')
            try:
                print('\t',a_rez.groups()[0],'\t',a_rez.groups()[1])
            except AttributeError:  # Nothing found.
                pass
                #print(len(a_rez.groups()))
            #print(a_line.rstrip())
            #print(line_number)


if len(sys.argv)!=2:
    print('первый аргумент путь к фаилу')
else:
    #f = open(argv[1]).read()
    #ip_host(f)
    ip_host(sys.argv[1])
    


    


