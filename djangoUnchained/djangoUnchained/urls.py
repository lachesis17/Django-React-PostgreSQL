"""
URL configuration for djangoUnchained project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from graphene_django.views import GraphQLView
from .schema import schema
from core.views import home
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.views import serve
from django.views.generic import TemplateView
from django.conf import settings
import os

urlpatterns = [
    #path('', home, name='home'),
    path('admin/', admin.site.urls),
    path("graphql", GraphQLView.as_view(graphiql=True, schema=schema)),
    #re_path(r'^(?P<path>.*)$', serve, {'document_root': os.path.join(settings.BASE_DIR, 'core/static/build'), 'show_indexes': True}),
    re_path(r'^.*$', TemplateView.as_view(template_name='index.html'), name='home'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
