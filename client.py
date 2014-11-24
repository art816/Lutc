__author__ = 'art'

''' клиент '''


import socket


cl = socket.socket()
# cl.blind("120.0.0.1", 10001)
# cl.listen(1)
cl.connect(("127.0.0.1", 10001))
cl.send(b"Hello gay!\n")
data = cl.recv(1024)
udata = data.decode("utf-8")
print("Data: " + udata)
data = cl.recv(1024)
udata = data.decode("utf-8")
print("Data: " + udata)
cl.send(b"Your data: " + udata.encode("utf-8"))
while 1:
	data = cl.recv(1024)
	if data.decode("utf-8") == 'stop':
		print(data.decode("utf-8").upper())
		break
	else:
		print(data.decode("utf-8"))
cl.close()
