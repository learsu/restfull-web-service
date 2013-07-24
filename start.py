#!/bin/env python
#coding = utf-8

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options

define("port", default=8889, help="run on the given port", type=int)

from test import TestHandler, TradeHandler, TestGetHandler, GoHandler, TestModHandler


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world. learsu")


def main():
    tornado.options.parse_command_line()
    application = tornado.web.Application([
    	#('/favicon.ico', tornado.web.ErrorHandler, dict(status_code=404)), 
        (r"/", MainHandler),
        (r"/test", TestHandler),
        (r"/trade", TradeHandler),
        #(r"/testget/([0-9]+)", TestGetHandler),
        (r"/testget/(\w+)", TestGetHandler),
        (r"/go/(\w+)/(\w+)/(\w+)", GoHandler),
        (r"/testmod/(\w+)", TestModHandler),
    ])
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
