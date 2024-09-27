# -*- coding: utf-8 -*-

import graphene
from graphene import ObjectType, Schema
from project.schema import Mutations as ProjectMutation

# from users.schema import Mutations as UserMutations
from tasks.schema import Mutations as TaskMutation
from tasks.schema import Query as TaskQuery

class Query(
    TaskQuery,
    ObjectType,
):
    hello = graphene.String()

    def resolve_hello(root, info, **kwargs):
        return 'world!'


class Mutation(
    ProjectMutation,
    TaskMutation,
    ObjectType,
):
    pass


schema = Schema(
    query=Query,
    mutation=Mutation,
)
