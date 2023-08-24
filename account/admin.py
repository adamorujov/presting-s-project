from django.contrib import admin
from account.models import Account
from django.contrib.auth.models import Group

admin.site.register(Account)
admin.site.unregister(Group)