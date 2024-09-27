# -*- coding: utf-8 -*-

import graphene
from graphene import ObjectType, Schema
from project.schema import Mutations as ProjectMutation
from project.schema import Query as ProjectQuery
from tasks.schema import Mutations as TaskMutation


class Query(
    ProjectQuery,
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
