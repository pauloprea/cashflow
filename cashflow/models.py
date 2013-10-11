from django.contrib.auth.models import User
from django.db import models
from django_iban.fields import IBANField, SWIFTBICField

class Currency(models.Model):
    name = models.CharField(max_length=3, verbose_name="Currency name")
    description = models.CharField(max_length=100, verbose_name="Currency description")

    def __unicode__(self):
        return u"%s" % (self.name)

    class Meta:
        verbose_name_plural = "currencies"


class Account(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    IBAN = IBANField(null=True, blank=True)
    SWIFTBIC = SWIFTBICField(null=True, blank=True)
    name = models.CharField(max_length=100,verbose_name="Account name")
    active = models.BooleanField(default=False)
    currency = models.ForeignKey(Currency)

    def __unicode__(self):
        return u"%s's account - %s (%s)" % (self.user, self.name, self.currency)

    def balance(self):
        return self.accountoperation_set.aggregate(models.Sum('amount'))['amount__sum'] or 0

class AccountOperation(models.Model):
    account = models.ForeignKey(Account)
    amount = models.FloatField(verbose_name="Amount")
    stamp = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=255, verbose_name="Details", null=True, blank=True)
    stamp.editable = True

    def __unicode__(self):
        return u"%s: %s%s" % (self.description or 'No details given', self.amount, self.account.currency)


#class Transaction(models.Model):
#    positive = models.ForeignKey(AccountOperation, related_name="positive_op")
#    negative = models.ForeignKey(AccountOperation, related_name="negative_op")
#    date = models.DateField()
#    description = models.CharField(max_length=255, verbose_name="Details", null=True, blank=True)