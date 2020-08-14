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
from .views import HomeView
from .views.employee import (
    AmbitionListBoardView, CtuListBoardView, EmployeeListBoardView,
    HptnListBoardView, HrListBoardView, MmabanaListBoardView)
from .views.visitor import VisitorListBoardView

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
    identifier_label='cell',
    identifier_pattern=app_config.identifier_pattern)

employee_listboard_url_config = UrlConfig(
    url_name='employee_listboard_url',
    view_class=EmployeeListBoardView,
    label='employee_listboard',
    identifier_label='cell',
    identifier_pattern=app_config.identifier_pattern)

ctu_listboard_url_config = UrlConfig(
    url_name='ctu_listboard_url',
    view_class=CtuListBoardView,
    label='ctu_listboard',
    identifier_label='site_name',
    identifier_pattern=app_config.identifier_pattern)

hptn_listboard_url_config = UrlConfig(
    url_name='hptn_listboard_url',
    view_class=HptnListBoardView,
    label='hptn_listboard',
    identifier_label='site_name',
    identifier_pattern=app_config.identifier_pattern)

ambition_listboard_url_config = UrlConfig(
    url_name='ambition_listboard_url',
    view_class=AmbitionListBoardView,
    label='ambition_listboard',
    identifier_label='site_name',
    identifier_pattern=app_config.identifier_pattern)

hr_listboard_url_config = UrlConfig(
    url_name='hr_listboard_url',
    view_class=HrListBoardView,
    label='hr_listboard',
    identifier_label='site_name',
    identifier_pattern=app_config.identifier_pattern)

pepfar_listboard_url_config = UrlConfig(
    url_name='pepfar_listboard_url',
    view_class=CtuListBoardView,
    label='pepfar_listboard',
    identifier_label='site_name',
    identifier_pattern=app_config.identifier_pattern)

tsepamo_listboard_url_config = UrlConfig(
    url_name='tsepamo_listboard_url',
    view_class=CtuListBoardView,
    label='tsepamo_listboard',
    identifier_label='site_name',
    identifier_pattern=app_config.identifier_pattern)

mmabana_listboard_url_config = UrlConfig(
    url_name='mmabana_listboard_url',
    view_class=MmabanaListBoardView,
    label='mmabana_listboard',
    identifier_label='site_name',
    identifier_pattern=app_config.identifier_pattern)

urlpatterns += visitor_listboard_url_config.listboard_urls
urlpatterns += employee_listboard_url_config.listboard_urls
urlpatterns += ctu_listboard_url_config.listboard_urls
urlpatterns += hptn_listboard_url_config.listboard_urls
urlpatterns += ambition_listboard_url_config.listboard_urls
urlpatterns += hr_listboard_url_config.listboard_urls
urlpatterns += pepfar_listboard_url_config.listboard_urls
urlpatterns += tsepamo_listboard_url_config.listboard_urls
urlpatterns += mmabana_listboard_url_config.listboard_urls
