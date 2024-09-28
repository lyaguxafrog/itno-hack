# -*- coding: utf-8 -*-

import graphql_jwt

from graphene import ObjectType

from .mutations import Mutation as UserMutation
from .queries import Query as UserQuery

class Query(
    UserQuery,
    ObjectType,
):
    pass

class Mutation(
    UserMutation,
    ObjectType
):
    sign_in = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    sign_out = graphql_jwt.DeleteJSONWebTokenCookie.Field()
    # delete_refresh_token_cookie = graphql_jwt.DeleteRefreshTokenCookie.Field()
