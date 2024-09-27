# -*- coding: utf-8 -*-

import graphene
from graphene_django import DjangoConnectionField

from .nodes import TaskTypeNode

from tasks.services import get_tasks_for_project, get_tasks


class Query(graphene.ObjectType):
    task_by_id = graphene.Field(
        type_=TaskTypeNode,
        id=graphene.ID()
    )
    all_tasks = DjangoConnectionField(TaskTypeNode)

    def resolve_task_by_id(root, info, id):
        return get_tasks().get(pk=id)
