from django import forms

from edc_base.sites import SiteModelFormMixin

from ..models import Temperature


class TemperatureForm(SiteModelFormMixin, forms.ModelForm):

    identity = forms.CharField(
        label='Identity number/Passport number',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = Temperature
        fields = '__all__'
