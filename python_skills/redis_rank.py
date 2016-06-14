# -*- coding: utf-8 -*-
from operator import itemgetter

import redis

r = redis.Redis(host='localhost', port=6379, db=0)


def get_rank(redis_score, redis_time, conn, last_rank):
    """
    :param redis_score: 存储积分的键
    :param redis_time: 存储达到某个积分的时间的键
    :param conn: redis连接
    :param last_rank: 取前x名
    :return: [(name, score),]
    """
    if not isinstance(conn, redis.Redis):
        raise Exception
    a = conn.zrevrange(redis_score, 0, last_rank - 1, withscores=True)
    last_score = a[0][1]

    b = conn.zrevrangebyscore(redis_score, last_score, 0, withscores=True)
    if len(a) == len(b):
        if len(set([s for _, s in a])) == len(a):
            return a
        else:
            k = [(n, conn.zscore(redis_score, n), conn.zscore(redis_time, n))
                 for n, _ in a]
            g = sorted(k, key=itemgetter(1, 2), reverse=True)
            return [(n, s) for n, s, _ in g]
    else:
        c = [(n, conn.zscore(redis_score, n), conn.zscore(redis_time, n))
             for n, s in b]
        p = sorted(c, key=itemgetter(1, 2), reverse=True)
        return [(n, s) for n, s, _ in p][:last_rank]

if __name__ == "__main__":
    import cProfile

    cProfile.run("get_rank('zz', 'zztime', r, 7)")
