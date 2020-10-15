from .base_listboard_view import BaseListBoardView


class HrListBoardView(BaseListBoardView):

    listboard_url = 'hr_listboard_url'
    navbar_selected_item = 'hr_finance'
    search_form_url = 'hr_listboard_url'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(site_name='hr_finance', **kwargs)
        return context

    def get_queryset_filter_options(self, request, *args, **kwargs):
        options = super().get_queryset_filter_options(request,
                                                      site_name='hr_finance',
                                                      *args, **kwargs)
        return options
