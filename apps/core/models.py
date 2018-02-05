from django.db import models
from django.utils.translation import ugettext_lazy as _


class Address(models.Model):
    place_id = models.CharField(
        max_length=250,
        verbose_name=_('address'),
        unique=True,
    )
    address = models.CharField(
        max_length=250,
        verbose_name=_('address'),
    )
    latitude = models.FloatField(
        verbose_name=_('latitude'),
    )
    longitude = models.FloatField(
        verbose_name=_('longitude'),
    )
    elevation = models.FloatField(
        verbose_name=_('elevation'),
    )

    class Meta:
        verbose_name = _('address')
        verbose_name_plural = _('addresses')

    def __str__(self):
        return "{}".format(self.address)
