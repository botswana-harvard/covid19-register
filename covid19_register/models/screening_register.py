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

from .temparature import Temperature


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
        verbose_name='Identity number/Passport number',
        unique=True)

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

    @property
    def today_temperature(self):
        """Returns True if today's temperature exits.
        """
        lastest_temp = Temperature.objects.filter(
            identity=self.identity).order_by('today_date').last()
        if lastest_temp.today_date == get_utcnow().date():
            return True
        return False

    class Meta:
        abstract = True
