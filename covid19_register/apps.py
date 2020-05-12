from django.apps import AppConfig as DjangoAppConfig

from edc_base.apps import AppConfig as BaseEdcBaseAppConfig


class AppConfig(DjangoAppConfig):
    name = 'covid19_register'
    verbose_name = 'Covid-19 Register'
    admin_site_name = 'covid19_register_admin'
    identifier_pattern = None


class EdcBaseAppConfig(BaseEdcBaseAppConfig):
    project_name = 'BHP Covid-19 Register'
    institution = 'Botswana-Harvard AIDS Institute'
