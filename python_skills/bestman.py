# encoding=utf-8
"""
I love python, I love life
"""
from collections import defaultdict
import bisect
import random


def login(username=None, password=None):  # 解包
    if (username, password) == ('linbin', 'lin1234'):
        return 'login success'
    return 'login failed, please check it again'


def logout(**kwargs):  # 装包
    username = kwargs.get('username')
    password = kwargs.get('password')
    if (username, password) == ('linbin', 'lin1234'):
        return 'logout success'
    return 'logout failed, please check it again'

data1 = {'username': 'linbin', 'password': 'lin1234'}
data2 = {'username': 'linbin', 'password': 'lin1235'}

print login(**data2)  # 解包

print logout(**data2)  # 装包
#  纯粹的语法糖而已,简单高效的写代码

#  列表推导式, 简单明了高效, 推荐使用
print[i for i in xrange(100) if i % 2]  # 筛选出奇数

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
d = dict((stu[0], Student(*stu[1:]))
         for stu in stu_data if stu[0] % 2)  # 列表推导式与解包的结合
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

# 二分查找
rank = [10, 20, 40, 60, 80]
x = 5
print rank[bisect.bisect(rank, x) - 1]  # 归档时候特别好用(多少分到多少分是啥等级)

# 根据权重选择物品


def weighted_choice(weights):
	"""
	weights:权重的列表
	"""
    rnd = random.random() * sum(weights)
    for i, w in enumerate(weights):
        rnd -= w
        if rnd < 0:
            return i

print weighted_choice([1, 3, 4, 2])

class WeightedRandomGenerator(object):
    def __init__(self, weights):
        self.totals = []
        running_total = 0

        for w in weights:
            running_total += w
            self.totals.append(running_total)

    def next(self):
        rnd = random.random() * self.totals[-1]
        return bisect.bisect_right(self.totals, rnd)

    def __call__(self):
        return self.next()
# 如果我们使用同一个权重数组weights, 但是要多次得到随机结果, 
# 多次的调用weighted_choice方法, totals变量还是有必要的, 提前计算好它,
# 每次获取随机数的消耗会变得小很多, 在调用次数超过1000次的时候, 
# WeightedRandomGenerator的速度是weighted_choice的100倍,
# 所以我们在对同一组权重列表进行多次计算的时候选择方法4, 如果少于100次, 则使用方法3

#字符串
data = "linbinisgoodman"

def mando(data, step):
    start, length = 0, len(data)
    while start <= length:
        yield data[start:start+step]
        start += step

print type(mando(data, 6))  # <type 'generator'>
for i in mando(data, 6):
	print i 
#linbin
#isgood
#man
