from edc_model_wrapper import ModelWrapper


class TemperatureModelWrapper(ModelWrapper):

    model = 'covid19_register.temperature'
    next_url_attrs = ['identity']
    next_url_name = 'home_url'
    querystring_attrs = ['identity']
