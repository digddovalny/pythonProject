from django.contrib import admin

from users.models import User

from baskets.admin import BasketTableAdmin


# admin.site.register(User)
# admin.site.register(Products)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'email', ]
    search_fields = ['username', 'first_name', 'last_name', 'email', ]

    inlines = [BasketTableAdmin, ]
