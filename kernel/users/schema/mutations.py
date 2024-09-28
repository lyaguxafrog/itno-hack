# -*- coding: utf-8 -*-

from typing import Any, Dict

from django.core.exceptions import ValidationError
from graphql.error import GraphQLError
import graphene
from graphene import relay, ObjectType

from .nodes import UserNode
from users.services import create_user


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


class Mutation(
    ObjectType
):
    register_user = RegisterUserMutation.Field()
