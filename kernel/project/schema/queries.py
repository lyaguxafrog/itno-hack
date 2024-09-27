import graphene
from graphene_django import DjangoConnectionField

from .nodes import ProjectNode 

from project.services import get_project
from utils.global_id import to_global_id 


# class ProjectQuery():
#     project = graphene.Field(ProjectNode)
#
#     class Input:
#         project_id = graphene.ID()
#
#     @staticmethod
#     def get_project(
#         root: Any,
#         info: graphene.ResolveInfo,
#         **input: Dict[str, Any]
#     ):
#         try:
#             id = to_global_id(info, input['project_id'])
#             project = get_project(
#                 project_id=id
#             )
#         except Exception as err:
#             raise Exception(err)
#
#         return ProjectQuery(project=project)


class Query(graphene.ObjectType):
    project_by_id = graphene.Field(
        type_=ProjectNode,
        id=graphene.ID()
    )
    all_project = DjangoConnectionField(ProjectNode)

    def resolve_project_by_id(root, info, id):
        id = to_global_id(info, id)
        return get_project().get(pk=id)




