from django.contrib import admin
from GamePage.models import Account
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
class AccountInLine(admin.StackedInline):
    model = Account
    can_delete = False
    verboser_name_plural = 'Accounts'
class CustomPanel(UserAdmin):
    inlines =(AccountInLine,)

admin.site.unregister(User)
admin.site.register(User,CustomPanel)
