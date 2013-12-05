from django import forms
from .models import Account, Currency
from .fields import CurrencyField, TagsField

# Only used in conjunction with Bootstrap 3
class PaymentForm(forms.Form):
    account = forms.ModelChoiceField(queryset=Account.objects.all())
    currency = forms.ModelChoiceField(queryset=Currency.objects.all(), required=False)
    amount = CurrencyField(decimal_places=2, currency_prefix="GBP")
    tags = TagsField(max_length=255, autocomplete="on")
    description = forms.CharField(widget=forms.Textarea(attrs={"rows": 2}))