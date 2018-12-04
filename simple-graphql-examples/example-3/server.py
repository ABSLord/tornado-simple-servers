"""
TornadoQL server as a simple example or skeleton
"""
from tornadoql.tornadoql import TornadoQL, PORT
from schema import schema


def main():
    print('GraphQL server starting on %s' % PORT)
    TornadoQL.start(schema)


if __name__ == '__main__':
    main()
