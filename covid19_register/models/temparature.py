from django.db import models

from django_crypto_fields.fields import IdentityField
from edc_base.model_mixins import BaseUuidModel
from edc_base.sites.site_model_mixin import SiteModelMixin


class Temperature(SiteModelMixin, BaseUuidModel):

    identity = IdentityField(
        verbose_name='Identity number')

    today_date = models.DateField(
        verbose_name='Date')

    time_in = models.TimeField(
        verbose_name='Time in')

    time_out = models.TimeField(
        verbose_name='Time out',
        blank=True,
        null=True,)

    temperature = models.DecimalField(
        verbose_name='Body Temperature',
        max_digits=5, decimal_places=2,
        help_text='Unit is Celsius')

    def __str__(self):
        return f'{self.today_date}, {self.temperature} {self.time_in}'

    class Meta:
        app_label = 'covid19_register'
        verbose_name = "Covid-19 Register"
        verbose_name_plural = "Covid-19 Register"
