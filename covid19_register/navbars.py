from edc_navbar import NavbarItem, site_navbars, Navbar

covid19_register = Navbar(name='covid19_register')

covid19_register.append_item(
    NavbarItem(name='covid19_register',
               label='Covid19 Register',
               fa_icon='fa-cogs',
               url_name='covid19_register:home_url'))


site_navbars.register(covid19_register)
