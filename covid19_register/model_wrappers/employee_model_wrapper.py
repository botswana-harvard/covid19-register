from django.conf import settings
from edc_base.utils import get_utcnow
from edc_model_wrapper import ModelWrapper

from ..models import Temperature
from .temerature_model_wrapper import EmployeeTemperatureModelWrapper


class EmployeeModelWrapper(ModelWrapper):

    model = 'covid19_register.employee'
    next_url_attrs = ['cell']
    next_url_name = settings.DASHBOARD_URL_NAMES.get(
        'employee_listboard_url')

    @property
    def temperature_obj(self):
        """Return today's temperature obj or an empty wrapped temperature obj.
        """
        temperatures = Temperature.objects.filter(
            cell=self.cell, site_name=self.site_name)
        if temperatures:
            temperature = temperatures.order_by('today_date').last()
            if temperature.today_date == get_utcnow().date():
                return EmployeeTemperatureModelWrapper(
                    temperature, next_url_name=self.next_url_name)

        return EmployeeTemperatureModelWrapper(
            Temperature(), next_url_name=self.next_url_name)
