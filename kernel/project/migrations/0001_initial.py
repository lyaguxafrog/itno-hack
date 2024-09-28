# Generated by Django 5.1.1 on 2024-09-28 11:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organisation', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024, verbose_name='Название')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('organisation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='organisation', to='organisation.organisation', verbose_name='Организация')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_owner', to=settings.AUTH_USER_MODEL, verbose_name='Владелец')),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
    ]
