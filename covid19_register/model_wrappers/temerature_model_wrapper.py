from django.conf import settings

from edc_model_wrapper import ModelWrapper


class EmployeeTemperatureModelWrapper(ModelWrapper):

    model = 'covid19_register.temperature'
    next_url_attrs = ['cell']
    next_url_name = settings.DASHBOARD_URL_NAMES.get('employee_listboard_url')
    querystring_attrs = ['cell', 'site_name']


class VisitorTemperatureModelWrapper(ModelWrapper):

    model = 'covid19_register.temperature'
    next_url_attrs = ['cell']
    next_url_name = settings.DASHBOARD_URL_NAMES.get('visitor_listboard_url')
    querystring_attrs = ['cell', 'site_name']
