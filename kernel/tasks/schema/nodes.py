# -*- coding: utf-8 -*-

from graphene import relay
from graphene_django import DjangoObjectType
import django_filters

from tasks.models import Task


class TaskTypeNode(DjangoObjectType):
    class Meta:
        model = Task
        filels = ["__all__"]
        interfaces = [relay.Node, ]


class TaskFilter(django_filters.FilterSet):
    class Meta:
        model = Task
        fields = []
        # ordering = []
