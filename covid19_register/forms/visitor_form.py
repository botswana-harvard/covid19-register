from django import forms

from edc_base.sites import SiteModelFormMixin

from ..models import Visitor


class VisitorForm(SiteModelFormMixin, forms.ModelForm):

    class Meta:
        model = Visitor
        fields = '__all__'
