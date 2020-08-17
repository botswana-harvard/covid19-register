from .base_listboard_view import BaseListBoardView


class VisitorListBoardView(BaseListBoardView):

    listboard_url = 'visitor_listboard_url'
    navbar_name = 'covid_19'
    navbar_selected_item = 'visitor'
    search_form_url = 'visitor_listboard_url'
