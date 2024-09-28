# -*- coding: utf-8 -*-

import graphene
from graphene import ObjectType, Schema

from project.schema import Mutations as ProjectMutation
from project.schema import Query as ProjectQuery
from organisation.schema import Mutations as OrganisationMutation
from organisation.schema import Query as OrganisationQuery
from tasks.schema import Mutations as TaskMutation
from tasks.schema import Query as TaskQuery

class Query(
    OrganisationQuery,
    ProjectQuery,
    TaskQuery,
    ObjectType,
):

    hello = graphene.String()

    def resolve_hello(root, info, **kwargs):
        return 'world!'


class Mutation(
    OrganisationMutation,
    ProjectMutation,
    TaskMutation,
    ObjectType,
):
    pass


schema = Schema(
    query=Query,
    mutation=Mutation,
)
