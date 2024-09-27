import graphene
from graphene_django import DjangoConnectionField

from .nodes import ProjectNode 

from project.services import get_project
from utils.global_id import to_global_id 


class Query(graphene.ObjectType):
    """
    Query для получения проекта 
    """
    project_by_id = graphene.Field(
        type_=ProjectNode,
        id=graphene.ID()
    )
    all_project = DjangoConnectionField(ProjectNode)

    def resolve_project_by_id(root, info, id):
        id = to_global_id(info, id)
        return get_project().get(pk=id)




