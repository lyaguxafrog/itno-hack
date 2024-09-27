# -*- coding: utf-8 -*-

from graphene import relay
from graphene_django import DjangoObjectType

from django.contrib.auth.models import User


class UserNode(DjangoObjectType):
    """
    User base model
    """

    class Meta:
        model = User
        filels = [
            "id",
            "email",
            "username"
        ]
        exclude = [
            "password",
            "first_name",
            "last_name",
            "is_active",
            "last_login",
            "is_staff",
            "is_superuser"
        ]
        interfaces = [relay.Node, ]
