__author__ = 'art'

import pickle
import time

data = []
while 1:
    time.sleep(5)
    data = (time.time())
    send_data = (data,)
    pick = pickle.dumps(send_data)
    repick = pickle.loads(pick)
    print('srt==', pick, '\n')
    print('restr==', repick, '\n')
    with open('DB1', mode='ab') as f:
        f.write(pick)
        f.write(b'\n')
    with open('DB1', mode='rb') as f:
        for line in f:
            print('ln===', line, '\n')
            print('reln===', pickle.loads(line), '\n')
            time.sleep(2)
            print('newstr\n')
