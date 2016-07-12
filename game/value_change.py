# encoding=utf-8
import functools


def value_check(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        char, delta = args[:2]
        n = func.__name__.split('_')[0]
        v = getattr(char, n)
        if v + delta >= 0:
            return func(*args, **kwargs)
        else:
            raise Exception("{0} is not enough".format(n))
    return wrapper


def change_log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        char, delta, change_type = args[:3]
        n = func.__name__.split('_')[0]
        v = getattr(char, n)
        _func = func(*args, **kwargs)
        print "{0} is {1}, delta is {2}, type is {3}.".format(n, v, delta, change_type)
        return _func
    return wrapper


class Character(object):

    def __init__(self, money, diamond):
        self.money = money
        self.diamond = diamond

    @change_log
    @value_check
    def money_change(self, delta=0, change_type=0):
        self.money += delta
        print 'money changed!'

    @change_log
    @value_check
    def diamond_change(self, delta=0, change_type=0):
        self.diamond += delta
        print 'diamond changed!'

c = Character(100, 20)

try:
    c.money_change(-80, 100023)
    c.diamond_change(-5, 200023)
except Exception as e:
    print 'is not enough'
finally:
    print c.money
    print c.diamond
