# -*- coding: utf-8 -*-
import MySQLdb
from DBUtils.PersistentDB import PersistentDB
"""
加载游戏数据到内存中，此类数据一般固定不变
但是在游戏中使用频繁，根据数据库表自动生成对象存在内存中
"""


class _Model(object):

    def __init__(self, dic):
        self.__dict__.update(dic)

    def __getattr__(self, item):
        if item not in self.__dict__:
            raise AttributeError()
        else:
            setattr(self, item, None)
        return self.item


def ta_name(name):
    name_list = list(name)

    def action(nl):
        for v in nl:
            if 65 <= ord(v) <= 90:
                v = '_' + v
            yield v
    return ''.join(action(name_list))[1:].lower()


class _Manager(object):

    @classmethod
    def dict_all(cls):
        return cls.find_all("select * from {0}".format(ta_name(cls.__name__)))

    @staticmethod
    def find_all(sql):
        cur = conn.cursor()
        cur.execute(sql)
        column_names = [d[0] for d in cur.description]
        for row in cur:
            yield _Model(dict(zip(column_names, row)))

#  数据库连接池
persist = PersistentDB(MySQLdb, maxusage=5, init_command='set names utf8',
                       host='192.168.100.243', user='root', passwd='abcd.1234',
                       db='dj3_cdbgame')
conn = persist.connection()


def test():
    class MCareer(_Manager):  # 类名与数据库表对应，自定规则
        pass
    s = MCareer.dict_all()
    for i in s:
        print i.name


if __name__ == '__main__':
    import cProfile
    cProfile.run("test()")  # 测试性能
