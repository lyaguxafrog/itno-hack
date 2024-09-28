import graphene
from graphene import relay
from graphene_django import DjangoObjectType

from project.models import Project 


class ProjectNode(DjangoObjectType):

    class Meta:
        model = Project 
        interfaces = [relay.Node,]
        fields = [
            'name',
            'create_date',
            'owner',
            'user',
        ]
