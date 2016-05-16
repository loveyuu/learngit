# encoding=utf-8
def check_is_admin(f):
    def wrapper(*args, **kwargs):
        if kwargs.get('username') != 'admin':
            raise Exception('you are not admin')
        return f(*args, **kwargs)
    return wrapper


class Store2(object):

    def __init__(self, x=None):
        self.x = {} if x is None else x

    @check_is_admin
    def get_food(self, **kwargs):
        food = kwargs.get('food')
        return self.x.get(food)

    @check_is_admin
    def put_food(self, **kwargs):
        food = kwargs.get('food')
        num = kwargs.get('num')
        self.x[food] = num

s2 = Store2()
s2.put_food(username='admin', food='apple', num=3)
print s2.get_food(username='admin', food='apple')
