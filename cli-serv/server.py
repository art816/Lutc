__author__ = 'art'

''' сервер '''


import psutil
import sys
import socket
import pickle
import time

import settings as cfg


def tuple_data():
    data = []
    data.append(time.time())
    data.append(psutil.cpu_times_percent())
    data.append(psutil.swap_memory())
    return tuple(data)


def connect_sv(max_packets=0):
    with socket.socket() as serv_sock:
        serv_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        serv_sock.bind(("", cfg.PORT))
        serv_sock.listen(cfg.NUMBER_OF_CLIENTS)
        conn, addr = serv_sock.accept()
        conn.settimeout(cfg.SERV_WAIT_TIMEOUT)
        data = conn.recv(cfg.MAX_SEND_SIZE)
        udata = data.decode("utf-8")
        print("Data: " + udata)
        conn.send(b"Hay\n")
        packet_cnt = 0
        while conn.recv(cfg.MAX_SEND_SIZE):
            send_data = tuple_data()
            pick = pickle.dumps(send_data)
            print(len(pick))
            packet_cnt += 1
            if max_packets and packet_cnt >= max_packets:
                print('max packet limit reached. exit.')
                break
            if not conn.send(pick):
                print("разрыв связи")
                break
            print('Server: sending data...')
        conn.close()


def main():
    if len(sys.argv) > 1:
        connect_sv(int(sys.argv[1]))
    else:
        connect_sv(10)


if __name__ == '__main__':
    main()
