import graphene
from graphene import relay
from graphene_django import DjangoObjectType

from project.models import Organisation 


class OrganisationNode(DjangoObjectType):

    class Meta:
        model = Organisation 
        interfaces = [relay.Node,]
        fields = [
            'name',
            'create_date',
            'owner',
            'user',
        ]

