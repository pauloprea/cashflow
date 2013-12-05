from django import forms
import widgets

# Only used in conjunction with Bootstrap 3
class CurrencyField(forms.DecimalField):
    widget = widgets.InputGroupBootstrap3

    def __init__(self, max_value=None, min_value=None, max_digits=None, decimal_places=None,
                 currency_prefix=None, *args, **kwargs):
        self.currency_prefix = currency_prefix
        super(CurrencyField, self).__init__(*args, **kwargs)

    def widget_attrs(self, widget):
        attrs = super(CurrencyField, self).widget_attrs(widget)
        if self.currency_prefix is not None and isinstance(widget, widgets.InputGroupBootstrap3):
            addon = {
                        'value': self.currency_prefix,
                        'position': widgets.ADDON_POSITION_PREFIX,
                        'type': widgets.ADDON_TYPE_LABEL,
                        'links': ['GBP', 'EUR', 'RON']
                     }
            attrs.update({'addon': addon})
        return attrs


class TagsField(forms.CharField):
    widget = widgets.TagInputBootstrap3
    def __init__(self, autocomplete=None, *args, **kwargs):
        self.autocomplete = autocomplete
        super(TagsField, self).__init__(*args, **kwargs)

    def widget_attrs(self, widget):
        attrs = super(TagsField, self).widget_attrs(widget)
        if isinstance(widget, widgets.TagInputBootstrap3):
            attrs.update({'autocomplete': str(self.autocomplete)})
        return attrs