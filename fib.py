#!D:\Program Files\Python python
__author__ = 'art'

def fib(max):
	a, b = 0, 1
	while a < max:
		yield a
		a, b = b, a + b


def main():
	for n in fib(1E100):
		print(n, end='\n')

if __name__ == '__main__':
	main()



