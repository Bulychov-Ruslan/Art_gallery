from django.contrib import admin
from .models import *


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'imageUser', 'bio', 'location', 'birth_date')


admin.site.register(Profile, ProfileAdmin)
