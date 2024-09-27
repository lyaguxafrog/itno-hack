# -*- coding: utf-8 -*-

import graphene
from graphene import ObjectType, Schema
from project.schema import Mutations as ProjectMutation


class Query(ObjectType):
    hello = graphene.String()

    def resolve_hello(root, info, **kwargs):
        return 'world!'


class Mutation(
    ObjectType,
    ProjectMutation
):
    pass


schema = Schema(
    query=Query,
    mutation=Mutation,
)
