from .base_listboard_view import BaseListBoardView


class CtuVisitorListBoardView(BaseListBoardView):

    listboard_url = 'ctu_visitor_listboard_url'
    navbar_selected_item = 'ctu_visitor'
    search_form_url = 'ctu_visitor_listboard_url'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(site_name='ctu', **kwargs)
        return context

    def get_queryset_filter_options(self, request, *args, **kwargs):
        options = super().get_queryset_filter_options(request,
                                                      site_name='ctu',
                                                      *args, **kwargs)

        return options
