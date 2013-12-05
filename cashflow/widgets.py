from django.forms.widgets import format_html
from django.forms.util import flatatt
from django.utils.encoding import force_text
from django.forms.widgets import TextInput

ADDON_TYPE_LABEL = 1
ADDON_TYPE_BUTTON = 2
ADDON_TYPE_DROPDOWN = 3
ADDON_TYPE_SELECT = 4

ADDON_POSITION_PREFIX = 1
ADDON_POSITION_SUFFIX = 2
# addon
#  position
#  value
#  type
#  options

class InputGroupBootstrap3(TextInput):
    def render(self, name, value, attrs=None):
        addon = {}
        if value is None:
            value = ''
        final_attrs = self.build_attrs(attrs, type=self.input_type, name=name)
        if value != '':
            # Only add the 'value' attribute if a value is non-empty.
            final_attrs['value'] = force_text(self._format_value(value))
        if 'addon' in final_attrs:
            addon = final_attrs.pop('addon')
            if set(('position', 'value', 'type', 'links')) > set(addon):
                raise Exception('Insufficient parameters passed to the widget')

            if addon['type'] == ADDON_TYPE_BUTTON:
                addon['html'] = format_html('<span class="input-group-btn"><button class="btn btn-default" '
                                            'type="button">{0}</button></span>', addon.get('value'))
            elif addon['type'] == ADDON_TYPE_DROPDOWN:
                choices = format_html(''.join([format_html('<li><a href="{1}">{0}</a></li>', x, y) for (x, y) in addon['options']]))
                addon['html'] = format_html('<div class="input-group-btn"><button type="button" '
                                            'class="btn btn-default dropdown-toggle" '
                                            'data-toggle="dropdown">{0} <span class="caret"></span></button>'
                                            '<ul class="dropdown-menu">{1}'
                                            '</ul></div>', addon.get('value'), choices)
            else:
                addon['html'] = format_html('<span class="input-group-addon">{0}</span>', addon.get('value'))
        return format_html('<div class="input-group">{0}<input{1} />{2}</div>',
                    addon['html'] if addon['position']== ADDON_POSITION_PREFIX else '' ,
                    flatatt(final_attrs),
                    addon['html'] if addon['position']== ADDON_POSITION_SUFFIX else '')

class TagInputBootstrap3(TextInput):
    def render(self, name, value, attrs=None):
        if value is None:
            value = ''
        final_attrs = self.build_attrs(attrs, type=self.input_type, name=name)
        if value != '':
            # Only add the 'value' attribute if a value is non-empty.
            final_attrs['value'] = force_text(self._format_value(value))
        return format_html('<input{0} />',flatatt(final_attrs))




#<input type="text" autocomplete="off" name="tagsk" placeholder="Tags" style="width:9em;" class="input-medium tm-input tm-input-success" data-original-title=""/>