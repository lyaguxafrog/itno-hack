# -*- coding: utf-8 -*-

from graphene_django.views import GraphQLView

# from django.contrib import admin
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from django.views.generic import TemplateView
from graphql_jwt.decorators import jwt_cookie



urlpatterns = [
    # path('admin/', admin.site.urls),
    path('api/', jwt_cookie(csrf_exempt(GraphQLView.as_view(graphiql=True)))),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





# urlpatterns += [
#     re_path(r'',
#         ensure_csrf_cookie(TemplateView.as_view(template_name='index.html')),
#         name='index',
#     )
# ]
