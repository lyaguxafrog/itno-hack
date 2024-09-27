# -*- coding: utf-8 -*-

from graphene import ObjectType

from .mutations import Mutation as ProjectMutation

class Query(
    ObjectType,
):
    pass


class Mutations(
    ProjectMutation,
    ObjectType
):
    pass
