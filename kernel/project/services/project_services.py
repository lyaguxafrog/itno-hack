from typing import Optional, List

from django.db.models import QuerySet
from django.db.transaction import atomic
from django.core.cache import cache
from django.contrib.auth.models import User

from project.models import Project 
from organisation.models import Organisation

@atomic
def create_project(
    name: str,
    organisation_id: int | None,
    owner_id: int,
    user_id_list: List[int] | None, 
) -> Project:
    try:
        cache.delete(key='project')
        if organisation_id is not None:
            organisation = Organisation.objects.get(pk=organisation_id)
        else:
            organisation = None
        owner = User.objects.get(pk=owner_id)
        if user_id_list is not None:
            user = User.objects.filter(pk__in=user_id_list)
        else:
            user = None
        project = Project.objects.create(
            organisation=organisation,
            name=name,
            owner=owner,
        )
        if user:
            project.user.set(user)
        project.save()
    except Exception as err:
        raise Exception(err)
    return project 


@atomic
def edit_project(
    project_id: int,
    name: str | None,
    organisation_id: int,
    owner_id: int | None,
    user_id_list: List[int] | None, 
) -> Project:
    try:
        cache.delete(key='project')
        project = Project.objects.get(
            pk=project_id,
        )
        if name is not None:
            project.name = name

        if organisation_id is not None:
            organisation = Organisation.objects.get(pk=organisation_id)
            project.organisation = organisation

        if owner_id is not None:
            owner = User.objects.get(pk=owner_id)
            project.owner = owner

        if user_id_list is not None:
            user = User.objects.filter(pk__in=user_id_list)
            project.user = user

        project.save()

    except Exception as err:
        raise Exception(err)
    return project 


@atomic
def add_user_to_project(
    project_id: int,
    user_id: int,
) -> bool:
    try:
        project = Project.objects.get(
            pk=project_id,
        )

        user = User.objects.get(pk=user_id)
        project.user.add(user)
        project.save()

    except Exception as err:
        raise Exception(err)
    return True  


@atomic
def remove_user_from_project(
    project_id: int,
    user_id: int,
) -> bool:
    try:
        project = Project.objects.get(
            pk=project_id,
        )

        user = User.objects.get(pk=user_id)
        project.user.remove(user)
        project.save()

    except Exception as err:
        raise Exception(err)
    return True  


@atomic
def delete_project(
    project_id: int,
) -> bool:
    try:
        cache.delete(key='project')
        project = Project.objects.get(
            pk=project_id,
        )
        project.delete()
    except Exception as err:
        raise Exception(err)
    return True 


def get_project() -> QuerySet:
    """
    Функция для получения всех событий
    """
    cache_ = cache.get(key='project')

    if cache_:
        cache.set(
            key='project',
            value=cache_,
            timeout=1209600
        )
        return cache_
    else:
        project = Project.objects.filter().all()
        cache.set(
            key='project',
            value=project,
            timeout=1209600
        )
        return project 

