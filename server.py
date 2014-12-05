__author__ = 'art'

''' сервер '''


import psutil
import socket
import pickle
import time


def tuple_data():
	data = []
	data.append(time.time())
	data.append(psutil.cpu_times_percent())
	data.append(psutil.swap_memory())
	# cl.send(pickle.dumps((, cpu_times, swap_memory)))
	return tuple(data)


def connect_sv():
	# print("awedfawefawefawefawef")
	serv = socket.socket()
	serv.bind(("127.0.0.1", 10001))
	serv.listen(1)
	conn, addr = serv.accept()
	conn.settimeout(5)
	data = conn.recv(1024)
	udata = data.decode("utf-8")
	print("Data: " + udata)
	conn.send(b"Hay\n")
	# data = conn.recv(1024)
	while conn.recv(1024):
		# if reply == 'stop':
		# 	print(reply.upper())
		# 	conn.send(reply.encode("utf-8"))
		# 	break
		# else:
		# if conn.send(reply.encode("utf-8")):
		# 	data = conn.recv(1024)
		# 	if data:
				# print(dir(pickle.loads(data)))
		if conn.send(pickle.dump(tuple_data())):
			pass
		else:
			prinf("разрыв связи")
			break
	conn.close()
