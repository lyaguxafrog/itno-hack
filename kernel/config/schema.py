# -*- coding: utf-8 -*-

import graphene
from graphene import ObjectType, Schema

from users.schema import (
    Mutation as UserMutation
)

from project.schema import (
    Mutations as ProjectMutation,
    Query as ProjectQuery
)

from tasks.schema import (
    Mutations as TaskMutation,
    Query as TaskQuery
)

class Query(
    ProjectQuery,
    TaskQuery,
    ObjectType,
):
    pass

class Mutation(
    UserMutation,
    ProjectMutation,
    TaskMutation,
    ObjectType,
):
    pass


schema = Schema(
    query=Query,
    mutation=Mutation,
)
