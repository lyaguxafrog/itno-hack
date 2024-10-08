from typing import Dict, Any
import graphene
from graphene import relay, ObjectType

from .nodes import OrganisationNode

from organisation.services import (
    create_organisation,
    edit_organisation,
    delete_organisation,
    add_user_to_organisation,
    remove_user_from_organisation,
) 

from utils.global_id import to_global_id


class CreateOrganisationMutation(relay.ClientIDMutation):
    """
    """
    organisation = graphene.Field(OrganisationNode)

    class Input:
        name = graphene.String() 
        owner_id = graphene.ID()
        user_id_list = graphene.List(graphene.String, ids=graphene.List(graphene.ID))

    @staticmethod
    def mutate_and_get_payload(
        root: Any,
        info: graphene.ResolveInfo,
        **input: Dict[str, Any]
    ):
        try:
            organisation = create_organisation(
                name=input['name'],
                owner_id=input['owner_id'],
                user_id_list=input['user_id_list'], 
            )
        except Exception as err:
            raise Exception(err)

        return CreateOrganisationMutation(organisation=organisation)


class EditOrganisationMutation(relay.ClientIDMutation):
    """
    """
    organisation = graphene.Field(OrganisationNode)

    class Input:
        organisation_id = graphene.ID() 
        name = graphene.String() 
        owner_id = graphene.ID()
        user_id_list = graphene.List(graphene.String, ids=graphene.List(graphene.ID))

    @staticmethod
    def mutate_and_get_payload(
        root: Any,
        info: graphene.ResolveInfo,
        **input: Dict[str, any]
    ):
        try:
            id = to_global_id(info, input['organisation_id'])
            organisation = edit_organisation(
                organisation_id=id,
                name=input['name'],
                owner_id=input['owner_id'],
                user_id_list=input['user_id_list'], 
            )
        except Exception as err:
            raise Exception(err)

        return EditOrganisationMutation(organisation=organisation)


class DeleteOrganisationMutation(relay.ClientIDMutation):
    """
    """
    message = graphene.String()

    class Input:
        organisation_id = graphene.ID()

    @staticmethod
    def mutate_and_get_payload(
        root: Any,
        info: graphene.ResolveInfo,
        **input: Dict[str, any]
    ):
        try:
            id = to_global_id(info, input['organisation_id'])
            delete_organisation(organisation_id=id)
            message = 'successful delete'
        except Exception as err:
            message = 'fail to delete'
            raise Exception(err)
        return DeleteOrganisationMutation(message=message)


class AddUserOrganisation(relay.ClientIDMutation):
    """
    Мутация для добавления user 
    """
    message = graphene.String()

    class Input:
        organisation_id = graphene.ID()
        user_id = graphene.ID()

    @staticmethod
    def mutate_and_get_payload(
        root: Any,
        info: graphene.ResolveInfo,
        **input: Dict[str, any]
    ):
        try:
            id = to_global_id(info, input['organisation_id'])
            add_user_to_organisation(
                organisation_id=id,
                user_id=input['user_id']
            )
            message = 'successful add'
        except Exception as err:
            message = 'fail to add'
            raise Exception(err)
        return AddUserOrganisation(message=message)


class DeleteUserOrganisation(relay.ClientIDMutation):
    """
    Мутация для удаления user 
    """
    message = graphene.String()

    class Input:
        organisation_id = graphene.ID()
        user_id = graphene.ID()

    @staticmethod
    def mutate_and_get_payload(
        root: Any,
        info: graphene.ResolveInfo,
        **input: Dict[str, any]
    ):
        try:
            id = to_global_id(info, input['organisation_id'])
            remove_user_from_organisation(
                organisation_id=id,
                user_id=input['user_id']
            )
            message = 'successful delete'
        except Exception as err:
            message = 'fail to delete'
            raise Exception(err)
        return DeleteUserOrganisation(message=message)



class Mutation(
    ObjectType
):
    create_organisation = CreateOrganisationMutation.Field()
    edit_organisation = EditOrganisationMutation.Field()
    delete_organisation = DeleteOrganisationMutation.Field()
    add_user_to_Organisation = AddUserOrganisation.Field()
    remove_user_from_Organisation = DeleteUserOrganisation.Field()

