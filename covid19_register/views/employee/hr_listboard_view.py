import re
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.utils.decorators import method_decorator

from ..base_site_listboard_view import BaseSiteListboardView

from ...model_wrappers import EmployeeModelWrapper


class HrListBoardView(BaseSiteListboardView):

    listboard_template = 'employee_listboard_template'
    listboard_url = 'hr_listboard_url'
    listboard_panel_style = 'info'
    listboard_fa_icon = "fa-user-plus"

    model = 'covid19_register.employee'
    model_wrapper_cls = EmployeeModelWrapper
    navbar_selected_item = 'Finance & HR'
    ordering = '-modified'
    paginate_by = 10
    search_form_url = 'hr_listboard_url'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            contact='employee',
            contact_add_url=self.model_cls().get_absolute_url())
        return context

    def get_queryset_filter_options(self, request, *args, **kwargs):
        options = super().get_queryset_filter_options(request, *args, **kwargs)
        if kwargs.get('cell'):
            options.update(
                {'cell': kwargs.get('cell')})
        return options

    def extra_search_options(self, search_term):
        q = Q()
        if re.match('^[A-Z]+$', search_term):
            q = Q(first_name__exact=search_term)
        return q
