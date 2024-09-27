from typing import Dict, Any
import graphene
from graphene import relay, ObjectType

from .nodes import ProjectNode
from users.schema.nodes import UserNode
from project.services import create_project


class CreateProjectMutation(relay.ClientIDMutation):
    project = graphene.Field(ProjectNode)

    class Input:
        name = graphene.String() 
        owner_id = graphene.ID()
        # user = graphene.List(UserNode)

    @staticmethod
    def mutate_and_get_payload(
        root: Any,
        info: graphene.ResolveInfo,
        **input: Dict[str, Any]
    ):
        try:
            project = create_project(
                name=input['name'],
                owner_id=input['owner_id'],
                # user=user, 
            )
        except Exception as err:
            raise Exception(err)

        return CreateProjectMutation(project=project)


class Mutation(
    ObjectType
):
    create_project = CreateProjectMutation.Field()
