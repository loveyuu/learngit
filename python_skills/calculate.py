# encoding=utf-8
"""
计算战斗力，百分比属性与固定值属性
"""
from time import sleep, time

FLAG = 1


def pro_sum(sequence):
    sleep(len(sequence)*0.1)
    return sum(sequence)


class Career(object):

    def __init__(self, attr_last=None):
        self.ph = [100, 200]
        self.ph_per = [0.3, 0.2, 0.5]
        self.t_ph = []
        self.t_ph_per = []
        self.attr_last = attr_last or {}

    def calculate(self):
        if not self.attr_last:
            x, y = pro_sum(self.ph), pro_sum(self.ph_per)
        else:
            _ph = self.attr_last.get('ph', 0)
            _ph_per = self.attr_last.get('ph_per', 0)
            x, y = _ph + pro_sum(self.t_ph), _ph_per + pro_sum(self.t_ph_per)
        a = int(x * (1 + y))
        if FLAG:
            self.set_attr_last(x, y)
            self.clear_t()
        return a

    def clear_t(self):
        del self.t_ph[:]
        del self.t_ph_per[:]

    def set_attr_last(self, k, v):
        self.attr_last['ph'] = k
        self.attr_last['ph_per'] = v

s = time()
c = Career()
for i in xrange(10):
    if i % 2:
        c.ph.append(100)
        c.t_ph.append(100)
        print c.calculate()
    else:
        c.ph_per.append(0.1)
        c.t_ph_per.append(0.1)
        print c.calculate()

print time() - s

"""
用缓存     不用缓存
630-------630
840-------840
880-------880
1100------1100
1150------1150
1380------1380
1440------1440
1680------1680
1750------1750
2000------2000
     耗时
1.5-------10.5010001659
"""