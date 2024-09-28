import graphene
from graphene_django import DjangoConnectionField

from .nodes import ProjectNode 

from tasks.schema.nodes import TaskTypeNode
from tasks.models import Task
from tasks.schema.queries import Query as TaskQuery


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

    TaskQuery.all_tasks

    def resolve_project_by_id(root, info, id):
        id = to_global_id(info, id)
        return get_project().get(pk=id)

    def resolve_all_tasks(root, info):
        return Task.objects.all()


