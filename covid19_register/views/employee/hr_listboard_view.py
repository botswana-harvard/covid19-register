from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.utils.decorators import method_decorator
import re

from .base_listboard_view import BaseListBoardView


class HrListBoardView(BaseListBoardView):

    listboard_url = 'hr_listboard_url'
    navbar_selected_item = 'hr'
    search_form_url = 'hr_listboard_url'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(site_name='hr', **kwargs)
        return context

    def get_queryset_filter_options(self, request, *args, **kwargs):
        options = super().get_queryset_filter_options(request,
                                                      site_name='hr',
                                                      *args, **kwargs)
        return options
