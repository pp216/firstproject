import graphene
from graphql_auth.schema import UserQuery
from graphql_auth.schema import MeQuery
from graphql_auth.schema import mutations



class AuthMutation(graphene.ObjectType):
    register=mutations.Register.Field()




class Query(UserQuery,MeQuery,graphene.ObjectType):
    pass

class Mutation(AuthMutation,graphene.ObjectType):
    pass


schema=graphene.Schema(query=Query,mutation=Mutation)
