from typing import Optional, List

from django.db.models import QuerySet
from django.db.transaction import atomic
from django.core.cache import cache
from django.contrib.auth.models import User

from project.models import Project 


@atomic
def create_project(
    name: str,
    owner_id: int,
    user_id_list: List[int] | None, 
) -> Project:
    try:
        cache.delete(key='project')
        owner = User.objects.get(pk=owner_id)
        user = User.objects.filter(pk__in=user_id_list)
        project = Project.objects.create(
            name=name,
            owner=owner,
        )
        project.user.set(user)
        project.save()
    except Exception as err:
        raise Exception(err)
    return project 


@atomic
def edit_project(
    project_id: int,
    name: str | None,
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

