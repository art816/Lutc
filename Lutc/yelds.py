__author__ = 'art'

import sys, mytimer # Импортирует функцию timer
reps = 1000
repslist = range(reps) # Вызов функции range вынесен за пределы цикла в 2.6


def forLoop():
    res = []
    for x in repslist:
        res.append(x + 10)
    return res


def listComp():
    return [x + 10 for x in repslist]


def mapCall():
    return list(map(lambda x: x + 10, repslist)) # Вызов list необходим только в 3.0


def genExpr():
    return list(x + 10 for x in repslist) # Функция list вынуждает


def genFunc():
    def gen():
        for x in repslist:
            yield x + 10
    return list(gen())
    print(sys.version)


if __name__ == '__main__':
    for test in (forLoop, listComp, mapCall, genExpr, genFunc):
        elapsed, result = mytimer.timer(test)
        print('-' * 33)
        print('%-9s: %.5f => [%s...%s]' % (test.__name__, elapsed, result[0], result[-1]))