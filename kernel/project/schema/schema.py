# -*- coding: utf-8 -*-

from graphene import ObjectType

from .mutations import Mutation as ProjectMutation
from .queries import Query as ProjectQuery


class Query(
    ProjectQuery,
    ObjectType,
):
    pass


class Mutations(
    ProjectMutation,
    ObjectType
):
    pass
