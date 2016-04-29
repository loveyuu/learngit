# encoding=utf-8
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    def get(self):
        name = self.get_argument("name")
        password = self.get_argument("password")
        if name and password:
            pass
        # 省去处理流程...