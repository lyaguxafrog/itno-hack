# -*- coding: utf-8 -*-

import graphene
from graphene import ObjectType, Schema

# from users.schema import Mutations as UserMutations
from tasks.schema import Mutations as TaskMutation


class Query(
    EventQueries,
    ObjectType,
):
    hello = graphene.String()

    def resolve_hello(root, info, **kwargs):
        return 'world!'


class Mutation(
    # UserMutations,
    TaskMutation,
):
    pass


schema = Schema(
    query=Query,
    mutation=Mutation,
)