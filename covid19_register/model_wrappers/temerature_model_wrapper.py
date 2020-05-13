from edc_model_wrapper import ModelWrapper


class TemperatureModelWrapper(ModelWrapper):

    model = 'covid19_register.temperature'
    next_url_attrs = ['identity']
    querystring_attrs = ['identity']
