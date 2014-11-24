__author__ = 'art'

''' сервер '''


import socket


serv = socket.socket()
serv.bind(("127.0.0.1", 10001))
serv.listen(1)
conn, addr = serv.accept()
data = conn.recv(1024)
udata = data.decode("utf-8")
print("Data: " + udata)
while 1:
	reply = input('Enter text:')
	if reply == 'stop':
		print(reply.upper())
		conn.send(reply.encode("utf-8"))
		break
	else:
		conn.send(reply.encode("utf-8"))

conn.send(b"Hello 123!\n")
conn.send(b"Your data: " + udata.encode("utf-8"))

conn.close()