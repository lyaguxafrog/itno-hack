import graphene
from graphene import relay
from graphene_django import DjangoObjectType

from project.models import Project 
from tasks.schema.nodes import TaskTypeNode


class ProjectNode(DjangoObjectType):
    class Meta:
        model = Project 
        interfaces = [relay.Node]
        fields = [
            'name',
            'create_date',
            'owner',
            'user',
            'tasks',
        ]
    
    tasks = graphene.List(TaskTypeNode)

    def resolve_tasks(self, info):
        return self.tasks.all() if self.tasks.exists() else []
