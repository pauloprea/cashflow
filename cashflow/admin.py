from django.contrib import admin
from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin
from models import Account, Currency, \
    AccountOperation, Payment, Income, TransferIn, TransferOut


class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


class AccountAdmin(admin.ModelAdmin):
    list_display = ('name', 'user_fullname', 'currency', 'balance')
    fieldsets = (
        ('Required details', {
            'fields': ('user', 'name', 'currency')
        }),
        ('Additional details', {
            'classes': ('collapse',),
            'fields': ('IBAN', 'SWIFTBIC')
        }),
    )

    def user_fullname(self, obj):
        return obj.user.get_full_name()


class IncomeAdmin(PolymorphicChildModelAdmin):
    base_model = AccountOperation


class PaymentAdmin(PolymorphicChildModelAdmin):
    base_model = AccountOperation
    list_display = ('__unicode__', 'stamp')
    readonly_fields = ('stamp',)
    change_form_template = 'cashflow/payment/change_form.html'
    fieldsets = (
        ('Payment details', {
            'fields': ('account', 'date', 'amount', 'tags', 'description')
        }),
        ('Make a payment in a different currency', {
            'classes': ('collapse',),
            'fields': ('currency', 'currency_amount')
        }),
        ('Additional information', {
            'classes': ('collapse',),
            'fields': ('stamp',)
        })
    )


class TransferInAdmin(PolymorphicChildModelAdmin):
    base_model = AccountOperation


class TransferOutAdmin(PolymorphicChildModelAdmin):
    base_model = AccountOperation


class AccountOperationAdmin(PolymorphicParentModelAdmin):
    base_model = AccountOperation
    polymorphic_list = True
    child_models = (
        (Payment, PaymentAdmin),
        (Income, IncomeAdmin),
        (TransferIn,TransferInAdmin),
        (TransferOut,TransferOutAdmin),
    )
    list_display = ('__unicode__', 'operation_icon')
    change_list_template = "cashflow/accountoperation/change_list.html"


admin.site.register(Account, AccountAdmin)
admin.site.register(Currency, CurrencyAdmin)
admin.site.register(AccountOperation, AccountOperationAdmin)