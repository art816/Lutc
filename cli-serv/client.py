__author__ = 'art'

''' клиент '''


import socket
import pickle
import time
import struct


import settings as cfg
import sys
sys.path.append('../create_db')
import create_db as lite

class MonDB:
    db_filename = 'DB'

    def __init__(self):
        self.db = []
        self.cache_new = []
        self.cache_all = []

    # def __iter__(self):
    #     self.cache_new = []

    def load(self):
        try:
            self.db = open(self.db_filename, mode='rb')
        #     self.db = open(self.db_filename, mode='rb')
        #     i = 1
        #     line1 = []
        #     for line in self.db:
        #         line1.append(line)
        #         # print(line1)
        #         print(pickle.dumps(line1))
        #         # for n in range(1, 10)
        #         if i+1 % n == 0 and i != 0:
        #             line1 = []
        #         i += 1
        #         self.cache_all = pickle.loads(line)
        #         print(self.cache_all)

            self.cache_all = pickle.load(self.db)###########
            #     self.cache_all = struct.unpack('@', self.db.read())

                    # print(i)
        except FileNotFoundError:
            print("LOAD: FILE DB NOT FOUND")
            self.db = open(self.db_filename, mode='wb')
            self.db.close()
            self.db = open(self.db_filename, mode='rb')
        # # except :
        # #     print('все сломалось начальника [create]')
        # finally:
        #     self.db.close()

        return self.cache_all

    def add(self, new_data):
        try:
            self.cache_new.append(new_data)################
            # self.cache_new = new_data
            # self.db = open(self.db_filename, mode='ab')
            # self.cache_new = pickle.dumps(new_data)
            # self.db.write(new_data)
            # self.db.write(b"\n")
        except:
            print('все сломалось начальника [add_save]')
        # finally:
        #     self.db.close()
        return 1

    def refresh(self):
        self.cache_all.append(self.cache_new)
        return self.cache_all

    def save(self):
        try:
            self.db = open(self.db_filename, mode='ab')
                            # self.cache_all = pickle.load(self.db)
            pickle.dump(self.cache_all, self.db)
        except :
            print('все сломалось начальника [save]')
            return None
        finally:
            self.db.close()
        return self.cache_all


def connect_cl(data_base):
    cl = socket.socket()
    cl.connect(("127.0.0.1", cfg.PORT))
    cl.send(b"Hello gay!\n")
    cl.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    data = cl.recv(cfg.MAX_SEND_SIZE)
    # packet_cnt = 0
    while data:
        time.sleep(cfg.CLIENT_SEND_INTERVAL)
        if cl.send(b"need data\n"):
            data = cl.recv(cfg.MAX_SEND_SIZE)
            print('Client: getting data...')
            if data:
                data_base.add(pickle.loads(data))# было вот так data_base.add(pickle.loads(data))
                lite.create_db(pickle.loads(data))
        else:
            print("разрыв связи\n")
            break
        # if max_packets and packet_cnt >= max_packets:
        #     print('max packet limit reached. exit.')
        #     break
        # packet_cnt += 1
    cl.close()

def main():
    data_base = MonDB()
    connect_cl(data_base)
    data_base.load()
    data_base.refresh()
    data_base.save()
    lite.look_db()


if __name__ == '__main__':
    main()
