from django.conf import settings
from edc_model_wrapper import ModelWrapper


class EmployeeModelWrapper(ModelWrapper):

    model = 'covid19_register.employee'
    next_url_attrs = ['identity']
    next_url_name = settings.DASHBOARD_URL_NAMES.get(
        'employee_listboard_url')
