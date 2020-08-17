from .base_listboard_view import BaseListBoardView


class BhpHqVisitorListBoardView(BaseListBoardView):

    listboard_url = 'bhp_hq_visitor_listboard_url'
    navbar_selected_item = 'bhp_hq_visitor'
    search_form_url = 'bhp_hq_visitor_listboard_url'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(site_name='bhp_hq', **kwargs)
        return context

    def get_queryset_filter_options(self, request, *args, **kwargs):
        options = super().get_queryset_filter_options(request,
                                                      site_name='bhp_hq',
                                                      *args, **kwargs)

        return options
