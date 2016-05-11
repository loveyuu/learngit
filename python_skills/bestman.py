# encoding=utf-8
"""
I love python, I love life
"""
from collections import defaultdict


def login(username=None, password=None):  # 解包
    if (username, password) == ('linbin', 'lin1234'):
        return 'login success'
    return 'login failed, please check it again'


def logout(**kwargs):  # 装包
    if (kwargs.get('username'), kwargs.get('password')) == ('linbin', 'lin1234'):
        return 'logout success'
    return 'logout failed, please check it again'

data1 = {'username': 'linbin', 'password': 'lin1234'}
data2 = {'username': 'linbin', 'password': 'lin1235'}

print login(**data2)  # 解包

print logout(**data2)  # 装包
#  纯粹的语法糖而已,简单高效的写代码

#  列表推导式, 简单明了高效, 推荐使用
print [i for i in xrange(100) if i % 2]  # 筛选出奇数

# 数据源
stu_data = [
    [1, 12202710, 'linbin', 'lin1234'],
    [2, 12202713, 'yanyu', 'wutai666'],
    [3, 12202745, 'jintian', 'qwer123'],
]


# bean
class Student(object):
    def __init__(self, number=0, name=None, password=None):  # 函数参数使用默认值是很好的习惯
        self.number = number
        self.name = name
        self.password = password

# 封装
d = dict((stu[0], Student(*stu[1:])) for stu in stu_data if stu[0] % 2)  # 列表推导式与解包的结合
print d

# 字典
book_lib = [('linbin', 'A'), ('yanyu', 'B'), ('linbin', 'C')]
books = {}
for author, book_name in book_lib:
    books.setdefault(author, []).append(book_name)  # 免除了if判断
else:
    print books

# 总结数目
salary_all = defaultdict(int)
day1 = {'linbin': 30, 'yanyu': 500, 'shaoxiaoyu': 80}
day2 = {'linbin': 10, 'yanyu': 50, 'shaoxiaoyu': 600}
day3 = {'linbin': 30, 'yanyu': 450}
day4 = {'linbin': 100, 'yanyu': 50, 'shaoxiaoyu': 70}


def do(*salary_dics):
    for salary_dic in salary_dics:
        for name, salary in salary_dic.iteritems():
            salary_all[name] += salary
a = [day1, day2, day3, day4]
do(*a)
print salary_all

#  __getitem__(), __setitem__妙用,非常优雅


class Career(object):
    def __init__(self):
        self.bags = {}

    def __getitem__(self, item):
        return self.bags.get(item)

    def __setitem__(self, key, value):
        self.bags[key] = value

    def __len__(self):
        return len(self.bags)
ca = Career()
ca[1002] = 'dao'
ca[1003] = 'jian'
print ca[1003]
print len(ca)
