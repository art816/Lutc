__author__ = 'art'


s = 1


class A(object):
    a = 1


if __name__ == "__main__":
    import sys
    print(sys.argv[:])
    if len(sys.argv) > 1:
        print(sys.argv)