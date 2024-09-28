import graphene
from graphene import relay
from graphene_django import DjangoObjectType

from organisation.models import Organisation 
from users.schema.nodes import UserNode


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

