from typing import Optional, List

from django.db.models import QuerySet
from django.db.transaction import atomic
from django.core.cache import cache
from django.contrib.auth.models import User

from organisation.models import Organisation 


@atomic
def create_organisation(
    name: str,
    owner_id: int,
    user_id_list: List[int] | None, 
) -> Organisation:
    try:
        cache.delete(key='organisation')
        owner = User.objects.get(pk=owner_id)
        user = User.objects.filter(pk__in=user_id_list)
        organisation = Organisation.objects.create(
            name=name,
            owner=owner,
        )
        organisation.user.set(user)
        organisation.save()
    except Exception as err:
        raise Exception(err)
    return organisation 


@atomic
def edit_organisation(
    organisation_id: int,
    name: str | None,
    owner_id: int | None,
    user_id_list: List[int] | None, 
) -> Organisation:
    try:
        cache.delete(key='organisation')
        organisation = Organisation.objects.get(
            pk=organisation_id,
        )
        if name is not None:
            organisation.name = name

        if owner_id is not None:
            owner = User.objects.get(pk=owner_id)
            organisation.owner = owner

        if user_id_list is not None:
            user = User.objects.filter(pk__in=user_id_list)
            organisation.user = user

        organisation.save()

    except Exception as err:
        raise Exception(err)
    return organisation 


@atomic
def delete_organisation(
    organisation_id: int,
) -> bool:
    try:
        cache.delete(key='organisation')
        organisation = Organisation.objects.get(
            pk=organisation_id,
        )
        organisation.delete()
    except Exception as err:
        raise Exception(err)
    return True 


def get_organisation() -> QuerySet:
    cache_ = cache.get(key='organisation')

    if cache_:
        cache.set(
            key='organisation',
            value=cache_,
            timeout=1209600
        )
        return cache_
    else:
        organisation = Organisation.objects.filter().all()
        cache.set(
            key='organisation',
            value=organisation,
            timeout=1209600
        )
        return organisation 


