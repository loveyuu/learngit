# encoding=utf-8
import tornado.web


class RedisBaseHandle(tornado.web.RequestHandler):

    def data_received(self, chunk):
        pass

    @property
    def redis(self):
        return self.settings['redis']
