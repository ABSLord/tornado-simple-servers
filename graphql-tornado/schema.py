import graphene
from graphene import ObjectType, Schema
from graphql import GraphQLError

test_posts = [
    {'id': 1, 'author': 'Bob', 'text': 'Text 1'},
    {'id': 2, 'author': 'John', 'text': 'Text 2'},
    {'id': 3, 'author': 'Matt', 'text': 'Text 3'},
]


class Post(ObjectType):

    id = graphene.ID(required=True)
    author = graphene.String(required=True)
    text = graphene.String(required=True)


class Query(ObjectType):
    read_post = graphene.Field(Post, id=graphene.ID())

    def resolve_read_post(self, _info, id):
        post_id = int(id)
        result = list(filter(lambda post: post['id'] == post_id, test_posts))
        if result:
            return Post(id=result[0]['id'],
                        author=result[0]['author'],
                        text=result[0]['text'])
        raise GraphQLError('Not Found')


class MutationQuery(ObjectType):
    write_post = graphene.Field(Post, id=graphene.ID(), author=graphene.String(), text=graphene.String())

    def resolve_write_post(self, info, id, author, text):
        #  save in db if need it
        return Post(id=id, author=author, text=text)


post_schema = Schema(query=Query, mutation=MutationQuery)
