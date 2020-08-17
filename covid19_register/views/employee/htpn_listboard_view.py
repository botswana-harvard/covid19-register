from .base_listboard_view import BaseListBoardView


class HptnListBoardView(BaseListBoardView):

    listboard_url = 'hptn_listboard_url'
    navbar_selected_item = 'hptn'
    search_form_url = 'hptn_listboard_url'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(site_name='hptn', **kwargs)
        return context

    def get_queryset_filter_options(self, request, *args, **kwargs):
        options = super().get_queryset_filter_options(request,
                                                      site_name='hptn',
                                                      *args, **kwargs)
        return options
