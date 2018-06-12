from django.utils.html import mark_safe
from magi.magicollections import (
    MagiCollection,
    AccountCollection as _AccountCollection,
    ActivityCollection as _ActivityCollection,
    UserCollection as _UserCollection,
    NotificationCollection as _NotificationCollection,
    DonateCollection as _DonateCollection,
)
from magi.utils import staticImageURL, setSubField
from circles import forms, models

############################################################
# MagiCircles base

class AccountCollection(_AccountCollection):
    title = 'Roles per website'
    plural_title = 'Websites contributed to'
    form_class = forms.AccountForm
    navbar_link = False
    reportable = False

    class ItemView(_AccountCollection.ItemView):
        def to_fields(self, item, images=None, *args, **kwargs):
            if images is None: images = {}
            images.update({
                'website': item.website_image,
                'groups': staticImageURL(item.groups[0], folder='groups', extension='png') if item.groups else None,
            })
            fields = super(AccountCollection.ItemView, self).to_fields(item, *args, images=images, **kwargs)
            setSubField(fields, 'website', key='type', value=u'link')
            setSubField(fields, 'website', key='value', value=item.website_url)
            setSubField(fields, 'website', key='link_text', value=item.website)
            return fields

class UserCollection(_UserCollection):
    reportable = False

    class ItemView(_UserCollection.ItemView):
        share_enabled = False
        follow_enabled = False

        def buttons_per_item(self, request, context, item):
            buttons = super(UserCollection.ItemView, self).buttons_per_item(request, context, item)
            if 'block' in buttons:
                del(buttons['block'])
            return buttons

class DonateCollection(_DonateCollection):
    enabled = True

class ActivityCollection(_ActivityCollection):
    enabled = False

class NotificationCollection(_NotificationCollection):
    enabled = False

############################################################
############################################################
############################################################
