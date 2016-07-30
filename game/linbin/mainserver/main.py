# -*- coding: utf-8 -*-
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.httpclient
import tornado.gen
from tornado.httpclient import AsyncHTTPClient
from tornado.concurrent import run_on_executor
import tornado.escape

from mainserver.base import BaseHandle
from mainserver.db import conn


class RegisterHandler(BaseHandle):

    @tornado.gen.coroutine
    def get(self):
        username = self.get_argument('username')
        password = self.get_argument('password')
        uid = yield self.register(username, password)
        self.write(dict(uid=uid))

    @run_on_executor(executor="thread_pool")
    def register(self, username, password):
        return conn.insert(
            "insert into user (username, password) values(%s, %s)",
            username,
            password,
        )


class LoginHandler(BaseHandle):

    @tornado.gen.coroutine
    def get(self):
        username = self.get_argument('username')
        password = self.get_argument('password')
        user = yield self.login(username, password)
        self.write(user)

    @run_on_executor(executor="thread_pool")
    def login(self, username, password):
        return conn.get(
            'select username, password from user where username = %s and password = %s',
            username,
            password,
        )


class RequireHandle(BaseHandle):

    @tornado.gen.coroutine
    def get(self):
        http_client = AsyncHTTPClient()
        response = yield http_client.fetch("http://news-at.zhihu.com/api/4/news/latest")
        r_data = tornado.escape.json_decode(response.body)
        self.write(r_data)


if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[
        (r"/register", RegisterHandler), (r"/login", LoginHandler), (r"/require", RequireHandle)])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
