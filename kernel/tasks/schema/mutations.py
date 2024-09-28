# -*- coding: utf-8 -*-

from typing import Dict, Any

from graphql_jwt.decorators import login_required, permission_required
import graphene

from graphene import ObjectType, relay
from graphene.relay.node import DefaultGlobalIDType
from django.core.exceptions import ValidationError
from graphql.error import GraphQLError

from tasks.models import Task
from tasks.services import (
    create_task,
    edit_task,
    delete_task,
)
from .nodes import TaskTypeNode
from utils import to_global_id


class CreateTaksMutation(relay.ClientIDMutation):
    """
    Мутация для создания задачи
    """
    task = graphene.Field(TaskTypeNode)

    class Input:
        title = graphene.String(required=True)
        status = graphene.Int(required=False)
        project_id = graphene.ID(required=True)
    @staticmethod
    # @permission_required(perm="tasks.add_task")
    def mutate_and_get_payload(
        root: Any,
        info: graphene.ResolveInfo,
        **input: Dict[str, any]
    ):
        project_id = to_global_id(info, input['project_id'])
        try:
            task = create_task(
                title=input['title'],
                status=input['status'],
                project_id=project_id,
            )

        except Exception as err:
            raise Exception(err)

        return CreateTaksMutation(task=task)


class EditTaskMutation(relay.ClientIDMutation):
    """
    Мутация для изменения задачи
    """
    task = graphene.Field(type_=TaskTypeNode)

    class Input:
        task_id = graphene.ID(required=True)
        title = graphene.String(required=False)
        status = graphene.Int(required=False)

    @staticmethod
    # @permission_required(perm="tasks.edit_tasks")
    def mutate_and_get_payload(
        root: Any,
        info: graphene.ResolveInfo,
        **input: Dict[str, any]
    ):
        try:

            id = to_global_id(info, input['task_id'])

            task = edit_task(
                task_id=id,
                kwargs={
                    'title': input['title'],
                    'status': input['status']
                }
            )
        except Exception as err:
            raise Exception(err)

        return EditTaskMutation(task=task)


class DeleteTaskMutation(relay.ClientIDMutation):
    """
    Мутация для удаления задачи
    """
    message = graphene.String()

    class Input:
        task_id = graphene.ID()

    @staticmethod
    # @permission_required(perm="tasks.delete_tasks")
    def mutate_and_get_payload(
        root: Any,
        info: graphene.ResolveInfo,
        **input: Dict[str, any]
    ):
        try:

            id = to_global_id(info, input['task_id'])
            delete_task(task_id=id)
            message = 'successful delete'
        except Exception as err:
            message = 'fail to delete'
            raise Exception(err)
        return DeleteTaskMutation(message=message)



class Mytation(
    ObjectType
):
    create_task = CreateTaksMutation.Field()
    edit_task = EditTaskMutation.Field()
    delete_task = DeleteTaskMutation.Field()
