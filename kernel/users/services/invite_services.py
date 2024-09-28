# -*- coding: utf-8 -*-

import json
import random
import string

from django.contrib.auth.models import User
from django.db.transaction import atomic
from django.core.mail import send_mail
from django.core.cache import cache

from project.services import add_user_to_project


def random_sequence(length: int = 16):
    char = string.ascii_letters + string.digits  
    return ''.join(random.choice(char) for _ in range(length))



def send_invite_email(
    invite_code: str,
    user_email: str
):
    subject = 'Приглашение'
    message = f'Ссылка: /invite/{invite_code}'
    email_from = 'no-reply@makridenko.ru' 
    recipient = [user_email]

    # Параметры для отправки почты
    fail_silently = False  # Если True, исключения при ошибке не будут генерироваться
    auth_user = None  # Если требуется аутентификация, укажите здесь пользователя
    auth_password = None  # Если требуется аутентификация, укажите здесь пароль
    connection = None  # Используйте соединение по умолчанию
    html_message = None  # Если нужно отправить HTML-письмо, добавьте здесь HTML-контент

    print(recipient)
    print(f"{subject} {message} {email_from} {recipient}")

    # Отправка почты
    status = send_mail(
        subject=subject,
        message=message,
        from_email=email_from,
        recipient_list=recipient,
        fail_silently=fail_silently,
        auth_user=auth_user,
        auth_password=auth_password,
        connection=connection,
        html_message=html_message,
    )


    return status



@atomic
def invite_user_to_project(
    user_id: int,
    project_id: int,
) -> bool:
    user = User.objects.get(pk=user_id)
    user_info = {
        'user_id': user_id, 
        'project_id': project_id,
    }
    user_info_str = json.dumps(user_info)
    invite_code = random_sequence()
    cache.set(invite_code, user_info_str, timeout=60*60*3)
    
    
    send_invite_email(invite_code, user.email)
    value = cache.get(invite_code)
    print(value)
    return True 



@atomic
def accept_user_to_project(
    user_id: int,
    invite_code: str,
) -> int:
    cache_ = cache.get(key=invite_code)
    
    if cache_:
        data_dict = json.loads(cache_)
        if data_dict['user_id'] == str(user_id):
            project_id = int(data_dict['project_id'])
            add_user_to_project(project_id, user_id)
            return data_dict['project_id']
    else:
        return -1