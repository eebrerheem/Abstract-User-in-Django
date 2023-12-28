from dataclasses import fields
from django.contrib import admin
from .models import NewUser
from django.contrib.auth.admin import UserAdmin

# class CustomUserAdmin(UserAdmin):
#     fieldsets = (
#         *UserAdmin.fieldsets, (
#             'Aditional Info', {
#                 'fields': (
#                     'other_name', 'date_of_birth', 'phone_number', 'work', 'location'
#                     )
#                 }
#             )
#         )

# admin.site.register(NewUser, CustomUserAdmin)


fields = list(UserAdmin.fieldsets)
fields[1] = ('Personal Info', {'fields': ('first_name', 'last_name', 'other_name', 'email', 'phone_number', 'date_of_birth', 'work', 'location')})
UserAdmin.fieldsets = tuple(fields)

admin.site.register(NewUser, UserAdmin)
