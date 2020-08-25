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
            cell=self.cell, site_name=self.site_name).order_by('modified').last()
        temp_obj = None
        if temperature:
            temp_obj = VisitorTemperatureModelWrapper(
                temperature, next_url_name=self.next_url_name)
        else:
            temp_obj = VisitorTemperatureModelWrapper(
                Temperature(cell=self.cell, site_name=self.site_name),
                next_url_name=self.next_url_name)
        return temp_obj
