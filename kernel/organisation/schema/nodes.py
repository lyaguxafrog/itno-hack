import graphene
from graphene import relay
from graphene_django import DjangoObjectType

from organisation.models import Organisation 
from users.schema.nodes import UserNode
from project.schema.nodes import ProjectNode

class OrganisationNode(DjangoObjectType):

    class Meta:
        model = Organisation 
        interfaces = [relay.Node,]
        fields = [
            'name',
            'create_date',
            'owner',
            'user',
            'projects'
        ]

    projects = graphene.List(ProjectNode)

    def resolve_projects(self, info):
        return self.projects.all()