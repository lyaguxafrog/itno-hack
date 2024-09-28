from django.db import models
from django.utils.translation import gettext_lazy as _


class Project(models.Model):

    name = models.CharField(
        max_length=1024,
        verbose_name=_("Название"),
    )
    create_date = models.DateTimeField(
        auto_now_add=True, 
        verbose_name=_("Дата создания")
    )


    organisation = models.ForeignKey(
        'organisation.Organisation',
        related_name='organisation',
        on_delete=models.CASCADE,
        verbose_name=_("Организация"),
        null=True,
    )
    owner = models.ForeignKey(
        'auth.User',
        related_name='project_owner',
        on_delete=models.CASCADE,
        verbose_name=_("Владелец")
    ) 
    user = models.ManyToManyField(
        'auth.User',
        verbose_name=_("Пользователь")
    )
