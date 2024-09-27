import graphene
from graphene import relay
from graphene_django import DjangoObjectType

from project.models import Project 
from users.schema.nodes import UserNode


class ProjectNode(DjangoObjectType):
    name = graphene.String() 
    create_date = graphene.String()
    owner = graphene.Field(UserNode)
    user = graphene.List(UserNode)

    class Meta:
        model = Project 
        interfaces = [relay.Node,]
        fields = [
            'name',
            'create_date',
            'owner',
            'user',
        ]

        # read_only_fields = [
        #     'create_date'
        # ]
