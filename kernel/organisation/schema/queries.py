import graphene
from graphene_django import DjangoConnectionField

from .nodes import OrganisationNode 

from project.schema.nodes import ProjectNode
from project.models import Project
from project.schema.queries import Query as ProjectQuery

from organisation.services import get_organisation
from utils.global_id import to_global_id 


class Query(graphene.ObjectType):
    """
    Query для получения организации
    """
    organisation_by_id = graphene.Field(
        type_=OrganisationNode,
        id=graphene.ID()
    )
    all_organisation = DjangoConnectionField(OrganisationNode)

    ProjectQuery.all_project
    
    def resolve_organisation_by_id(root, info, id):
        id = to_global_id(info, id)
        return get_organisation().get(pk=id)

    def resolve_all_projects(root, info):
        return Project.objects.all()