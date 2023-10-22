from functools import reduce


def sum(*args):
    acc = []
    result = 0

    def inner(*args):
        nonlocal result
        if len(args) == 0:
            return result
        else:
            for i in args:
                acc.append(i)
            result = reduce(lambda x, y: x+y, acc)
            return inner

    return inner(*args)


print('final sum:', sum(1, 0)(1, 1, 1)(1)(1, 1)())
