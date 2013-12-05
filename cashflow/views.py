from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import View
from cashflow.forms import PaymentForm
from .models import Account, Currency

# Only used in conjunction with Bootstrap 3
class PaymentView(View):
    template_name = 'cashflow/payment.html'
    form_class = PaymentForm
    latest_account = Account.objects.get(pk=2)
    initial = {'account': latest_account, 'currency': latest_account.currency}
    #TODO: setup initial based on last account. also update the currency based on that
    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name,{'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/success/')

        return render(request, self.template_name, {'form': form})