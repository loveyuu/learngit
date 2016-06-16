# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 14:46:33 2016

@author: linbin
"""
import time
import bisect


activity_time_dic = {
    101: ('2016-06-16 11:40:00', '2016-06-16 12:00:00',
          '2016-06-16 13:00:00', '2016-06-16 13:30:00'),
    102: ('2016-05-16 11:40:00', '2016-05-16 12:00:00',
          '2016-05-16 13:00:00', '2016-05-16 13:30:00'),
}


def trans(x):
    return time.mktime(time.strptime(x, "%Y-%m-%d %H:%M:%S"))


def get_time(time_list=None):
    time_list = time_list or []
    return [trans(v) for v in time_list]


def refresh():
    """
    返回经过刷新的活动的id以及状态
    """
    result, out_date = [], []
    for k, v in activity_time_dic.iteritems():
        _time_list = get_time(v)
        flag = bisect.bisect_left(_time_list, time.time())
        if flag < 4:
            result.append((k, flag))
        else:
            out_date.append(k)
    if out_date:  # 判断是否有过期活动
        for k in out_date:  # 遍历过期活动list
            del activity_time_dic[k]  # 删除过期活动
    return result


if __name__ == '__main__':
    import cProfile

    cProfile.run("refresh()")
