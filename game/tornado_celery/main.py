# -*- coding: utf-8 -*-
"""
非常高兴把这个tornado结合celery结合起来了，能跑通，并且有了不阻塞的效果
redis有点坑爹，最好不要用，rabbitq比较好，很出色
"""
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.httpclient
import tornado.gen
import tornado.escape

import tasks
from base import BaseHandle

import tcelery
tcelery.setup_nonblocking_producer()


class ZhihuHandler(BaseHandle):

    @tornado.gen.coroutine
    def get(self):
        url = 'https://api.douban.com/v2/book/1220562'
        response = yield tornado.gen.Task(tasks.require_douban.apply_async,
                                          args=[url])
        r_data = tornado.escape.json_decode(response.result)
        self.write(r_data)


class AddHandle(BaseHandle):

    @tornado.gen.coroutine
    def get(self):
        response = yield tornado.gen.Task(tasks.add.apply_async,
                                          args=[300, 700])
        self.write(str(response.result))


if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[
        (r"/zhihu", ZhihuHandler), (r"/add", AddHandle)])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(8887)
    tornado.ioloop.IOLoop.instance().start()
