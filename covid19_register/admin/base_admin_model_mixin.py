from django.contrib import admin

from django_revision.modeladmin_mixin import ModelAdminRevisionMixin
from edc_base.sites.admin import ModelAdminSiteMixin
from edc_model_admin import (
    ModelAdminNextUrlRedirectMixin, ModelAdminFormInstructionsMixin,
    ModelAdminFormAutoNumberMixin, ModelAdminAuditFieldsMixin,
    ModelAdminReadOnlyMixin, ModelAdminInstitutionMixin,
    ModelAdminRedirectOnDeleteMixin)
from edc_model_admin import audit_fieldset_tuple


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

    fieldsets = (
        (None, {
            'fields': (
                'first_name',
                'last_name',
                'dob',
                'gender',
                'identity',
                'cell',
                'physical_address',
                'permit_reason',
                'work_place',
                'today_date',
                'time_in',
                'time_out',
                'temperature')}),
        audit_fieldset_tuple
    )

    radio_fields = {
        'gender': admin.VERTICAL}

    list_display = [
        'created', 'identity', 'cell',
        'first_name', 'last_name', 'temperature']

    list_filter = [
        'created', 'user_created', 'modified', 'user_modified']

    search_fields = (
        'identity', 'cell', 'first_name', 'last_name')
