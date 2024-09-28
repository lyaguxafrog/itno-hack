import graphene
from graphene_django import DjangoConnectionField

from .nodes import OrganisationNode 

from organisation.services import get_organisation
from utils.global_id import to_global_id 


class Query(graphene.ObjectType):
    """
    """
    project_by_id = graphene.Field(
        type_=OrganisationNode,
        id=graphene.ID()
    )
    all_project = DjangoConnectionField(OrganisationNode)

    def resolve_organisation_by_id(root, info, id):
        id = to_global_id(info, id)
        return get_organisation().get(pk=id)
