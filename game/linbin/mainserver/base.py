# encoding=utf-8
import tornado.web
from concurrent.futures import ThreadPoolExecutor


class BaseHandle(tornado.web.RequestHandler):
    thread_pool = ThreadPoolExecutor(2)

    def data_received(self, chunk):
        pass
