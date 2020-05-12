from django.db import models

from django_crypto_fields.fields import EncryptedCharField
from django_crypto_fields.fields import EncryptedTextField
from django_crypto_fields.fields import FirstnameField
from django_crypto_fields.fields import IdentityField
from django_crypto_fields.fields import LastnameField
from django_crypto_fields.mixins import CryptoMixin
from edc_base.model_validators import CellNumber
from edc_base.utils import get_utcnow
from edc_constants.choices import GENDER_UNDETERMINED


class ScreeningRegister(CryptoMixin, models.Model):

    first_name = FirstnameField(
        null=True, blank=False)

    last_name = LastnameField(
        verbose_name="Last name",
        null=True, blank=False)

    dob = models.DateField(
        verbose_name="Date of birth",
        null=True,
        blank=False)

    gender = models.CharField(
        verbose_name="Gender",
        choices=GENDER_UNDETERMINED,
        max_length=1,
        null=True,
        blank=False)

    identity = IdentityField(
        verbose_name='Identity number')

    cell = EncryptedCharField(
        verbose_name='Cell number',
        validators=[CellNumber, ],
        blank=True,
        null=True,
        help_text='')

    physical_address = EncryptedTextField(
        verbose_name='Physical address with detailed description',
        max_length=500,
        blank=True,
        null=True,
        help_text='')

    permit_reason = EncryptedTextField(
        verbose_name='Reason for permit',
        max_length=500,
        blank=True,
        null=True,
        help_text='')

    work_place = EncryptedCharField(
        verbose_name='Place of work',
        blank=True,
        null=True,
        help_text='')

    today_date = models.DateField(
        verbose_name='Date',
        default=get_utcnow)

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

    class Meta:
        abstract = True
