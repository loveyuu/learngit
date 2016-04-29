# encoding=utf-8
from peewee import fn

from model.student import Student, db

#  全部查询
print [(i.name, i.password, i.address, i.score) for i in Student.select()]  # select()中可以选择要查询的列

#  条件查询
print [(i.name, i.password, i.address, i.score) for i in Student.select().where(Student.name == 'yanyu')]

#  更新
query = Student.update(password='miqilin').where(Student.name == 'yanyu')
query.execute()

#  插入数据(very fast)
data_source = [
    {'name': 'python', 'password': 'py123456', 'address': 'Suzhou',    'score': 81},
    {'name': 'golang', 'password': 'go123456', 'address': 'Changzhou', 'score': 89},
    {'name': 'ruby',   'password': 'ry123456', 'address': 'Taizhou',   'score': 54},
    {'name': 'erlang', 'password': 'er123456', 'address': 'Nantong',   'score': 71},
]
with db.atomic():
    Student.insert_many(data_source).execute()

#  排序
print [i.name for i in Student.select(Student.name).order_by(Student.score)]  # 升序

print [i.name for i in Student.select(Student.name).order_by(+Student.score)]  # 升序(第二种写法)

print [i.name for i in Student.select(Student.name).order_by(Student.score.desc())]  # 降序

print [i.name for i in Student.select(Student.name).order_by(-Student.score)]  # 降序(第二种写法)

# 分组
print [(i.address, i.max) for i in Student.select(Student.address, fn.MAX(Student.score).alias('max'))
                                          .group_by(Student.address)]

# 结果
'''
[(u'asd', u'asd', u'Xinghua', 80), (u'asdds', u'asd', u'Nanjing', 67), (u'do_any_thing', u'666666', u'Shanghai', 80), (u'erlang', u'er123456', u'Nantong', 71), (u'garlurn', u'lin444', u'Nanjing', 91), (u'golang', u'go123456', u'Changzhou', 89), (u'leona', u'lin222', u'Xinghua', 72), (u'linbin', u'woshilinbin1993', u'Nanjing', 65), (u'masteryi', u'lin333', u'Nanjing', 98), (u'pansheng', u'lin222', u'Xinghua', 87), (u'python', u'py123456', u'Suzhou', 81), (u'qqq', u'ppp', u'Wuxi', 45), (u'ruby', u'ry123456', u'Taizhou', 54), (u'yanyu', u'miqilin', u'Xinghua', 80), (u'yasuo', u'lin111', u'Wuxi', 70)]
[(u'yanyu', u'miqilin', u'Xinghua', 80)]
[u'qqq', u'ruby', u'linbin', u'asdds', u'yasuo', u'erlang', u'leona', u'asd', u'do_any_thing', u'yanyu', u'python', u'pansheng', u'golang', u'garlurn', u'masteryi']
[u'qqq', u'ruby', u'linbin', u'asdds', u'yasuo', u'erlang', u'leona', u'asd', u'do_any_thing', u'yanyu', u'python', u'pansheng', u'golang', u'garlurn', u'masteryi']
[u'masteryi', u'garlurn', u'golang', u'pansheng', u'python', u'asd', u'do_any_thing', u'yanyu', u'leona', u'erlang', u'yasuo', u'asdds', u'linbin', u'ruby', u'qqq']
[u'masteryi', u'garlurn', u'golang', u'pansheng', u'python', u'asd', u'do_any_thing', u'yanyu', u'leona', u'erlang', u'yasuo', u'asdds', u'linbin', u'ruby', u'qqq']
[(u'Changzhou', 89), (u'Nanjing', 98), (u'Nantong', 71), (u'Shanghai', 80), (u'Suzhou', 81), (u'Taizhou', 54), (u'Wuxi', 70), (u'Xinghua', 87)]
'''