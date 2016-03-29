# encoding=utf-8
import time

import tornado.ioloop
import tornado.web
import tornado.gen
import tornado.escape
from tornado.httpclient import AsyncHTTPClient


class GenAsyncHandler(tornado.web.RequestHandler):

    @tornado.gen.coroutine
    def get(self):
        http_client = AsyncHTTPClient()
        response = yield http_client.fetch("https://api.douban.com/v2/book/1220562")
        data = tornado.escape.json_decode(response.body)
        self.write(data)


class Gen2AsyncHandler(tornado.web.RequestHandler):

    @tornado.gen.coroutine
    def get(self):
        yield tornado.gen.Task(tornado.ioloop.IOLoop.instance().add_timeout, time.time() + 5)
        self.write("I sleep 5s")
