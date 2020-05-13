from django.conf import settings
from edc_model_wrapper import ModelWrapper


class VisitorModelWrapper(ModelWrapper):

    model = 'covid19_register.visitor'
    next_url_attrs = ['identity']
    next_url_name = settings.DASHBOARD_URL_NAMES.get(
        'visitor_listboard_url')
