import unittest
#from multiprocessing import Process
from threading import Thread
import time

import server
import client
import pickle
import settings as cfg
import sys
sys.path.append('../create_db')
import create_db as lite

class TestDB(unittest.TestCase):

    def test_basic(self):
        DB = client.MonDB()
        res = DB.add(pickle.dumps('efgw'))
        assert res, '{}'.format('не удалось записать в db')
        res = DB.load()
        # print(res)
        assert res, '{}'.format('не удалось считать db')
        res = DB.refresh()
        assert res, '{}'.format('не удалось обновить db')
        res = DB.save()
        assert res, '{}'.format('не удалось сохранить db')


    def test_basic_network_communication(self):
        """ """
        DB = client.MonDB()
        store_send_interval = cfg.CLIENT_SEND_INTERVAL
        cfg.CLIENT_SEND_INTERVAL = 0.01
        packets = 10
        serv_proc = Thread(target=server.connect_sv, args=(packets,))
        cl_proc = Thread(target=client.connect_cl, args=(DB,))
        serv_proc.start()
        time.sleep(2)
        cl_proc.start()
        serv_proc.join()
        cl_proc.join()
        cfg.CLIENT_SEND_INTERVAL = store_send_interval

        lite.look_db()


if __name__ == '__main__':
    unittest.main()
