from django.contrib import admin
from account.models import Account
from django.contrib.auth.models import Group

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    filter_horizontal = ("user_permissions",)
    
admin.site.unregister(Group)