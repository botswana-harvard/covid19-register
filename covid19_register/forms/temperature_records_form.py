from django import forms

from edc_base.sites import SiteModelFormMixin

from ..models import Temperature, TemperatureRecords


class TemperatureForm(SiteModelFormMixin, forms.ModelForm):

    cell = forms.CharField(
        label='Cell number',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = Temperature
        fields = '__all__'


class TemperatureRecordsForm(SiteModelFormMixin, forms.ModelForm):

    class Meta:
        model = TemperatureRecords
        fields = '__all__'
