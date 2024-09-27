import graphene
from graphene import relay
from graphene_django import DjangoObjectType

from project.models import Project 
from user.schema.nodes import UserNode


class ProjectNode(DjangoObjectType):
    name = graphene.String() 
    create_date = graphene.String()
    owner = graphene.Field(UserNode)
    user = graphene.List(UserNode)

    class Meta:
        model = Project 
        interfaces = [relay.Node,]
        # fields = [
        #     'phone',
        #     'email',
        #     'first_name',
        #     'last_name',
        #     'role',
        #     # 'date_of_birth'
        # ]

        # read_only_fields = [
        #     'phone'
        # ]
