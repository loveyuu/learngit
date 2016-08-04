# encoding=utf-8
import tornado.web


class BaseHandle(tornado.web.RequestHandler):

    def data_received(self, chunk):
        pass
