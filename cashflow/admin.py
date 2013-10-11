from django.contrib import admin
from models import Account, Currency, AccountOperation

class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

class AccountAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'currency', 'balance')
    fieldsets = (
        ('Required details', {
            'fields': ('user', 'name', 'currency')
        }),
        ('Additional details', {
            'classes': ('collapse',),
            'fields': ('IBAN', 'SWIFTBIC')
        }),
    )

class AccountOperationAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'stamp')
    readonly_fields = ('stamp',)
    fieldsets = (
        ('None', {
            'fields': ('account', 'amount', 'description', 'stamp')
        }),
    )


admin.site.register(Account, AccountAdmin)
admin.site.register(Currency, CurrencyAdmin)
admin.site.register(AccountOperation, AccountOperationAdmin)

