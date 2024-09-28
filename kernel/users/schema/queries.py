import graphene
from graphene_django import DjangoConnectionField

from .nodes import UserNode 

from project.schema.nodes import ProjectNode
from project.models import Project
from project.schema.queries import Query as ProjectQuery

from organisation.services import get_organisation
from utils.global_id import to_global_id 
from users.services import get_user

class Query(graphene.ObjectType):
    """
    Query для получения организации
    """
    user_by_id = graphene.Field(
        type_=UserNode,
        id=graphene.ID()
    )
    all_users = DjangoConnectionField(UserNode)

    ProjectQuery.all_project
    
    def resolve_user_by_id(root, info, id):
        user_id = to_global_id(info, id)
        return get_user().get(pk=user_id)

    def resolve_all_projects(root, info):
        return Project.objects.all()