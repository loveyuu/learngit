# -*- coding: utf-8 -*-
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.gen


import tornadoredis

from redis_base import RedisBaseHandle


class ActivityHandle(RedisBaseHandle):

    @tornado.gen.coroutine
    def get(self):
        name = yield tornado.gen.Task(self.redis.hgetall, 'data')
        self.write(name)


if __name__ == "__main__":
    tornado.options.parse_command_line()

    conn = tornadoredis.Client()
    conn.connect()
    # conn.hset("data", "linbin", "Shanghai")
    # conn.hset("data", "xuyangyang", "Nanjing")
    # conn.hset("data", "jijialu", "NanTong")

    settings = {
        'redis': conn,
    }
    app = tornado.web.Application(handlers=[(r"/", ActivityHandle), ], **settings)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
