from django.conf import settings

from edc_model_wrapper import ModelWrapper


class EmployeeTemperatureRecordsModelWrapper(ModelWrapper):

    model = 'covid19_register.temperaturerecords'
    next_url_attrs = ['cell']
    next_url_name = settings.DASHBOARD_URL_NAMES.get('employee_listboard_url')
    querystring_attrs = ['cell']


class VisitorTemperatureRecordsModelWrapper(ModelWrapper):

    model = 'covid19_register.temperaturerecords'
    next_url_attrs = ['cell']
    next_url_name = settings.DASHBOARD_URL_NAMES.get('visitor_listboard_url')
    querystring_attrs = ['cell']
