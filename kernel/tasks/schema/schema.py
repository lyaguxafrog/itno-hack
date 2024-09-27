# -*- coding: utf-8 -*-

from graphene import ObjectType

from .queries import Query as TaskQuery
from .mutations import Mytation as TaskMutations


class Query(
    TaskQuery,
    ObjectType,
):
    pass


class Mutations(
    TaskMutations,
    ObjectType,
):
    pass
