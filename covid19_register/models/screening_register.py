from django.db import models

from django_crypto_fields.fields import EncryptedCharField
from django_crypto_fields.fields import EncryptedTextField
from django_crypto_fields.fields import FirstnameField
from django_crypto_fields.fields import IdentityField
from django_crypto_fields.fields import LastnameField
from django_crypto_fields.mixins import CryptoMixin
from edc_base.model_validators import CellNumber
from edc_constants.choices import GENDER_UNDETERMINED

from .choices import SITE_NAME


class ScreeningRegister(CryptoMixin, models.Model):

    first_name = FirstnameField(
        null=True, blank=False)

    last_name = LastnameField(
        verbose_name="Last name",
        null=True, blank=False)

    dob = models.DateField(
        verbose_name="Date of birth",
        null=True,
        blank=True)

    gender = models.CharField(
        verbose_name="Gender",
        choices=GENDER_UNDETERMINED,
        max_length=1,
        null=True,
        blank=True)

    identity = IdentityField(
        verbose_name='Identity number/Passport number',
        null=True,
        blank=True)

    cell = EncryptedCharField(
        verbose_name='Cell number',
        validators=[CellNumber, ],
        blank=False)

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
        null=True)

    work_place = EncryptedCharField(
        verbose_name='Place of work',
        blank=True,
        null=True)

    site_name = models.CharField(
        verbose_name='Site name',
        choices=SITE_NAME,
        max_length=20,
        blank=False,
        null=False)

    class Meta:
        abstract = True
        unique_together = (
            'first_name', 'last_name', 'cell', 'site_name')
