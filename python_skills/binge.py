# -*- coding: utf-8 -*-
import MySQLdb
import torndb


class _Model(object):

    def __init__(self, dic):
        self.dic = dic.iterkeys()
        self.__dict__.update(dic)

    def __getattr__(self, item):
        if item not in self.dic:
            raise AttributeError()
        else:
            setattr(self, item, None)
        return self.item


class _Manager(object):

    @classmethod
    def dict_all(cls):
        return db.ob_iter("select * from {0}".format(cls.__name__.lower()))


class CConnection(torndb.Connection):
    def ob_iter(self, query, *parameters, **kwparameters):
        self._ensure_connected()
        cursor = MySQLdb.cursors.SSCursor(self._db)
        try:
            self._execute(cursor, query, parameters, kwparameters)
            column_names = [d[0] for d in cursor.description]
            for row in cursor:
                yield _Model(torndb.Row(zip(column_names, row)))
        finally:
            cursor.close()

db = CConnection("192.168.100.243", "dj3_cdbgame", user="root", password="abcd.1234")
NAME_PASSWORD_ADDRESS_SCORE = {}


def test():
    class M_career_info(_Manager):
        pass

    s = M_career_info.dict_all()
    for i in s:
        print i.id, i.name
    # for i in s:
    #     NAME_PASSWORD_ADDRESS_SCORE[i.name] = (i.password, i.address, i.score)
    #
    # password, _, score = NAME_PASSWORD_ADDRESS_SCORE.get('linbin')
    # print password, score

if __name__ == '__main__':
    import cProfile
    cProfile.run("test()")


