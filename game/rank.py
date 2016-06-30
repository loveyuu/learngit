# -*- coding: utf-8 -*-
from operator import itemgetter

import redis

pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
r = redis.Redis(connection_pool=pool)


def add_data():
    """
    添加测试数据
    """
    r.zadd('zz', 'zzlinbin', 75)
    r.zadd('zztime', 'zzlinbin', -10001)

    r.zadd('zz', 'zzyanyu', 90)
    r.zadd('zztime', 'zzyanyu', -10010)

    r.zadd('zz', 'zzzhangjian', 75)
    r.zadd('zztime', 'zzzhangjian', -10000)

    r.zadd('zz', 'zzshaoxiaoyu', 85)
    r.zadd('zztime', 'zzshaoxiaoyu', -10028)

    r.zadd('zz', 'zzliushuo', 85)
    r.zadd('zztime', 'zzliushuo', -10025)

    r.zadd('zz', 'zzjijialu', 85)
    r.zadd('zztime', 'zzjijialu', -10046)

    r.zadd('zz', 'zzqzc', 75)
    r.zadd('zztime', 'zzqzc', -9999)

    r.zadd('zz', 'zzshaoxiaoshu', 100)
    r.zadd('zztime', 'zzshaoxiaoshu', -10036)

    r.zadd('zz', 'zznike', 59)
    r.zadd('zztime', 'zznike', -10036)


def get_rank(conn, score_key, time_key, rank_limit):
    """
    按积分排名, 积分相同按达到积分时间戳排，时间越少, 越靠前
    :param conn: redis连接
    :param score_key: 存储积分的键
    :param time_key: 存储达到某个积分的时间的键
    :param rank_limit: 排名范围
    :return: [(name, score),]
    """
    if not isinstance(conn, redis.Redis):
        raise Exception
    a = conn.zrevrange(
        score_key, 0, rank_limit - 1, withscores=True)  # 前n名分数列表
    max_score, min_score = a[0][1], a[-1][1]  # 最高分, 最低分

    b = conn.zrevrangebyscore(
        score_key, max_score, min_score, withscores=True)  # 范围在最高和最低范围内的列表
    if len(a) == len(b):
        if len(set([s for _, s in a])) == len(a):
            return a
        else:
            k = [(n, conn.zscore(score_key, n), conn.zscore(time_key, n))
                 for n, _ in a]
            g = sorted(k, key=itemgetter(1, 2), reverse=True)
            return [(n, s) for n, s, _ in g]
    else:
        c = [(n, conn.zscore(score_key, n), conn.zscore(time_key, n))
             for n, s in b]
        p = sorted(c, key=itemgetter(1, 2), reverse=True)
        return [(n, s) for n, s, _ in p][:rank_limit]


if __name__ == "__main__":
    import cProfile

    add_data()
    cProfile.run("get_rank(r, 'zz', 'zztime', 7)")
