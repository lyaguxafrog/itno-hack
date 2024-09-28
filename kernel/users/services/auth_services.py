# -*- coding: utf-8 -*-

from graphql_jwt.utils import jwt_payload, jwt_encode

from django.contrib.auth.models import User


def gen_jwt_token(user: User) -> str:
    """
    Service to generate a jwt token for a user.

    :param user: User object
    :type user: auth.User

    :returns: Returns the generated token
    :rtype: str
    """

    payload = jwt_payload(
        user=user,
        context=None
    )

    token = jwt_encode(
        payload=payload
    )

    return token
