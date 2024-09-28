# -*- coding: utf-8 -*-

from typing import Any, Dict

from django.core.exceptions import ValidationError
from graphql.error import GraphQLError
import graphene
from graphene import relay, ObjectType
from graphql_jwt.decorators import login_required

from .nodes import UserNode
from project.schema.nodes import ProjectNode
from project.models import Project

from users.services import (
    create_user, 
    invite_user_to_project,
    accept_user_to_project,
)
from utils.global_id import to_global_id


class RegisterUserMutation(relay.ClientIDMutation):
    """
    Mutation to user registartion
    """

    user = graphene.Field(UserNode)

    class Input:
        username = graphene.String(required=True)
        email = graphene.String(required=True)
        password = graphene.String(required=True)
        repeat_password = graphene.String(required=True)


    @staticmethod
    def mutate_and_get_payload(
        root: Any,
        info: graphene.ResolveInfo,
        **input: Dict[str, Any]
    ):
        try:
            user = create_user(
                username=input['username'],
                email=input['email'],
                password=input['password'],
                repeat_password=input['repeat_password']
            )

        except ValidationError as errors:
            error_list = [str(error) for error in errors]
            raise GraphQLError(message='\n'.join(error_list))

        return RegisterUserMutation(user=user)


class InviteUserMutation(relay.ClientIDMutation):
    """
    Mutation to user invite 
    """

    user = graphene.Field(UserNode)

    class Input:
        user_id = graphene.ID(required=True)
        project_id = graphene.ID(required=True)


    @staticmethod
    def mutate_and_get_payload(
        root: Any,
        info: graphene.ResolveInfo,
        **input: Dict[str, Any]
    ):
        try:
            user_id = to_global_id(info, input['user_id'])
            project_id = to_global_id(info, input['project_id'])
            invite_user_to_project(
                user_id=user_id,
                project_id=project_id, 
            )
            message = 'successful send'
        except Exception as err:
            message = 'fail in send'
            raise Exception(err) 

        return InviteUserMutation(message=message)


class AcceptToProjectMutation(relay.ClientIDMutation):
    """
    Mutation to accept or reject user 
    """

    project = graphene.Field(ProjectNode)

    class Input:
        invite_code = graphene.String(required=True)


    @staticmethod
    @login_required
    def mutate_and_get_payload(
        root: Any,
        info: graphene.ResolveInfo,
        **input: Dict[str, Any]
    ):
        try:
            invite_code = input['invite_code']
            user_id = info.context.user.id
            
            response = accept_user_to_project(
                user_id=user_id,
                invite_code=invite_code, 
            )

            project = Project.objects.get(pk=response)                
        except Exception as err:
            raise Exception(err) 

        return AcceptToProjectMutation(project=project)


class Mutation(
    ObjectType
):
    register_user = RegisterUserMutation.Field()
    invite_user = InviteUserMutation.Field()
    accept_user = AcceptToProjectMutation.Field()