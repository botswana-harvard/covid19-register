"""covid19_register URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.apps import apps as django_apps
from django.contrib import admin
from django.urls import path

from edc_dashboard import UrlConfig

from .admin_site import covid19_register_admin
from .views import HomeView, VisitorListBoardView, EmployeeListBoardView

app_name = 'covid19_register'
app_config = django_apps.get_app_config(app_name)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/', covid19_register_admin.urls),
    path('', HomeView.as_view(), name='home_url'),
]

visitor_listboard_url_config = UrlConfig(
    url_name='visitor_listboard_url',
    view_class=VisitorListBoardView,
    label='visitor_listboard',
    identifier_label='identity',
    identifier_pattern=app_config.identifier_pattern)

employee_listboard_url_config = UrlConfig(
    url_name='employee_listboard_url',
    view_class=EmployeeListBoardView,
    label='employee_listboard',
    identifier_label='identity',
    identifier_pattern=app_config.identifier_pattern)

urlpatterns += visitor_listboard_url_config.listboard_urls
urlpatterns += employee_listboard_url_config.listboard_urls
