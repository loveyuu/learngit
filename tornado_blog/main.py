# encoding=utf-8

import tornado.ioloop
import tornado.web

from handlers import GenAsyncHandler, Gen2AsyncHandler


def make_app():
    return tornado.web.Application([
        (r"/gen", GenAsyncHandler),
        (r"/gen2", Gen2AsyncHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()

