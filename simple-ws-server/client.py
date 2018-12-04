#!/usr/bin/env python3

import io
from contextlib import redirect_stdout
from tornado import gen
from tornado.ioloop import IOLoop
from tornado.websocket import websocket_connect


class Client:
    def __init__(self, url):
        self.url = url
        self.connection = None
        self.ioloop = IOLoop.instance()
        self.connect()
        self.ioloop.start()
        self.ioloop.close()

    @gen.coroutine
    def connect(self):
        self.connection = yield websocket_connect(self.url)
        self.run()

    def run(self):
        f = io.StringIO()
        with redirect_stdout(f):
            import this
        zen = f.getvalue().split('\n')[2:-1]
        for elem in zen:
            self.connection.write_message(elem)
        self.connection.close()
        self.ioloop.stop()


def start_websocket_client():
    client = Client("ws://localhost:8888/main")


if __name__ == '__main__':
    start_websocket_client()
