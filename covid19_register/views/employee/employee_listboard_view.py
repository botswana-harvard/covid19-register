from .base_listboard_view import BaseListBoardView


class EmployeeListBoardView(BaseListBoardView):

    listboard_url = 'employee_listboard_url'
    navbar_name = 'covid_19'
    navbar_selected_item = 'employee'
    search_form_url = 'employee_listboard_url'
