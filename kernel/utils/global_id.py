# -*- coding: utf-8 -*-

from graphene.relay.node import DefaultGlobalIDType


def to_global_id(info, gql_id: str) -> int:
    if gql_id is None:
        return None
    id = DefaultGlobalIDType.resolve_global_id(info, gql_id)
    return id[-1]
