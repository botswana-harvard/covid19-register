from django.conf import settings
from edc_model_wrapper import ModelWrapper

from ..models import TemperatureRecords, Temperature
from .temerature_model_wrapper import EmployeeTemperatureRecordsModelWrapper


class EmployeeModelWrapper(ModelWrapper):

    model = 'covid19_register.employee'
    next_url_attrs = ['cell']
    next_url_name = settings.DASHBOARD_URL_NAMES.get(
        'employee_listboard_url')

    @property
    def temperature_obj(self):
        """Return today's temperature obj.
        """
        temperature = TemperatureRecords.objects.filter(
            cell=self.cell).order_by('modified').last()
        temp_obj = None
        if temperature and self.object.today_temperature:
            temp_obj = EmployeeTemperatureRecordsModelWrapper(temperature)
        else:
            temp_obj = EmployeeTemperatureRecordsModelWrapper(TemperatureRecords())
        return temp_obj
