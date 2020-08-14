from django.conf import settings
from edc_model_wrapper import ModelWrapper

from ..models import Temperature
from .temerature_model_wrapper import VisitorTemperatureModelWrapper


class VisitorModelWrapper(ModelWrapper):

    model = 'covid19_register.visitor'
    next_url_attrs = ['cell']
    next_url_name = settings.DASHBOARD_URL_NAMES.get(
        'visitor_listboard_url')

    @property
    def temperature_obj(self):
        """Return today's temperature obj.
        """
        temperature = Temperature.objects.filter(
            cell=self.cell).order_by('modified').last()
        temp_obj = None
        if temperature:
            temp_obj = VisitorTemperatureModelWrapper(temperature)
        else:
            temp_obj = VisitorTemperatureModelWrapper(Temperature())
        return temp_obj
