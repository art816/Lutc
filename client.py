__author__ = 'art'

''' клиент '''


import socket
import pickle
import unittest
import time


class MonDB:
	db_filename = 'DB'

	def __init__(self):
		self.db = []
		self.cache_new = []
		self.cache_old = []

	def load(self):
		with open(self.db_filename, mode='rb') as self.db:
			try:
				self.cache_old = pickle.load(self.db)
			except:
				print('все сломалось начальника')
				return None
		return self.cache_old

	def add(self, new_data):
		self.cache_new.append(new_data)
		return self.cache_new

	def refresh(self):
		self.cache_old.append(self.cache_new)
		return self.cache_old

	def save(self):
		with open(self.db_filename, mode='wb') as self.db:
			try:
				# self.cache_all = pickle.load(self.db)
				pickle.dump(self.cache_old, self.db)
			except:
				print('все сломалось начальника')
				return None
		return self.cache_old


DB = MonDB()


class TestDB(unittest.TestCase):

	def test_basic(self):
		res = DB.load()
		assert res, '{}'.format('не удалось считать db')
		res = DB.add("efgw")
		assert res, '{}'.format('не удалось записать в db')
		res = DB.refresh()
		assert res, '{}'.format('не удалось обновить db')
		res = DB.save()
		assert res, '{}'.format('не удалось сохранить db')

# print("awedfawefawefawefawef")
# print(__name__)

def connect_cl():
	cl = socket.socket()
	cl.connect(("127.0.0.1", 10001))
	cl.send(b"Hello gay!\n")
	# cl.blind("120.0.0.1", 10001)
	# cl.listen(1)
	# data = cl.recv(1024)
	# udata = data.decode("utf-8")
	# print("Data: " + udata)
	# data = cl.recv(1024)
	# udata = data.decode("utf-8")
	# print("Data: " + udata)
	# cl.send(b"Your data: " + udata.encode("utf-8"))
	data = cl.recv(1024)
	print(data.decode("utf-8"))
	while data:
		time.sleep(3)
		if cl.send(b"need data\n"):
			data = cl.recv(1024)
			if data:
				DB.add(pickle.load(data))
		else:
			print("разрыв связи\n")
			break
	cl.close()

def main():
	DB.load()
	connect_cl()
	DB.refresh()
	DB.save()

	# DB.db.close()
	# print(DB)

	# conn.send(b"Hello 123!\n")
	# conn.send(b"Your data: " + udata.encode("utf-8"))



if __name__ == '__main__':
	# main()
	unittest.main()