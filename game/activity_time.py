# -*- coding: utf-8 -*-
import time
import datetime
import json
import bisect

import redis

pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
r = redis.Redis(connection_pool=pool)


def date2timestamp(_time=None):
    _time = () if _time is None else _time
    _date = datetime.datetime(*_time)
    timestamp = int(time.mktime(_date.timetuple()))
    return timestamp


def check_data(*times_tuple):
    if sorted(times_tuple) == list(times_tuple):
        return True


def analyze_activity(act_id):
    act_id = str(act_id)
    if act_id in r.hkeys('activity_time'):
        now = int(time.time())
        time_dic = json.loads(r.hget('activity_time', act_id))
        time_line = sorted(time_dic.values())
        return bisect.bisect_left(time_line, now)


def add_activity(act_id=0, preview=None, start=None,
                 end=None, reward=None):
    preview_time = date2timestamp(preview)
    start_time = date2timestamp(start)
    end_time = date2timestamp(end)
    reward_time = date2timestamp(reward)
    if check_data(preview_time, start_time, end_time, reward_time):
        date_dumps = json.dumps(dict(preview_time=preview_time,
                                     start_time=start_time,
                                     end_time=end_time,
                                     reward_time=reward_time))
        r.hset('activity_time', act_id, date_dumps)
        if not 2 <= analyze_activity(act_id) < 4:
            print '刷新数据'


add_activity(act_id=101,
             preview=(2016, 06, 30, 16, 21),
             start=(2016, 06, 30, 16, 21),
             end=(2016, 06, 30, 19, 21),
             reward=(2016, 06, 30, 19, 24),
             )

print r.hgetall('activity_time')

print analyze_activity(101)

# 0：未达到预览时间
# 1：达到预览时间，但未开始
# 2：开始，未结束
# 3：领奖时间
# 4: 领奖结束
