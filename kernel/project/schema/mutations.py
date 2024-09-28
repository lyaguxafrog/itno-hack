# -*- coding: utf-8 -*-

from typing import Dict, Any
import graphene
from graphene import relay, ObjectType
from graphql_jwt.decorators import login_required

from .nodes import ProjectNode
from project.services import (
    create_project,
    edit_project,
    delete_project,
    get_project,
)

from utils.global_id import to_global_id


class CreateProjectMutation(relay.ClientIDMutation):
    """
    Мутация для создания проектов
    """
    project = graphene.Field(ProjectNode)

    class Input:
        name = graphene.String()
        owner_id = graphene.ID()
        user_id_list = graphene.List(graphene.String, ids=graphene.List(graphene.ID))

    @staticmethod
    @login_required
    def mutate_and_get_payload(
        root: Any,
        info: graphene.ResolveInfo,
        **input: Dict[str, Any]
    ):
        try:
            # FIXME: ID gql не цифрой
            project = create_project(
                name=input['name'],
                owner_id=input['owner_id'],
                user_id_list=input['user_id_list'],
            )
        except Exception as err:
            raise Exception(err)

        return CreateProjectMutation(project=project)


class EditProjectMutation(relay.ClientIDMutation):
    """
    Мутация для изменения проекта
    """
    project = graphene.Field(ProjectNode)

    class Input:
        project_id = graphene.ID()
        name = graphene.String()
        owner_id = graphene.ID()
        user_id_list = graphene.List(graphene.String, ids=graphene.List(graphene.ID))

    @staticmethod
    @login_required
    def mutate_and_get_payload(
        root: Any,
        info: graphene.ResolveInfo,
        **input: Dict[str, any]
    ):
        try:
            id = to_global_id(info, input['project_id'])
            project = edit_project(
                project_id=id,
                name=input['name'],
                owner_id=input['owner_id'],
                user_id_list=input['user_id_list'],
            )
        except Exception as err:
            raise Exception(err)

        return EditProjectMutation(project=project)


class DeleteProjectMutation(relay.ClientIDMutation):
    """
    Мутация для удаления проекта
    """
    message = graphene.String()

    class Input:
        project_id = graphene.ID()

    @staticmethod
    @login_required
    def mutate_and_get_payload(
        root: Any,
        info: graphene.ResolveInfo,
        **input: Dict[str, any]
    ):
        try:
            id = to_global_id(info, input['project_id'])
            delete_project(project_id=id)
            message = 'successful delete'
        except Exception as err:
            message = 'fail to delete'
            raise Exception(err)
        return DeleteProjectMutation(message=message)


class Mutation(
    ObjectType
):
    create_project = CreateProjectMutation.Field()
    edit_project = EditProjectMutation.Field()
    delete_project = DeleteProjectMutation.Field()
