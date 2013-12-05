from django.contrib.auth.models import User
from django.db import models
from django.utils.html import format_html

from polymorphic import PolymorphicModel
from django_iban.fields import IBANField, SWIFTBICField
from django.contrib.contenttypes.models import ContentType
import tagging
import datetime
#from taggit.managers import TaggableManager

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

class AccountOperation(PolymorphicModel):
    account = models.ForeignKey(Account)
    amount = models.FloatField(verbose_name="Amount")
    date = models.DateField(verbose_name="Transaction date", default=datetime.date.today())
    tags = tagging.fields.TagField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=255, verbose_name="Details", null=True, blank=True)
    stamp = models.DateTimeField(auto_now_add=True)
    stamp.editable = False

    def __unicode__(self):
        return u"%s: %s%s" % (self.description or 'No details given', self.amount, self.account.currency)
    def operation_icon(self):
        return ''
    operation_icon.short_description = 'Operation'
    operation_icon.allow_tags = True

class Payment(AccountOperation):
    currency = models.ForeignKey(Currency, null=True, blank=True)
    currency_amount = models.FloatField(verbose_name="Currency amount", null=True, blank=True)

    def operation_icon(self):
        return format_html('<span class="glyphicon glyphicon-export"></span>')


class Income(AccountOperation):

    def operation_icon(self):
        return format_html('<span class="glyphicon glyphicon-import"></span>')

class TransferIn(AccountOperation):

    def operation_icon(self):
        return format_html('<span class="glyphicon glyphicon-transfer"></span>'
                           '<span class="glyphicon glyphicon-import"></span>')

class TransferOut(AccountOperation):

    def operation_icon(self):
        return format_html('<span class="glyphicon glyphicon-transfer"></span>'
                           '<span class="glyphicon glyphicon-export"></span>')

#class Transaction(models.Model):
#    positive = models.ForeignKey(AccountOperation, related_name="positive_op")
#    negative = models.ForeignKey(AccountOperation, related_name="negative_op")
#    date = models.DateField()
#    description = models.CharField(max_length=255, verbose_name="Details", null=True, blank=True)























