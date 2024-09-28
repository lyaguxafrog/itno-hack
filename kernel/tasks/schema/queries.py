# -*- coding: utf-8 -*-

import graphene
from graphene_django import DjangoConnectionField
from graphql_jwt.decorators import login_required

from .nodes import TaskTypeNode

from tasks.services import get_tasks_for_project, get_tasks
from utils.global_id import to_global_id

class Query(graphene.ObjectType):
    """
    Query для получения задачи
    """
    task_by_id = graphene.Field(
        type_=TaskTypeNode,
        id=graphene.ID()
    )
    all_tasks = DjangoConnectionField(TaskTypeNode)

    @login_required
    def resolve_task_by_id(root, info, id):
        new_id = to_global_id(info, id)

        return get_tasks().get(pk=new_id)
