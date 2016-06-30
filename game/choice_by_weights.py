# -*- coding: utf-8 -*-
import random
from operator import itemgetter


data_choice = {'a': 400, 'b': 300, 'c': 200, 'd': 100}


def weighted_choice(data=None, times=1):
    """
    抽奖函数
    :param data: {id : 权值}
    :param times: 抽奖次数
    :return:抽中的id的迭代器
    """
    data = data or {}
    _data = sorted(data.items(), key=itemgetter(1))

    weights = [v for _, v in _data]

    for t in xrange(0, times):
        rnd = random.random() * sum(weights)
        for i, w in enumerate(weights):
            rnd -= w
            if rnd < 0:
                yield _data[i][0]
                break

wc = weighted_choice(data_choice, 2000)
t_a, t_b, t_c, t_d = 0, 0, 0, 0
for c in wc:
    if c == 'a':
        t_a += 1
    elif c == 'b':
        t_b += 1
    elif c == 'c':
        t_c += 1
    else:
        t_d += 1

print t_a / 2000.0
print t_b / 2000.0
print t_c / 2000.0
print t_d / 2000.0
