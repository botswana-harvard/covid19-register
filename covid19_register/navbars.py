from django.conf import settings

from edc_navbar import NavbarItem, site_navbars, Navbar

covid19_register = Navbar(name='covid19_register')

covid19_register.append_item(
    NavbarItem(
        name='visitor',
        title='Visitor',
        label='Visitor',
        fa_icon='fa-user-plus',
        url_name=settings.DASHBOARD_URL_NAMES.get(
            'visitor_listboard_url')))

covid19_register.append_item(
    NavbarItem(
        name='employee',
        title='Employee',
        label='Employee',
        fa_icon='fa-user-plus',
        url_name=settings.DASHBOARD_URL_NAMES.get(
            'employee_listboard_url')))


site_navbars.register(covid19_register)
