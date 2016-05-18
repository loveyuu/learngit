# encoding=utf-8
from functools import wraps

data = ['diit']


def log(text):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if kwargs.get('name') not in data:
                raise Exception('username not in data')
            print "call %s() %s" % (func.__name__, text)
            return func(*args, **kwargs)
        return wrapper
    return decorator


@log('doit')
def now(name=None):
    print '2016-5-18', name


@log('doit')
def show(x, y, name=None):
    print '2016-5-18', x, y, name

try:
    show(100, 200, name='iit')
except Exception, e:
    print e

try:
    now(name='diit')
except Exception, e:
    print e
