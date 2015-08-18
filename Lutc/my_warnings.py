__author__ = 'art'

X = 99

def selector():
    import __main__
    print(dir())
    print(dir(__main__))
    X = 77
    print(X)

def saver(x=[1,2]): # Объект списка сохраняется
    x.append(1) # При каждом вызове изменяется один и тот же объект!
    print(x)

if __name__ == '__main__':
    selector()