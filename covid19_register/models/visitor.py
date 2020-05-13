from django.db import models
from edc_base.model_mixins import BaseUuidModel
from edc_base.sites.site_model_mixin import SiteModelMixin
from edc_search.model_mixins import SearchSlugManager
from edc_search.model_mixins import SearchSlugModelMixin as Base

from .screening_register import ScreeningRegister


class SearchSlugModelMixin(Base):

    def get_search_slug_fields(self):
        fields = super().get_search_slug_fields()
        fields.append('identity')
        fields.append('first_name')
        fields.append('last_name')
        fields.append('cell')
        return fields

    class Meta:
        abstract = True


class VisitorManager(SearchSlugManager, models.Manager):

    def get_by_natural_key(self, identity):
        return self.get(
            identity=identity
        )


class Visitor(
        ScreeningRegister, SiteModelMixin, SearchSlugModelMixin, BaseUuidModel):

    objects = VisitorManager()

    def __str__(self):
        return f'{self.first_name}, {self.last_name} {self.identity}'

    def natural_key(self):
        return (self.identity,)

    class Meta:
        app_label = 'covid19_register'
        verbose_name = "Covid-19 Register"
        verbose_name_plural = "Covid-19 Register"
