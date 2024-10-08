# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class Task(models.Model):
    """
    Модель задач

    * project: проект
    * title: название
    * status: статус
    """
    OPTION_CHOICES = [
        (0, 0),
        (1, 1),
        (2, 2),
    ]

    project = models.ForeignKey(
        "project.Project",
        related_name="tasks",
        on_delete=models.CASCADE,
        null=False,
    )

    title = models.CharField(
        max_length=64,
        null=False,
    )

    status = models.SmallIntegerField(
        choices = OPTION_CHOICES,
        null=True,
    )
