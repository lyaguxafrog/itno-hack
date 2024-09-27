# -*- coding: utf-8 -*-

from typing import Optional
from datetime import datetime

from django.db.transaction import atomic
from django.db.models import QuerySet
from django.core.cache import cache
from django.contrib.auth.models import Project

from tasks.models import Task


@atomic
def create_task(
    title: str,
    project: Project,
    status: int = 0
) -> Task:
    try:
        cache.delete(key='tasks')
        task = Task.objects.create(
            title=title,
            status=status,
            project=project
        )
    except Exception as err:
        raise Exception(err)

    return task


@atomic
def delete_task(
    task_id: str
) -> bool:
    try:
        task: Task = Task.objects.get(pk=task_id)
        cache.delete(key='tasks')
        task.objects.delete()
    except Exception as err:
        raise Exception(err)
    return True


@atomic
def edit_task(
    task_id: str,
    *args,
    **kwargs
) -> Task:
    """
    Сервис для редактирования существующего task
    """
    try:
        task: Task = Task.objects.get(pk=task_id)
        _kwargs = kwargs.get('kwargs')
        print(_kwargs, args)
        for attr_name, value in _kwargs.items():
            print('attr_name= ', attr_name, 'value= ', value)
            setattr(task, attr_name, value)
            print('attr saved')

        task.save()
        print('task saved')
        return task
    except Exception as err:
        raise Exception(err)


def get_tasks() -> QuerySet:
    """
    Функция для получения всех событий
    """
    cache_ = cache.get(key='tasks')

    if cache_:
        cache.set(
            key='tasks',
            value=cache_,
            timeout=1209600
        )
        return cache_
    else:
        tasks = Task.objects.filter(is_archive=False).all()
        cache.set(
            key='tasks',
            value=tasks,
            timeout=1209600
        )
        return tasks


def get_tasks_for_project(project: Project) -> QuerySet:
    """
    Функция для получения всех task for project
    """
    project_id = project.id
    cache_ = cache.get(key=f'tasks_proj{project_id}')
    if cache_:
        cache.set(
            key=f'tasks_proj{project_id}',
            value=cache_,
            timeout=1209600
        )
        return cache_
    else:
        tasks = Task.objects.filter(project=project, is_archive=False).all()
        cache.set(
            key=f'tasks_proj{project_id}',
            value=tasks,
            timeout=1209600
        )
        return tasks
