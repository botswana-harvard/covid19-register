from .base_listboard_view import BaseListBoardView


class AmbitionVisitorListBoardView(BaseListBoardView):

    listboard_url = 'ambition_visitor_listboard_url'
    navbar_selected_item = 'ambition_visitor'
    search_form_url = 'ambition_visitor_listboard_url'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(site_name='ambition', **kwargs)
        return context

    def get_queryset_filter_options(self, request, *args, **kwargs):
        options = super().get_queryset_filter_options(request,
                                                      site_name='ambition',
                                                      *args, **kwargs)

        return options
