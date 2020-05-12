from django.contrib import admin

from ..admin_site import covid19_register_admin
from ..forms import EmployeeForm
from ..models import Employee
from .base_admin_model_mixin import ModelAdminMixin


@admin.register(Employee, site=covid19_register_admin)
class EmployeeAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = EmployeeForm
