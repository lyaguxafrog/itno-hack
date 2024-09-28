from typing import Dict, Any
import graphene
from graphene import relay, ObjectType

from .nodes import ProjectNode
from project.services import (
    create_project,
    edit_project,
    delete_project,
    add_user_to_project,
    remove_user_from_project,
) 

from utils.global_id import to_global_id


class CreateProjectMutation(relay.ClientIDMutation):
    """
    Мутация для создания проектов 
    """
    project = graphene.Field(ProjectNode)

    class Input:
        name = graphene.String(required=True) 
        organisation_id = graphene.ID(required=False)
        owner_id = graphene.ID(required=True)
        user_id_list = graphene.List(graphene.String, ids=graphene.List(graphene.ID))

    @staticmethod
    def mutate_and_get_payload(
        root: Any,
        info: graphene.ResolveInfo,
        **input: Dict[str, Any]
    ):
        try:
            project = create_project(
                name=input['name'],
                organisation_id=input['organisation_id'],
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
        project_id = graphene.ID(required=True) 
        name = graphene.String(required=False) 
        organisation_id = graphene.ID(required=False)
        owner_id = graphene.ID(required=False)
        user_id_list = graphene.List(graphene.String, ids=graphene.List(graphene.ID))

    @staticmethod
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
                organisation_id=input['organisation_id'],
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


class AddUser(relay.ClientIDMutation):
    """
    Мутация для добавления user 
    """
    message = graphene.String()

    class Input:
        project_id = graphene.ID()
        user_id = graphene.ID()

    @staticmethod
    def mutate_and_get_payload(
        root: Any,
        info: graphene.ResolveInfo,
        **input: Dict[str, any]
    ):
        try:
            id = to_global_id(info, input['project_id'])
            add_user_to_project(
                project_id=id,
                user_id=input['user_id']
            )
            message = 'successful add'
        except Exception as err:
            message = 'fail to add'
            raise Exception(err)
        return DeleteProjectMutation(message=message)


class DeleteUser(relay.ClientIDMutation):
    """
    Мутация для удаления user 
    """
    message = graphene.String()

    class Input:
        project_id = graphene.ID()
        user_id = graphene.ID()

    @staticmethod
    def mutate_and_get_payload(
        root: Any,
        info: graphene.ResolveInfo,
        **input: Dict[str, any]
    ):
        try:
            id = to_global_id(info, input['project_id'])
            remove_user_from_project(
                project_id=id,
                user_id=input['user_id']
            )
            message = 'successful delete'
        except Exception as err:
            message = 'fail to delete'
            raise Exception(err)
        return DeleteUser(message=message)





class Mutation(
    ObjectType
):
    create_project = CreateProjectMutation.Field()
    edit_project = EditProjectMutation.Field()
    delete_project = DeleteProjectMutation.Field()
    add_user = AddUser.Field()
    remove_user = DeleteUser.Field()
