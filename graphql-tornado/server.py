import tornado.web
from tornado.ioloop import IOLoop
from graphene_tornado.tornado_graphql_handler import TornadoGraphQLHandler

from schema import post_schema


class Application(tornado.web.Application):

    def __init__(self):
        handlers = [
            (r'/post', TornadoGraphQLHandler, dict(graphiql=True, schema=post_schema))
        ]
        tornado.web.Application.__init__(self, handlers)


if __name__ == '__main__':
    app = Application()
    app.listen(8888)
    IOLoop.instance().start()