from typing import Optional

from django.db.models import QuerySet
from django.db.transaction import atomic
from django.core.cache import cache
from django.contrib.auth.models import User

from project.models import Project 


@atomic
def create_project(
    name: str,
    owner_id: str | int,
    # user: User, 
) -> Project:

    try:
        cache.delete(key='project')
        owner = User.objects.get(pk=int(owner_id))
        project = Project.objects.create(
            name=name,
            owner=owner,
            # user=user, 
        )
    except Exception as err:
        raise Exception(err)

    return project 


# @atomic
# def get_project(event_id: str) -> QuerySet:
#     cache_ = cache.get(key='project')
#     if cache_:
#         cache.set(
#             key='project',
#             value=cache_,
#             timeout=1209600
#         )
#         return cache_
#     else:
#         event = Project.objects.get(pk=event_id)
#         project = Project.objects.filter(event=event).all()
#         cache.set(
#             key='project',
#             value=project,
#             timeout=12096600
#         )
#         return project 
