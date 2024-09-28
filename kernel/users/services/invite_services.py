# -*- coding: utf-8 -*-

import json
import random
import string

from django.contrib.auth.models import User
from django.db.transaction import atomic
from django.core.mail import send_mail
from django.core.cache import cache



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
    print(recipient)
    status = send_mail(subject, message, email_from, recipient)
    print(status)



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


