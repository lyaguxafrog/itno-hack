# -*- coding: utf-8 -*-

from graphene import ObjectType

from .mutations import Mutation as OrganisationMutation 
from .queries import Query as OrganisationQuery 


class Query(
    OrganisationQuery,
    ObjectType,
):
    pass


class Mutations(
    OrganisationMutation,
    ObjectType
):
    pass
