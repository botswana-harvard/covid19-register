from django.contrib import admin

from ..admin_site import covid19_register_admin
from ..forms import VisitorForm
from ..models import Visitor
from .base_admin_model_mixin import ModelAdminMixin


@admin.register(Visitor, site=covid19_register_admin)
class VisitorAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = VisitorForm
