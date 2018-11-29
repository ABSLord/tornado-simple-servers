#!/usr/bin/env python3

from tornado.websocket import WebSocketHandler
from tornado.ioloop import IOLoop
from tornado.log import app_log as log
from tornado.web import Application
from tornado.options import define, options

define('port', default='8888')


class MainHandler(WebSocketHandler):

    def check_origin(self, origin):
        return True

    def open(self):
        log.info('Client connected')

    def on_message(self, message):
        log.info(f'Received message: {message}')

    def on_close(self):
        log.info("Client disconnected")


application = Application([
    (r'/main', MainHandler),
])


def start_websocket_server():
    options.parse_command_line()
    application.listen(options.port, )
    log.info('WebSocket server started')
    IOLoop.instance().start()


if __name__ == "__main__":
    start_websocket_server()
