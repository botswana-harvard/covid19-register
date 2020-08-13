from django.contrib import admin
from django_revision.modeladmin_mixin import ModelAdminRevisionMixin
from edc_base.sites.admin import ModelAdminSiteMixin
from edc_model_admin import (
    ModelAdminNextUrlRedirectMixin, ModelAdminFormInstructionsMixin,
    ModelAdminFormAutoNumberMixin, ModelAdminAuditFieldsMixin,
    ModelAdminReadOnlyMixin, ModelAdminInstitutionMixin,
    ModelAdminRedirectOnDeleteMixin)
from edc_model_admin import TabularInlineMixin
from edc_model_admin import audit_fieldset_tuple

from ..admin_site import covid19_register_admin
from ..forms import TemperatureForm, TemperatureRecordsForm
from ..models import Temperature, TemperatureRecords
from .base_admin_model_mixin import ModelAdminMixin


class ModelAdminMixin(ModelAdminNextUrlRedirectMixin,
                      ModelAdminFormInstructionsMixin,
                      ModelAdminFormAutoNumberMixin, ModelAdminRevisionMixin,
                      ModelAdminAuditFieldsMixin, ModelAdminReadOnlyMixin,
                      ModelAdminInstitutionMixin,
                      ModelAdminRedirectOnDeleteMixin,
                      ModelAdminSiteMixin):

    list_per_page = 10
    date_hierarchy = 'modified'
    empty_value_display = '-'


class TemperatureInlineAdmin(TabularInlineMixin, admin.TabularInline):

    form = TemperatureForm
    model = Temperature
    extra = 1

    fieldsets = (
        (None, {
            'fields': (
                'cell',
                'today_date',
                'time_in',
                'time_out',
                'temperature')}),
        audit_fieldset_tuple
    )

    list_display = [
        'created', 'today_date', 'time_in',
        'time_out', 'temperature']

    list_filter = [
        'created', 'today_date', 'time_in', 'time_out', 'user_modified']

    search_fields = ('temperature',)


@admin.register(TemperatureRecords, site=covid19_register_admin)
class TemperatureRecordsAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = TemperatureRecordsForm
    inlines = [TemperatureInlineAdmin]
