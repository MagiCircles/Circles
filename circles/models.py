from collections import OrderedDict
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.db import models
from magi.item_model import MagiModel, i_choices, getInfoFromChoices
from magi.abstract_models import BaseAccount
from magi.default_settings import DEFAULT_GROUPS
from magi.raw import other_sites

############################################################
# Account

class Account(BaseAccount):

    WEBSITES = OrderedDict([
        (_s['name'], _s)
        for _s in other_sites
    ])
    WEBSITE_CHOICES = WEBSITES.keys()
    i_website = models.PositiveIntegerField('Website', choices=i_choices(WEBSITE_CHOICES))
    website_image = property(getInfoFromChoices('website', WEBSITES, 'image'))
    website_url = property(getInfoFromChoices('website', WEBSITES, 'url'))

    GROUPS = OrderedDict([(group, info) for group, info in DEFAULT_GROUPS if not info.get('requires_staff', False)])
    GROUPS_CHOICES = [(_k, _v['translation']) for _k, _v in GROUPS.items()]
    c_groups = models.TextField(_('Roles'), blank=True, null=True)
    j_settings_per_groups = models.TextField(null=True)

    def __unicode__(self):
        return self.website

    class Meta(BaseAccount.Meta):
        unique_together = (('owner', 'i_website'),)
