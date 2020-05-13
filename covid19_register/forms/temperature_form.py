from django import forms

from edc_base.sites import SiteModelFormMixin

from ..models import Temperature


class TemperatureForm(SiteModelFormMixin, forms.ModelForm):

    class Meta:
        model = Temperature
        fields = '__all__'
