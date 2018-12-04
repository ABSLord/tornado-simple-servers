#!/usr/bin/env python3

import json

from tornado.websocket import WebSocketHandler
from tornado.ioloop import IOLoop
from tornado.log import app_log as log
from tornado.web import Application
from tornado.options import define, options
from schema import post_schema

define('port', default='8888')


class WebSocketGraphQLHandler(WebSocketHandler):

    def initialize(self, schema):
        self._schema = schema

    def check_origin(self, origin):
        return True

    def open(self):
        log.info('Client connected')

    def on_message(self, message):
        query = json.loads(message)['query']
        post_id = json.loads(message)['id']
        result = self._schema.execute(query, variable_values={'id': post_id})
        log.info(f'result: {result.data}')
        self.write_message('ok')

    def on_close(self):
        log.info("Client disconnected")


application = Application([
    (r'/ws/posts', WebSocketGraphQLHandler, {'schema': post_schema}),
])


def start_websocket_server():
    options.parse_command_line()
    application.listen(options.port, )
    log.info('WebSocket server started')
    IOLoop.instance().start()


if __name__ == "__main__":
    start_websocket_server()

    """example of usage:
    var websocket = new WebSocket("ws://localhost:8888/ws/posts");
    websocket.send(JSON.stringify({
      query: "query($id: ID){\
              readPost(id: $id){\
              author\
              }\
              }",
       id: 1
    }));
    """


