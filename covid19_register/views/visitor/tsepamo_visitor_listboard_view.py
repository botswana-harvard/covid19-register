from .base_listboard_view import BaseListBoardView


class TsepamoVisitorListBoardView(BaseListBoardView):

    listboard_url = 'tsepamo_visitor_listboard_url'
    navbar_selected_item = 'tsepamo_visitor'
    search_form_url = 'tsepamo_visitor_listboard_url'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(site_name='tsepamo', **kwargs)
        return context

    def get_queryset_filter_options(self, request, *args, **kwargs):
        options = super().get_queryset_filter_options(request,
                                                      site_name='tsepamo',
                                                      *args, **kwargs)

        return options
