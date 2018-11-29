import json
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.log import app_log as log
from tornado.web import Application
from tornado.web import RequestHandler
from tornado.options import define, options

define('host', default='localhost')
define('port', default='8888')


class MainHandler(RequestHandler):

    def get(self):
        self.render('static/main.html')

    def post(self):
        data = json.loads(self.request.body.decode('utf-8'))
        log.info(f'Post data:{data}')
        if not data['author']:
            self.set_status(400)
        self.write(json.dumps({'msg': 'Ok'}))


application = Application([
    (r"/main", MainHandler),
])


def start_http_server():
    options.parse_command_line()
    http_server = HTTPServer(application)
    http_server.listen(options.port, options.host)
    log.info(f'Server started {options.host}:{options.port}')
    IOLoop.instance().start()
