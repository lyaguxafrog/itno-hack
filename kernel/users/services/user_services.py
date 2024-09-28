# -*- coding: utf-8 -*-

from django.db.transaction import atomic
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.validators import validate_email
from django.contrib.auth.validators import ASCIIUsernameValidator

validate_username = ASCIIUsernameValidator()


@atomic
def create_user(
    username: str,
    email: str,
    password: str,
    repeat_password: str
) -> User:
    """
    Сервис создания пользователя

    :param username: Имя пользователя
    :type username: str
    :param email: Email пользователя
    :type email: str
    :param password: Пароль пользвателя
    :type password: str
    :param repeat_password: Подтверждение пароля
    :type repeat_password: str

    :returns: Объект пользователя
    :rtype: auth.User
    """

    if repeat_password != password:
        raise Exception('Passwords does not match')

    if User.objects.filter(username=username).exists():
        raise Exception('Username already taken')

    if User.objects.filter(email=email).exists():
        raise Exception('Email already taken')

    validate_email(email)
    validate_username(username)
    validate_password(password=password)

    user = User.objects.create_user(
        username=username,
        email=email,
        password=password
    )

    return user
