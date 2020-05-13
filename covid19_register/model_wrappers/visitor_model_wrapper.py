from django.conf import settings
from edc_model_wrapper import ModelWrapper

from .temerature_model_wrapper import TemperatureModelWrapper


class VisitorModelWrapper(ModelWrapper):

    model = 'covid19_register.visitor'
    next_url_attrs = ['identity']
    next_url_name = settings.DASHBOARD_URL_NAMES.get(
        'visitor_listboard_url')

    def temperature_obj(self):
        """Return a temperature obj.
        """
        return TemperatureModelWrapper(self.temperature)
