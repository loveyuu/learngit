# encoding=utf-8
from operator import itemgetter


class AttrDict(dict):

    def __getattr__(self, item):
        if item in self:
            return self[item]
        raise AttributeError('{0} not found'.format(item))

    def __setattr__(self, key, value):
        self[key] = value

    def __delattr__(self, item):
        del self[item]

p = AttrDict(name='linbin')
print p.name
p.name = 'cocos2d-x'

print p.name


class StudentManager(object):

    __slots__ = ['students']

    def __init__(self, students=None):
        self.students = {} if students is None else students

    def __contains__(self, item):
        return item in self.students

stu_man = StudentManager()
stu_man.students['name'] = 'linbin'
print stu_man.students
print 'name' in stu_man

data = dict(linbin=89, yanyu=80, shaoxiaoyu=65, alex=45)
_data = sorted(data.iteritems(), key=itemgetter(1))
print _data
