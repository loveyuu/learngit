# encoding=utf-8
import random
from operator import itemgetter


data = {'a': 400, 'b': 300, 'c': 200, 'd': 100}


def weighted_choice(weights=None, times=1):
    """
    抽奖函数
    :param weights: {id : 权值}
    :param times: 抽奖次数
    :return:抽中的id的迭代器
    """
    weights = weights or {}
    _data = sorted(weights.items(), key=itemgetter(1))

    vv = [v for _, v in _data]

    for t in xrange(0, times):
        rnd = random.random() * sum(vv)
        for i, w in enumerate(vv):
            rnd -= w
            if rnd < 0:
                yield _data[i][0]
                break

wc = weighted_choice(data, 2000)
s = 0
for c in wc:
    if c == 'a':
        s += 1

print s / 2000.0
