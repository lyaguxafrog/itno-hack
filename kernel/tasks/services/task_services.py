# -*- coding: utf-8 -*-

from typing import Optional
from datetime import datetime

from django.db.transaction import atomic
from django.db.models import QuerySet
from django.core.cache import cache

from project.models import Project

from tasks.models import Task


@atomic
def create_task(
    title: str,
    project_id: int,
    status: int = 0
) -> Task:
    try:
        project = Project.objects.get(pk=project_id)
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
        task.delete()
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
        for attr_name, value in _kwargs.items():
            if value is not None:
                setattr(task, attr_name, value)

        task.save()
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
        tasks = Task.objects.filter().all()
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
        tasks = Task.objects.filter(project=project).all()
        cache.set(
            key=f'tasks_proj{project_id}',
            value=tasks,
            timeout=1209600
        )
        return tasks
